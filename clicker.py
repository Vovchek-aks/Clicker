import mouse as ms
import keyboard as kb
import pyautogui as ag
import time
import os
from settings import *


LEFT = 'left'
RIGHT = 'right'

scr_name = 'screenshot.png'
running = True


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


def wait(sec):
    if sec <= 0:
        return
    for i in range(sec):
        time.sleep(1)
        kpp()


kb.add_hotkey("esc", stop)
SCREEN = ag.screenshot(scr_name)
SCREEN_PX = SCREEN.load()


# screenshot()

if __name__ == '__main__':
    stop()
