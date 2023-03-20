import pytesseract
from PIL import Image
def handle_uploaded_file(f):
    with open('firstapp/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    img = Image.open('firstapp/static/upload/'+f.name)
    print(img)
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    result = pytesseract.image_to_string(img)
    with open('firstapp/static/upload/abc.txt', 'w') as file:
        file.write(result)
    return result