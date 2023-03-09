import tkinter as tk
import webbrowser
from PIL import Image, ImageTk

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("+{}+{}".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.master.overrideredirect(True)
        self.master.lift()
        self.master.wm_attributes("-topmost", True)
        self.master.bind("<Button-1>", self.callback)

        self.image = tk.PhotoImage(file="rabbit.png")
        self.image = self.image.subsample(10)

        self.label = tk.Label(self.master, image=self.image, bd=0)
        self.label.pack()

        self.master.after(1000, self.slide_in)

    def slide_in(self):
        self.master.geometry("{}x{}+{}+{}".format(self.image.width(), self.image.height(),
                                                   self.master.winfo_screenwidth(), self.master.winfo_screenheight() - self.image.height()))
        self.master.after(10, self.animate_slide)

    def animate_slide(self):
        if self.master.winfo_x() > self.master.winfo_screenwidth() - self.image.width() - 10:
            self.master.geometry("{}x{}+{}+{}".format(self.image.width(), self.image.height(),
                                                       self.master.winfo_x() - 10, self.master.winfo_y()))
            self.master.after(10, self.animate_slide)

    def callback(self, event):
        webbrowser.open("http://www.example.com")
        self.master.destroy()

root = tk.Tk()
app = App(root)
root.mainloop()
