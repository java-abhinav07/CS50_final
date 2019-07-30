# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:43:26 2019

@author: javaa
"""

import RPi.GPIO as gpio
import time
import tkinter as tk
import sys

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward(t):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(t)
    gpio.cleanup()

def backward(t):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(15, False)
    gpio.output(13, True)
    time.sleep(t)
    gpio.cleanup()

def right(t):
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    time.sleep(t)
    gpio.cleanup()


def left(t):
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(t)
    gpio.cleanup()

def key_input(event):
    init()
    print('Key:', event.char)
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        backward(sleep_time)
    elif key_press.lower() == 'd':
        left(sleep_time)
    elif key_press.lower() == 'a':
        right(sleep_time)
    else:
        pass

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()


