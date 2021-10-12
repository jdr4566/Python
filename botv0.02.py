#Gathering bot by Boogies

#V0.02      **V0.02 Changed to LocateOnScreen image detections vs old RGB , XY Detection**

#This program is in alpha testing, purpose is to auto gather trees and repair axe, will not dump inventory yet...



from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


while 1:
    if pyautogui.locateOnScreen('Tree.png', confidence=0.8) != None:
        print("Tree Sighted!!")
        time.sleep (0.5)

    else:
        print ("NO TREE FOUND!! ERROR!!")
        time.sleep(0.5)
        

