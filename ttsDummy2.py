from PIL import Image
import pytesseract
from tts import Say

img = Image.open('test.png')
text = pytesseract.image_to_string(img)

Say(text)