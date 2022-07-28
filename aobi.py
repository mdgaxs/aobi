from adb import *


if __name__ == '__main__':

    while True:
        while True:
            point = match('blank', 0.9)
            if point is None:
                break
            click(*point)
            wait(0.5)
            swipe(*match('yama'), 950, 515, 750)
            wait(0.2)
    
        wait(15 * 60 - 20)
    
        while True:
            point = match('myama', 0.8)
            if point is None:
                break
            click(*point)
            wait(0.5)
            swipe(820, 460, 1100, 700, 800)
            wait(0.2)
