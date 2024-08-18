import cv2
import pytesseract
from pdf2image import convert_from_path

pages = convert_from_path(r'C:\Users\fk-sl\PycharmProjects\readPDF\example.pdf', 100, poppler_path=r'C:\Users\fk-sl\Downloads\Release-24.07.0-0.zip')
pages[1].save('out.jpg', 'JPEG')

imgcv=cv2.imread('out.jpg')
imgcv=cv2.cvtColor(imgcv, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(imgcv,  lang='rus'))