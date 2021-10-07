#######################################################################################################################
import time
import os
import pyautogui
import pyautogui as pyautogui
import pydirectinput
import autoit
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch
from pynput.keyboard import Key, Controller

clear = lambda: os.system("cls")

pyautogui.FAILSAFE = False

keyb = Controller()
mouse = Controller()

print("  _________.__    .__             ___.   .__  _________________________________")
print(" /   _____/|  |__ |__| ____   ____\_ |__ |__| \__    ___/\_   _____/\__    ___/")
print(" \_____  \ |  |  \|  |/    \ /  _ \| __ \|  |   |    |    |    __)    |    |   ")
print(" /        \|   Y  \  |   |  (  <_> ) \_\ \  |   |    |    |     \     |    |   ")
print("/_______  /|___|  /__|___|  /\____/|___  /__|   |____|    \___  /     |____|   ")
print("        \/      \/        \/           \/                     \/               ")

time.sleep(2)

def newTab():
    play = imagesearch('./content/play.png')
    pyautogui.click(play)

    time.sleep(1)
    pvp = pyautogui.locateCenterOnScreen('./content/pvp1.png') or pyautogui.locateCenterOnScreen('./content/pvp2.png') or pyautogui.locateCenterOnScreen('./content/pvp3.png') or pyautogui.locateCenterOnScreen('./content/pvp4.png')
    pyautogui.click(pvp)

    time.sleep(1)
    tft = pyautogui.locateOnScreen('./content/tft1.png') or pyautogui.locateOnScreen('./content/tft2.png') or pyautogui.locateOnScreen('./content/tft3.png')
    pyautogui.click(tft)

    time.sleep(1)
    normal = pyautogui.locateCenterOnScreen('./content/normal1.png')
    pyautogui.click(normal)

    time.sleep(1)
    confirm = pyautogui.locateCenterOnScreen('./content/confirm.png')
    pyautogui.click(confirm)
    pyautogui.moveTo(0, 0)
newTab()

time.sleep(1)

                                    #QUEUE

import __main