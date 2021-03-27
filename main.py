from clicker import *


np = 29

f = 0

wait(4)

for i in range(np):

    # print("new person")

    # new page

    pos = mmx, mmy = ms.get_position()

    click(RIGHT, pos)
    wait(1)
    click(LEFT, (ms.get_position()[0] + 100, ms.get_position()[1] + 10))
    wait(10) # time for load page

    # add friend
    click(LEFT, (300, 10))
    wait(1)
    click(LEFT, (1000, 250))
    wait(5)

    # go back
    click(LEFT, (431, 10))
    wait(1)
    ms.move(pos)

    # new person
    ms.wheel(-1)
    wait(1)
    ms.move(ms.get_position()[0], ms.get_position()[1] - 70)

    if ms.get_position()[1] < 100:
        ms.move(ms.get_position()[0], ms.get_position()[1] + 29 * 10 - 4 * f)
        f = 1 - f

    print(i + 1)
    wait(1)





