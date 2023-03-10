from tkinter import *
from tkinter import ttk


   
def show_loading_screen():
    loading_screen = Toplevel() 
    loading_screen.title("Loading...")
    loading_screen.geometry("300x100")
    loading_screen.resizable(False, False)
    
    label = ttk.Label(loading_screen, text="Please wait while the program is loading...")
    label.pack(pady=20)
    
    progress_bar = ttk.Progressbar(loading_screen, orient=HORIZONTAL, length=200, mode="indeterminate")
    progress_bar.pack(pady=10)
    progress_bar.start()


    loading_screen.destroy()
