from main import *


pos_w = (1500, 400)
pos_i = (520, 1050)

np = int(input('на 1 ip: '))  # на 1 ip
nc = int(input('количество переключений: '))  # переключение ip

# np = 0
# nc = 10

time.sleep(10)

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
        kpp()  # open page

        click('left', (300, 10))
        time.sleep(1)
        kpp()
        click('left', (1000, 250))
        time.sleep(5)
        kpp()  # add friend

        click('left', (431, 10))
        time.sleep(1)
        kpp()
        click('left', pos_i)
        time.sleep(1)
        ms.move(mmx, mmy)
        kpp()  # go back

        ms.wheel(-1)
        time.sleep(1)
        kpp()
        ms.move(0, -70, absolute=False)
        kpp()  # next user

        if ms.get_position()[1] < 100:
            ms.move(0, 29 * 10 - 4 * f, absolute=False)
            f = 1 - f  # nado

        print(i + 1 + j * np)
        time.sleep(1)
        kpp()

    print("reload")
    mmx, mmy = ms.get_position()
    kpp()

    click('left', (pos_i[0] - 40, pos_i[1]))
    time.sleep(1)
    kpp()
    click('left', )
    time.sleep(1)
    kpp()
    click('left', (pos_w[0], pos_w[1] + 200))
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

    print("reload_end")


stop()




