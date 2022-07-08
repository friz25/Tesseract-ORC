import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

"""Будет выведен весь текст с картинки (в формате string)"""
config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=config))
"""
H: Hey, this text is just amazing!
Maybe will you put a like on this video?
"""


""" чтото покруче"""
data = pytesseract.image_to_data(img, config=config)

# for el in data.splitlines():
#     print(el)
#     """
#     5	1	1	1	1	2	140	80	92	48	96.502541	Hey,
#     5	1	1	1	1	3	247	78	77	38	96.321396	this
#     5	1	1	1	1	4	337	85	85	31	96.560280	text
#     5	1	1	1	1	5	437	80	30	36	96.047729	is
#     """

for i, el in enumerate(data.splitlines()):
    if i == 0:
        continue
    try:
        el = el.split()
        x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        cv2.rectangle(img, (x, y), (w + x, h + y), (0,0,255), 1) #коорд начала, (ширина, высота), (цвет обводки), толщина)
        cv2.putText(img, el[11], (x,y), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 1)
    except IndexError:
        print("Операция была пропущена")


cv2.imshow('Result', img)
cv2.waitKey(0)