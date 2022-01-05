import sys
import threading
import random
import os
import time


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


mutex = threading.Lock()
tree = list(open(resource_path('data_files/tree.txt')).read().rstrip())
print(''.join(tree))
print(''.join("   SEE YOU NEXT YEAR :)"))


# returns colored symbol
def colored_dot(color) :
    if color == "yellow":
        return f'\033[93m○\033[0m'
    elif color == "red":
        return f'\033[91m○\033[0m'
    elif color == "green":
        return f'\033[92m○\033[0m'
    elif color == "blue":
        return f'\033[94m○\033[0m'
    elif color == "whiteStar":
        return f'\033[95m☺\033[0m'
    elif color == "woodBrown":
        return f'\033[33mW\033[0m'


# changes color
def lights(color, indexes):
    off = True
    while True:
        color_code = random.choice(['91m', '92m', '93m', '94m', '95m', '96m', '97m', '98m', '99m'])

        for idx in indexes:
            if off:
                tree[idx] = colored_dot(color)
            elif color == "whiteStar":
                tree[idx] = '☺'
            elif color == "woodBrown":
                tree[idx] = f'\033[33mW\033[0m'
            else:
                tree[idx] = '○'

        mutex.acquire()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(tree))
        print(''.join(f'\033[' + color_code + "   SEE YOU NEXT YEAR :)" + '\033[0m'))
        mutex.release()

        off = not off
        time.sleep(random.uniform(.5, 1.5))


yellow = []
red = []
green = []
blue = []
whiteStar = []
woodBrown = []

for i, character in enumerate(tree):
    if character == 'Y':
        yellow.append(i)
        tree[i] = '○'
    elif character == 'R':
        red.append(i)
        tree[i] = '○'
    elif character == 'G':
        green.append(i)
        tree[i] = '○'
    elif character == 'B':
        blue.append(i)
        tree[i] = '○'
    elif character == 'S':
        whiteStar.append(i)
        tree[i] = '☺'
    elif character == 'W':
        woodBrown.append(i)
        tree[i] = f'\033[33mW\033[0m'

# threading for animation
ty = threading.Thread(target=lights, args=('yellow', yellow))
tr = threading.Thread(target=lights, args=('red', red))
tg = threading.Thread(target=lights, args=('green', green))
tb = threading.Thread(target=lights, args=('blue', blue))
ts = threading.Thread(target=lights, args=('whiteStar', whiteStar))
tw = threading.Thread(target=lights, args=('woodBrown', woodBrown))

for t in [ty, tr, tg, tb, ts, tw]:
    t.start()

for t in [ty, tr, tg, tb, ts, tw]:
    t.join()
