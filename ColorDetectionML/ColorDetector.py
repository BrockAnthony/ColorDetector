# imports
import argparse
import pandas as pd
import cv2
import easydict

# argument parser that takes in image path
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")

args = easydict.EasyDict({'image': '/Users/brockada/Desktop/ColorDetectionML/colorpic.jpg'})
image_path = args['image']

# Using opencv to read image
img = cv2.imread(image_path)

# Using pandas to read in CSV file; naming each column
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']

# declaring global variables
b = g = r = xpos = ypos = 0
clicked = False

df = pd.read_csv('/Users/brockada/Desktop/ColorDetectionML/colors.csv', names=index, header=None)


# Calculates distance to the nearest color and finds that color's name
def getColorName(R, G, B):
    minDistance = 10000
    for i in range(len(df)):
        dist = abs(R - int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(B - int(df.loc[i, 'B']))
        if dist <= minDistance:
            minDistance = dist
            name = df.loc[i, 'color_name']
    return name


# draw_function : calculates x,y coordinate values of clicked pixel
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global clicked, b, g, r, xpos, ypos
        clicked = True
        r = img[y,x][0]
        g = img[y,x][1]
        b = img[y,x][2]
        b = int(b)
        g = int(g)
        r = int(r)
        xpos = x
        ypos = y


# Mouse callback event
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while 1:
    cv2.imshow('image', img)
    if clicked:
        # cv2.rectangle(image, start point, endpoint, color, thickness)
        # -1 thickness fills entire rectangle
        cv2.rectangle(img, (20, 20), (1000, 1000), (b, g, r), -1)

        # Displays text of color name and RGB values
        text = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(image, text, start, font(0-7), fontScale, color, thickness, lineType)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # display text in black if color is bright
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # breaks loop if user hits 'q' or esc key
    # 27 is the esc key, 113 is the 'q' key
    key = cv2.waitKey(0)

    if key == 27 or key == 113:
        break

cv2.destroyAllWindows()
