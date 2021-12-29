import pyautogui
import time
import cv2
import numpy as np
from PIL import ImageGrab, Image
import pytesseract

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 5 SECONDS DELAY TO EXECUTE CODE (PREPARE GAME FULLSCREEN)
time.sleep(5)
pyautogui.click()

# All Desired elements list (Mythic/Legend)
desiredElements = ['dragon', 'heaven\'s wrath', 'acceleration', 'arc of the elements', 'time', 'destruction', 'telekinesis', 'necromancer', 'prism', 'lunar', 'phoenix', 'mechanization','solar', 'cosmic', 'hydra', 'armament', 'sound']

# initial x and y to get desired color in the screen
ix = 425
iy = 312
# final x and y to get desired color in the screen
fx = 588
fy = 350

spins = 0

def apply_threshold(img, argument):
    switcher = {
        1: cv2.threshold(cv2.GaussianBlur(img, (3, 3), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1],
        2: cv2.threshold(cv2.GaussianBlur(img, (1, 1), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]}
    return switcher.get(argument, "Invalid method")

def get_string():
    # Read image using opencv
    img = cv2.imread('tmp.png')

    # Rescale the image
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    # Gray scale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    img_t = apply_threshold(img, 1)
    cv2.imwrite('c:/Users/ERGE 2/Desktop/Script Python Professional Text/image_filtered.png', img_t)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(img_t, lang="eng")

    return result

time.sleep(6.1)  # Initial Delay
while True:
    spins += 1

    # GET SCREENSHOT OF GOT ELEMENT
    im = ImageGrab.grab([ix, iy, fx, fy])
    im.save('tmp.png')

    # GET ELEMENT NAME STRING BY IMAGE
    text = get_string()

    if text == '':
        element = '???'
    else:
        element = text[7:len(text) - 2].strip()

    print('Got element: ' + element + ' | Total Spins: ' + str(spins))

    # Verify if current element is a Mythic/Legend element
    for de in desiredElements:
        if element.lower() == de.lower() or element == '???':
            print('You got a Mythic/Legend Element !!')
            quit()
        else:
            continue

    pyautogui.click()
    time.sleep(6.2)  # time to next spin
