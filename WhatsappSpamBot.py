from pynput.keyboard import Key, Controller
import time

Keyboard=Controller()
time.sleep(10)

while True:
    for i in "Happy Birthday Aidan":

        Keyboard.press(i)
        Keyboard.release(i)
       
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)

