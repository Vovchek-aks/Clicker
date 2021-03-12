import mouse as ms
import keyboard as kb
import pyautogui as ag
import time
import os
from settings import *


LEFT = 'left'
RIGHT = 'right'


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


def click(b, pos=None):
    if pos is None:
        pos = ms.get_position()
    ms.move(*pos)
    ms.click(b)


kb.add_hotkey("esc", stop)
SCREEN = ag.screenshot(scr_name)
SCREEN_PX = SCREEN.load()

running = True

# screenshot()

if __name__ == '__main__':
    while running:
        print(ms.get_position())

    stop()
