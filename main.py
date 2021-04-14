from clicker import *

# ========settings==========

np = 29  # on 1 ip

# ==========================

wait(10)

# start

f = 0  # dont touch

while True:
    i = 0
    _time = time.time()
    while i < np:
        fl = True
        # print("new person")

        # new page
        pos = mmx, mmy = ms.get_position()

        click(RIGHT, ms.get_position())
        wait(2)
        click(LEFT, (ms.get_position()[0] + 100, ms.get_position()[1] + 10))
        wait(10)  # time for load page

        # add friend
        click(LEFT, (300, 10))
        wait(2)
        if get_px((1144, 256)) == (255, 255, 255):
            fl = False
        else:
            click(LEFT, (1000, 250))
            wait(10)

        # go back
        click(LEFT, (431, 10))
        wait(2)
        ms.move(mmx, mmy, absolute=True)

        # new person
        ms.wheel(-1)
        wait(2)

        # end?
        try:
            Screen.shot()
        except Exception as x:
            input(x)
        ppos = (1850, 950)
        kpp()
        # print(clr)
        if get_px(ppos) == (246, 248, 253):
            import sender

            wait(1)
            exit(0)

        ms.move(mmx, mmy, absolute=True)

        wait(2)
        ms.move(ms.get_position()[0], ms.get_position()[1] - 70, absolute=True)

        if ms.get_position()[1] < 100:
            ms.move(ms.get_position()[0], ms.get_position()[1] + 29 * 10 - 4 * f)
            f = 1 - f

        wait(1)

        if fl:
            print(i + 1)
            i += 1
        print(f'---{i}')

    dmx, dmy = ms.get_position()
    if time.time() - _time < 3600:
        print(f"ждём {3600 - time.time() + _time}sec")
        # click(LEFT, (400, 1060))
        wait(3600 - time.time() + _time)
    print("выхожу на работу")
    ms.move(dmx, dmy, absolute=True)

    # stop()

input('end')
