import sys
import os
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


class Shotlocker:
    def __init__(self): ## This function will run when a instance of Shotlocker is made setting up the window
        self.root = Tk()
        self.root.title("ShotLocker")
        
        

        self.build_ui() ## Call to build UI after the window is set up


    def build_ui(self):
        self.mainframe = ttk.Frame(self.root, padding=5)
        self.mainframe.grid(column=0, row=0)


        self.add_game_button = ttk.Button(self.mainframe, text='Add Game', command=self.add_game_tile)
        self.add_game_button.grid(column=0, row=0)



    cover_ref = [] ## This keeps the garbage collector from breaking the images on the game tiles (buttons)
    game_start_ref = []
    def add_game_tile(self):
           global cover_ref
           global game_start_ref
           self.columns = 6
           self.current_count = len(self.mainframe.winfo_children())
           self.row = self.current_count // self.columns
           self.col = self.current_count % self.columns


           self.cover = self.image_res() ## Calls image res works it into car then appened below
           self.cover_ref.append(self.cover) ## Stops the image button glitch


           self.temp_path = self.choose_game_file()
           self.game_card = {
               "path": self.temp_path
           }
           self.game_start_ref.append(self.game_card)


           self.game_card_button = ttk.Button(self.mainframe, image=self.cover, command=lambda: self.run_game(self.temp_path))
           self.game_card_button.grid(column=self.col, row=self.row)


        
    def image_res(self):
        self.raw_img = Image.open("WoW_forever.png")
        self.scaled_img = self.raw_img.resize((160, 240), Image.Resampling.LANCZOS)
        self.cover_photo = ImageTk.PhotoImage(self.scaled_img)
        return self.cover_photo



    def choose_game_file(self):
        self.file_path = filedialog.askopenfilename(title="Select a games exe/application file") ## NOTE: THIS IS NOT USED AND OUT DATED FIX LATER 
        return self.file_path


    def run_game(self, path):
        os.startfile(path)




    def run(self): ## Starts the event loop must be called
        self.root.mainloop()



app = Shotlocker() 
app.run()

   