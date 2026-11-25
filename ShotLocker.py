import sys
from tkinter import *
from tkinter import ttk



class Shotlocker:
    def __init__(self): ## This function will run when a instance of Shotlocker is made setting up the window
        self.root = Tk()
        self.root.title("ShotLocker")
        

        self.build_ui() ## Call to build UI after the window is set up
        self.game_devide() ## Useless remove later 


    def build_ui(self):
        self.mainframe = ttk.Frame(self.root, padding=5)
        self.mainframe.grid(column=0, row=0)


        self.add_game_button = ttk.Button(self.mainframe, text='Add Game', command=self.add_game_tile)
        self.add_game_button.grid(column=0, row=0)


    
    row_count = 1 ## This is the counter for testing the row and grid layout
    def add_game_tile(self):
        global row_count


        self.new_label = ttk.Label(self.mainframe, padding=5, text="Tile Testing")
        self.new_label.grid(column=0, row=self.row_count)


        self.row_count += 1
        print(self.row_count)       


    def  game_devide(self): 
       self.game_count = 25
       self.col = 6
       for i in range(self.game_count):
           self.temp_row = i // self.col
           self.columns = i % self.col
            




    def run(self): ## Starts the event loop must be called
        self.root.mainloop()


app = Shotlocker() 
app.run()

   