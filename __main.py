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

time.sleep(2)

while True:

    time.sleep(1)
    # QUEUE

    while True:
        if pyautogui.locateCenterOnScreen('./content/findm1.png'):
            pyautogui.click('./content/findm1.png')
            print("Na fila")
            pyautogui.moveTo(0, 0)

        if pyautogui.locateCenterOnScreen('./content/accept.png'):
            pyautogui.click('./content/accept.png')
            print("Jogo aceito!")
            pyautogui.moveTo(0, 0)

        if pyautogui.locateCenterOnScreen('./content/select.png'):
            break

            # GAME
    print("Tela de carregamento")
    pyautogui.click(1000, 550)

    while True:
        if pyautogui.locateCenterOnScreen('./content/start.png'):
            break

    print("Jogo Iniciado")

    while True:
        if pyautogui.locateCenterOnScreen('./content/estagio.png'):
            break

    time.sleep(2)
    autoit.mouse_click("left", 1234, 869)

    time.sleep(40)
    autoit.mouse_click("left", 973, 866)
    autoit.mouse_click("left", 700, 865)
    autoit.mouse_click("left", 565, 850)

    time.sleep(40)
    autoit.mouse_click("left", 1234, 869)
    autoit.mouse_click("left", 1102, 865)
    autoit.mouse_click("left", 565, 850)

    ############################################

    time.sleep(40)
    autoit.mouse_click("left", 1234, 869)
    autoit.mouse_click("left", 836, 866)
    autoit.mouse_click("left", 565, 850)

    time.sleep(40)
    autoit.mouse_click("left", 1234, 869)
    autoit.mouse_click("left", 1102, 865)
    autoit.mouse_click("left", 565, 850)

    time.sleep(40)
    autoit.mouse_click("left", 836, 866)
    autoit.mouse_click("left", 1102, 865)
    autoit.mouse_click("left", 565, 850)

    time.sleep(40)
    autoit.mouse_click("left", 700, 865)
    autoit.mouse_click("left", 836, 866)
    autoit.mouse_click("left", 565, 850)

    time.sleep(40)
    autoit.mouse_click("left", 1234, 869)
    autoit.mouse_click("left", 973, 866)
    autoit.mouse_click("left", 565, 850)

    time.sleep(40)
    autoit.mouse_click("left", 973, 866)
    autoit.mouse_click("left", 700, 865)
    autoit.mouse_click("left", 565, 850)

    time.sleep(40)
    autoit.mouse_click("left", 1234, 869)
    autoit.mouse_click("left", 1102, 865)
    autoit.mouse_click("left", 565, 850)

    time.sleep(40)
    autoit.mouse_click("left", 1234, 869)
    autoit.mouse_click("left", 1102, 865)
    autoit.mouse_click("left", 565, 850)

    time.sleep(40)
    autoit.mouse_click("left", 700, 865)
    autoit.mouse_click("left", 973, 866)
    autoit.mouse_click("left", 565, 850)

    time.sleep(40)
    autoit.mouse_click("left", 700, 865)
    autoit.mouse_click("left", 1102, 865)
    autoit.mouse_click("left", 565, 850)

    time.sleep(40)
    autoit.mouse_click("left", 1102, 865)
    autoit.mouse_click("left", 836, 866)
    autoit.mouse_click("left", 565, 850)

    time.sleep(40)
    autoit.mouse_click("left", 1234, 869)
    autoit.mouse_click("left", 1102, 865)
    autoit.mouse_click("left", 565, 850)

    keyb.press(Key.enter)
    keyb.release(Key.enter)
    time.sleep(1)
    keyb.type('/ff')
    time.sleep(1)
    keyb.press(Key.enter)
    keyb.release(Key.enter)

    while True:
        if pyautogui.locateCenterOnScreen('./content/ff.png'):
            autoit.mouse_click("left", x=878, y=535)
            break
    clear()

    print("  _________.__    .__             ___.   .__  _________________________________")
    print(" /   _____/|  |__ |__| ____   ____\_ |__ |__| \__    ___/\_   _____/\__    ___/")
    print(" \_____  \ |  |  \|  |/    \ /  _ \| __ \|  |   |    |    |    __)    |    |   ")
    print(" /        \|   Y  \  |   |  (  <_> ) \_\ \  |   |    |    |     \     |    |   ")
    print("/_______  /|___|  /__|___|  /\____/|___  /__|   |____|    \___  /     |____|   ")
    print("        \/      \/        \/           \/                     \/               ")

    time.sleep(15)

    while pyautogui.locateCenterOnScreen('./content/ok.png'):
        pyautogui.click('./content/ok.png')
        pyautogui.moveTo(0, 0)
        time.sleep(2)

    while True:
        if pyautogui.locateOnScreen('./content/pagain.png'):
            pyautogui.click(pyautogui.locateOnScreen('./content/pagain.png'))
            pyautogui.moveTo(0, 0)
            break

    time.sleep(2)
