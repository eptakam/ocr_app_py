import pytesseract  # pytesseract is an API for OCR tool
import cv2

# set the tesseract command
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#configurer les parametres de l'OCR pour afficher seulement les chiffres
custom_config = 'digits'

# Path to the image
image_path = "img\ocr_sample.jpg"

# Read the image
img = cv2.imread(image_path)

# Convert the image to string
# il faut noter que pytesseract accepte uniquement les images en format RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert the image to RGB
text = pytesseract.image_to_string(img) # convert the image to string

results = pytesseract.image_to_boxes(img_rgb, config=custom_config) # get the bounding boxes
ih, iw, ic = img.shape  # get the image shape

# image to boxes module
# for box in results.splitlines():
#     # mettre chaque ligne de details dans une liste
#     box = box.split(' ')
#     print(box) # recuperer les coordonnees de chaque element
#
#     # dessiner les bounding boxes
#     x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     cv2.rectangle(img, (x, ih-y), (w, ih-h), (0, 255, 0), 2) # dessiner les bounding boxes
#     # 2 : epaisseur du rectangle
#
#     # ecrire le texte au-dessus de l'image
#     cv2.putText(img, box[0], (x, ih-h), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1) # ecrire le texte sur l'image

# image to data module
data = pytesseract.image_to_data(img_rgb)
for id, line in enumerate(data.splitlines()):
    # eliminer la ligne des titres
    if id != 0:
        # mettre chaque ligne de details dans une liste
        line = line.split()
        if len(line) == 12:
            x, y, w, h = int(line[6]), int(line[7]), int(line[8]), int(line[9])
            cv2.rectangle(img, (x, y), (w + x, h + y), (0, 255, 0), 2)  # dessiner les bounding boxes
            # 2 : epaisseur du rectangle
            # ecrire le texte au-dessus de l'image
            cv2.putText(img, line[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0),
                        1)  # ecrire le texte sur l'image

print()


# display the image
cv2.imshow('Input', img)
cv2.waitKey(0)