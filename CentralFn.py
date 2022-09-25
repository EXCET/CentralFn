import tkinter as tk
from tkinter import *
import pydirectinput
import pyautogui
from pyautogui import *
import customtkinter

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
    for i in range(100):
        pydirectinput.move(None, 25)
        
class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("CentralFN")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180, fg_color='#1d1d1d',
                                                 corner_radius=16)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self, fg_color='#1d1d1d', corner_radius=12)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=0)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, weight=0)  # empty row as spacing
        self.frame_left.grid_rowconfigure(0, minsize=0)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, minsize=0)  # empty row with minsize as spacing



        self.lava_title = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Central Cheat", width=5, height=0,
                                              text_color='red',
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.lava_title.grid(row=0, column=0, pady=0, padx=0, sticky='w')



        self.goto_crash = customtkinter.CTkButton(master=self.frame_left,
                                                hover_color='#2d2d2d',
                                                text_font=("Roboto Medium", -25),
                                                text_color='Red',
                                                text="rapid fire", width=145, height=40, fg_color='#1d1d1d',
                                                command=rapidfire)
        self.goto_crash.grid(row=2, pady=5, padx=20, sticky='nswe')

        self.goto_mines = customtkinter.CTkButton(master=self.frame_left,
                                                hover_color='#2d2d2d',
                                                text_font=("Roboto Medium", -25),
                                                text_color='Red',
                                                text="anti recoil", width=145, height=40, fg_color='#1d1d1d',
                                                command=macro)
        self.goto_mines.grid(row=3, pady=5, padx=20, sticky='nswe')
        self.goto_roulette = customtkinter.CTkButton(master=self.frame_left,
                                                hover_color='#2d2d2d',
                                                text_font=("Roboto Medium", -25),
                                                text_color='Red',
                                                text="Coming Soon", width=145, height=40, fg_color='#1d1d1d',
                                                command=exit)
        self.goto_roulette.grid(row=4, pady=5, padx=20, sticky='nswe')

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)
    
    def open_crash_tab(self):
        # everything you want to show when you click the crash tab should go in this function
        self.crash_test = customtkinter.CTkLabel(master=self.frame_right,
                                            text="Crash\n" + "Predictor", width=5, height=0, fg_color='#1d1d1d',
                                            text_color='Red',
                                            text_font=("Roboto Medium", -65))  # font name and size in px
        self.crash_test.grid(row=1, column=1, pady=15, padx=0, sticky='nswe')

    def open_mines_tab(self):
        self.mines_stuff = customtkinter.CTkLabel(master=self.frame_right,
                                            text="Mines\n", width=5, height=0, fg_color='#1d1d1d',
                                            text_color='Red',
                                            text_font=("Roboto Medium", -65))  # font name and size in px
        self.mines_stuff.grid(row=1, column=1, pady=15, padx=0, sticky='nswe')

        


    def open_roulette_tab(self):
        # everything you want to show when you click the roulette tab should go in this function
        self.roulette_stuff = customtkinter.CTkLabel(master=self.frame_right,
                                            text="Roulette", width=5, height=0, fg_color='#1d1d1d',
                                            text_color='Red',
                                            text_font=("Roboto Medium", -65))  # font name and size in px
        self.roulette_stuff.grid(row=1, column=1, pady=15, padx=0, sticky='nswe')
        
    def crash_predictBtn(self):
        print("Predict")
    def create_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("260x150")
        window.iconbitmap('assets/rocket.ico')
        window.title('Lava Credits')
        label = customtkinter.CTkLabel(master=window, text="Geek#7216",text_font=("Roboto Medium", -35))
        label.grid(row=1, column=1, pady=15, padx=0, sticky='nswe')

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
