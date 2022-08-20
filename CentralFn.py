import tkinter as tk
from tkinter import *
import pydirectinput
import pyautogui
from pyautogui import *

stopfunction = 1

def click():
    for i in range(50):
     if stopfunction == 1:
         pyautogui.click()
         pyautogui.click()
     else:
        quit()

def rapidfire():
    for i in range(100):
        pyautogui.click()
        pydirectinput.move(None, 35)

def cli():
    pyautogui.click()

def macro():
    for i in range(30):
        time.sleep(0.1)
        pydirectinput.move(None, 25)
        

def main():
  print('What Is Your Key')
  key = input("")
  r = tk.Tk()
  r.configure(bg='gray')
  r.title('CentralFn Cheat')
  w = Canvas(r, width=300, height=120, bg='gray')
  w.pack()
  w.configure(bg='gray')
  w = Label(r, text='Central Cheat')
  w.place(x=0, y=0)
  w.xbutton = tk.Button(r, text='Auto Clicker', width=10, fg = 'red', command=click)
  w.xbutton.pack()
  w.redbutton = tk.Button(r, text = 'RapidFire', width=10, fg ='blue', command=rapidfire)
  w.redbutton.pack()
  w.wredbutton = tk.Button(r, text = 'Anti Recoil', width=10, fg ='purple', command=macro)
  w.wredbutton.pack()
  r.mainloop()

main()