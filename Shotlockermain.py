import os
import sqlite3
import requests 
from io import BytesIO
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from pathlib import Path


class ShotLocker:


    def __init__(self):
        self.root = Tk()
        self.root.title("ShotLocker")
        self.root.geometry("960x540")
        self.card_path = []
        ## NOTE Add some kind of setup for sql database here

        self.build_ui()


    def build_ui(self):
        self.mainframe = ttk.Frame(self.root, padding=5)
        self.mainframe.grid(column=0, row=0)

        self.add_game_card = ttk.Button(self.mainframe, text="Add Game EXE/Application file", command=self.exe_select)
        self.add_game_card.grid(column=0, row=0)


    def exe_select(self):
        game_exe = filedialog.askopenfilename(title="Select games EXE or Application file")

        if game_exe:

            game_dir = os.path.dirname(game_exe)
            self.game_card_image_APIcall(game_dir)

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


    def game_card_image_APIcall(self, game_dir):
        for root, dirs, files in os.walk(game_dir):
            for file in files:
                if file == "steam_appid.txt":
                    full_path = os.path.join(root, file)
                    with open(full_path, 'r', encoding='utf-8') as file:
                        for line in file:
                            print(line.strip())
                            url = f'https://steamcdn-a.akamaihd.net/steam/apps/{line.strip()}/library_600x900_2x.jpg'
                            save_path = Path(f'{line}_cover.jpg')

                            response = requests.get(url, timeout=10)
                            if response.status_code == 200:
                                save_path.write_bytes(response.content)
                                print("SAVED")
                            else:
                                print(f'Failed to fetch images HTTP: {response.status_code}') ## FIXME: Make this a pop up that warns the user about the fail and make a way for them to retry it later or the code to try again


        ## NOTE: This will take the steam app id that is in MOST fodlers and use it to find and download the games 600x900 image via the steam CDN. 


    def run(self):
        self.root.mainloop()



app = ShotLocker()
app.run()

