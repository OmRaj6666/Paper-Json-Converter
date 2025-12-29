import pytesseract
from PIL import Image

def extract_text(file):
    """
    Extract text from an uploaded image file using Tesseract OCR
    """
    image = Image.open(file)
    text = pytesseract.image_to_string(image)
    return text
