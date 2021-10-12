#Gathering bot by Boogies

#V0.03  **In V0.03 have restructed method to utilizing OpenCV**

#This program is in alpha testing, purpose is to auto gather trees and repair axe, will not dump inventory yet...



import cv2 as cv
import numpy as np
import pyautogui

#Setting Images to look for
haystack_img = cv.imread('nw.jpg', cv.IMREAD_REDUCED_COLOR_2)
needle_img = cv.imread('Tree.jpg', cv.IMREAD_REDUCED_COLOR_2)


#call Matchtemplate function

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)


# get the best matched position
min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)


print("Best match top left position: %s" %str(max_loc))
print("Best match confidence: %s" %max_val)

#Verifying that image found is within out confidence threshold
threshold = 0.0
if max_val >= threshold:
    print("Found Needle")

    #get dimensions of the needle image
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    #define top_left and bottom_right
    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    #draw a green rectangle around the image
    cv.rectangle(haystack_img, top_left, bottom_right,  
                            color = (0,255,0), thickness = 2, lineType=cv.LINE_4)

else:
    print('Needle not found')



#show results
#cv.imshow('Result', result)

#save result as jpg
cv.imwrite('result.jpg', haystack_img)

#add a pause so we can review the image
cv.waitKey()

#White pixel == best matched locations
#black pixels == worst matched locations

