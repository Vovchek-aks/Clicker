from clicker import *

# ======= settings =========

np = 29  # on 1 ip
TFS = 3600  # sec for sleep
GOOGLE = False

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

        while get_px(ms.get_position()) == (246, 248, 253):
            ms.move(0, 1, absolute=False)
            time.sleep(0.5)
            kpp()

        # new page
        pos = mmx, mmy = ms.get_position()

        click(RIGHT, ms.get_position())
        wait(2)
        click(LEFT, (ms.get_position()[0] + 100, ms.get_position()[1] + 10))
        wait(10)  # time for load page

        # add friend
        click(LEFT, (300, 10))
        wait(2)
        if get_px((1144, 284) if GOOGLE else (1147, 254)) == (255, 255, 255):
            fl = False
        else:
            click(LEFT, (1000, 284) if GOOGLE else (1013, 256))
            wait(10)

        # go back
        click(LEFT, (472, 16) if GOOGLE else (432, 18))
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
            # import sender

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
        else:
            print('Пользователь уже был в друзьях')

    dmx, dmy = ms.get_position()
    tt = time.time() - _time
    tt = round(tt)
    if tt < TFS:
        print(f"ждём {TFS - tt} sec")
        # click(LEFT, (400, 1060))
        wait(TFS - tt)
    print("выхожу на работу")
    ms.move(dmx, dmy, absolute=True)

    # stop()

input('end')
