# import necessary libraries
import argparse
import cv2
import pandas as pd

# read in CSV file as pandas dataframe with named columns
columns = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv('Colors.csv', names=columns, header=None)

# declare global variables
b = g = r = xpos = ypos = 0
clicked = False

# function to calculate the color name based on RGB values
def getColorName(R, G, B):
    minDistance = 10000
    for i in range(len(df)):
        dist = abs(R - int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(B - int(df.loc[i, 'B']))
        if dist <= minDistance:
            minDistance = dist
            name = df.loc[i, 'color_name']
    return name

# function to calculate x, y coordinates of clicked pixel
def draw_function(event, x, y, flags, param):
    global clicked, b, g, r, xpos, ypos
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        r, g, b = map(int, img[y, x]) # get RGB values of clicked pixel
        
        # swap red and blue channels to convert from BGR to RGB
        r, g, b = img[y, x][2], img[y, x][1], img[y, x][0]

        xpos, ypos = x, y

# initialize argument parser to receive image path as argument
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")

# set image path
args = ap.parse_args()
image_path = args.image

# read image using OpenCV
img = cv2.imread(image_path)

# set up mouse callback
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while not clicked: # wait for user to click on image
    cv2.imshow('image', img)
    key = cv2.waitKey(10) & 0xFF # get key pressed by user
    if key == 27 or key == 113: # if user presses 'esc' or 'q', exit loop
        break

# draw rectangle around clicked pixel
cv2.rectangle(img, (xpos, ypos), (xpos, ypos), (int(b), int(g), int(r)), -1)

# get color name and RGB values and display them on the image
color_name = getColorName(r, g, b)
text = f"{color_name} R={r} G={g} B={b}"

#Setting font and padding values
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.6
padding = 5

# calculate size of text box based on font size and text length
(text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness=1)
box_width = text_width + padding*2
box_height = text_height + padding*2

# draw filled rectangle behind text
cv2.rectangle(img, (xpos, ypos - box_height), (xpos + box_width, ypos), (255, 255, 255), -1)

cv2.putText(img, text, (xpos + padding, ypos - padding), font, font_scale, (255, 255, 255), 2)

text_color = (0, 0, 0)
    
cv2.putText(img, text, (xpos + padding, ypos - padding), font, font_scale, text_color, 2)

# show final image with color name and RGB values
cv2.imshow('image', img)

# wait for user to close window
cv2.waitKey(0)

# close window
cv2.destroyAllWindows()