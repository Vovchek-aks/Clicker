import mouse as ms
import keyboard as kb
import pyautogui as ag
import time
import os
from settings import *


def stop():
    global running
    print("end_work")
    running = False
    if os.path.isfile(scr_name):
        os.remove(scr_name)
    exit(0)


def kpp():
    if not running or kb.is_pressed('esc'):
        stop()


def get_px(pos):
    screenshot()
    return SCREEN_PX[pos]


def screenshot():
    global SCREEN, SCREEN_PX
    SCREEN = ag.screenshot(scr_name)
    SCREEN_PX = SCREEN.load()


def click(b, pos=ms.get_position()):
    ms.move(*pos)
    ms.click(b)


kb.add_hotkey("esc", stop)
SCREEN = ag.screenshot(scr_name)
SCREEN_PX = SCREEN.load()

running = True

# screenshot()


np = 25
nc = 12

time.sleep(4)

f = 0
for j in range(nc):
    for i in range(np):

        # print("new person")

        mmx, mmy = ms.get_position()

        click('right')
        time.sleep(1)
        kpp()
        click('left', (mmx + 100, mmy + 10))
        time.sleep(10)
        kpp()

        click('left', (300, 10))
        time.sleep(1)
        kpp()
        click('left', (1000, 180))
        time.sleep(5)
        kpp()

        click('left', (431, 10))
        time.sleep(1)
        kpp()
        ms.move(mmx, mmy)
        kpp()

        ms.wheel(-1)
        time.sleep(1)
        kpp()
        ms.move(0, -70, absolute=False)
        kpp()

        if ms.get_position()[1] < 100:
            ms.move(0, 29 * 10 - 4 * f, absolute=False)
            f = 1 - f

        print(i + 1 + j * np)
        time.sleep(1)
        kpp()

    print("reload")
    mmx, mmy = ms.get_position()
    kpp()

    click('left', (460, 1070))
    time.sleep(1)
    kpp()
    click('left', (1500, 400))
    time.sleep(1)
    kpp()
    click('left', (1500, 600))
    # time.sleep(1)
    # lclick(1500, 630)
    time.sleep(5)
    kpp()

    # re login
    click('right', (mmx, mmy))
    time.sleep(1)
    kpp()
    ms.move(100, 10, absolute=False)
    click('left')
    time.sleep(10)  # time for load page
    kpp()

    click('left', (300, 10))
    time.sleep(1)
    kpp()
    click('left', (1620, 100))
    time.sleep(5)
    kpp()
    click('left', (1000, 350))
    time.sleep(1)
    kpp()
    click('left', (1000, 450))
    time.sleep(2)
    kpp()

    click('left', (431, 10))
    time.sleep(1)
    kpp()
    ms.move(mmx, mmy)
    time.sleep(1)
    kpp()

    # print("reload_end")


stop()
