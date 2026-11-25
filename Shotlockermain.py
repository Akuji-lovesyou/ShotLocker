import os
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


class ShotLocker:


    def __init__(self):
        self.root = Tk()
        self.root.title("ShotLocker")
        self.card_path = []
        ## NOTE Add some kinf of setup for sql database here

        self.build_ui()


    def build_ui(self):
        self.mainframe = ttk.Frame(self.root, padding=5)
        self.mainframe.grid(column=0, row=0)

        self.add_game_card = ttk.Button(self.mainframe, text="Add Game EXE/Application file", command=self.exe_select)
        self.add_game_card.grid(column=0, row=0)


    def exe_select(self):
        game_exe = filedialog.askopenfilename(title="Select games EXE or Application file")

        if game_exe:
            self.create_game_card(game_exe)


    def create_game_card(self, path):
        self.columns = 6
        self.current_count = len(self.mainframe.winfo_children())
        self.row = self.current_count // self.columns
        self.col = self.current_count % self.columns ## BUG NOTE: This works however there is no styling this will need to ne updated later when teh formatting of the application changes


        game_card = {
            "path": path
        }
        self.card_path.append(game_card)
        self.new_game_card_button = ttk.Button(self.mainframe, text='Placeholder', command=lambda: self.run_game(path))
        self.new_game_card_button.grid(column=self.col, row=self.row)


    def run_game(self, path):
        os.startfile(path)



    def run(self):
        self.root.mainloop()



app = ShotLocker()
app.run()

