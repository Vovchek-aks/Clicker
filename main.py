import mouse as ms
import keyboard as kb
import time


def stop():
    global running
    running = False


kb.add_hotkey("esc", stop)

running = True
while running:
    time.sleep(1)
    ms.click('left')
