import numpy as np
import cv2 
from PIL import ImageGrab
import pyautogui

# IMAGE PROCESSING KAARATE CHOP KICK
# https://gamersmoby.com/game-play/karate-chop-kick


# Load the templates
template_left1 = cv2.imread('images/woodleft.jpg', 0)
template_right1 = cv2.imread('images/woodright.jpg', 0)

# Get the dimensions of the template. This is the same size as the match.
h, w  = template_left1.shape

# Define the threshold
threshold = 0.7

# Define the click coordinates
x, y = (333,750)

# Define the side
Side = "Left"

while True:
    # Screen capture based on the side
    if Side == "Left":
        image = np.array(ImageGrab.grab(bbox=(280,620,505,680)))
    else:
        image = np.array(ImageGrab.grab(bbox=(505,620,730,680)))
        
    # Convert to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # Perform the matching
    left = cv2.matchTemplate(image, template_left1, cv2.TM_CCOEFF_NORMED)
    right = cv2.matchTemplate(image, template_right1, cv2.TM_CCOEFF_NORMED)

    
    # Get the best match
    loc_left = np.where(left >= threshold)
    _, max_val_left, _, max_loc_left = cv2.minMaxLoc(left)

    loc_right = np.where(right >= threshold)
    _, max_val_right, _, max_loc_right = cv2.minMaxLoc(right)


    # if match is found, draw a rectangle around it
    if max_val_left > threshold:
        print("Found Left")
        x, y = (650,750)
        Side = "Right"
        cv2.rectangle(image, max_loc_left, (max_loc_left[0] + w, max_loc_left[1] + h), (0,255,255), 5)


    if max_val_right > threshold:
        print("Found Right")
        Side = "Left"
        x, y = (333,750)
        cv2.rectangle(image, max_loc_right, (max_loc_right[0] + w, max_loc_right[1] + h), (0,255,255), 5)

    # Display the image
    # cv2.imshow('Detected', image)

    # Click the mouse
    pyautogui.click(x,y)

    # Press q to quit
    if cv2.waitKey(25) & 0xFF == ord('q'): 
        cv2.destroyAllWindows()
        break

cv2.destroyAllWindows()

