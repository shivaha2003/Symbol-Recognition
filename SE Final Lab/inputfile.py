import pytesseract
from PIL import Image
import pyttsx3
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    with Image.open(image_path) as img:
        extracted_text = pytesseract.image_to_string(img)
        return extracted_text

def generate_audio_from_text(text, output_audio_file):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)   
    engine.setProperty('volume', 0.9) 
    engine.save_to_file(text, output_audio_file)
    engine.runAndWait()

    print("Speech generated successfully!")

print(extract_text_from_image('input.png'))

generate_audio_from_text(extract_text_from_image('input.png'), 'output.mp3')