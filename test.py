import tkinter as tk
import webbrowser
from PIL import Image, ImageTk, ImageEnhance

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("+{}+{}".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()))
        self.master.overrideredirect(True)
        self.master.lift()
        self.master.wm_attributes("-topmost", True)
        self.master.bind("<Button-1>", self.callback)

        # Load the image and make it transparent
        self.image = Image.open("rabbit.png")
        self.image = self.image.subsample(10)
        self.image = self.image.convert("RGBA")
        alpha = self.image.split()[-1]
        alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
        self.image.putalpha(alpha)

        # Create the PhotoImage with the transparent image
        self.image = ImageTk.PhotoImage(self.image)

        # Create a transparent label to hold the image
        self.label = tk.Label(self.master, image=self.image, bd=0)
        self.label.pack()

        # Set the label and window background to transparent
        self.label.configure(background='#000000')
        self.master.config(bg='#000000')
        self.master.attributes('-transparentcolor', '#000000')

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
