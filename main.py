import mouse
import time


def stop():
    global running
    running = False


mouse.on_right_click(stop)

running = True
while running:
    time.sleep(1)
    mouse.click('left')
