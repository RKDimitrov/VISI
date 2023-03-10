import tkinter as tk
import subprocess
import threading
from PIL import Image, ImageTk, ImageEnhance

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("+{}+{}".format(self.master.winfo_screenwidth(), self.master.winfo_screenheight()-100))
        self.master.overrideredirect(True)
        self.master.lift()
        self.master.wm_attributes("-topmost", True)
        self.master.bind("<Button-1>", self.callback)

        # Load the images for the animation and make them transparent
        self.images = []
        for i in range(2):
            image = Image.open(f"../img/rooster_{i}.png")
            image = image.resize((int(image.size[0]/10), int(image.size[1]/10)))
            image = image.convert("RGBA")
            alpha = image.split()[-1]
            alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
            image.putalpha(alpha)
            self.images.append(ImageTk.PhotoImage(image))

        # Create a transparent label to hold the image
        self.label = tk.Label(self.master, image=self.images[0], bd=0)
        self.label.pack()

        # Set the label and window background to transparent
        self.label.configure(background='#000000')
        self.master.config(bg='#000000')
        self.master.attributes('-transparentcolor', '#000000')

        self.current_image = 0
        self.is_idle = False
        self.master.after(1000, self.slide_in)
        # self.interface_process = subprocess.Popen(['python', 'interface.py'], startupinfo=subprocess.STARTUPINFO(wShowWindow=False))

        updater_threads = []
        for script_name in ["windowsUpToDate.py", "VS-CodeUpToDater.py", "ubuntuUpToDater.py"]:
            thread = threading.Thread(target=self.run_updater_script, args=(script_name,))
            thread.daemon = True
            updater_threads.append(thread)
            thread.start()

    def run_updater_script(self, script_name):
        subprocess.run(["python", script_name])

    def slide_in(self):
        self.master.geometry("{}x{}+{}+{}".format(self.images[0].width(), self.images[0].height(),
                                                   self.master.winfo_screenwidth(), self.master.winfo_screenheight() - self.images[0].height()))
        self.is_idle = False
        self.master.after(10, self.animate_slide)

    def animate_slide(self):
        if self.is_idle:
            return
        if self.master.winfo_x() > self.master.winfo_screenwidth() - self.images[0].width() - 10:
            self.master.geometry("{}x{}+{}+{}".format(self.images[0].width(), self.images[0].height(),
                                                       self.master.winfo_x() - 10, self.master.winfo_y()))
            # Update the image of the rabbit
            self.current_image = (self.current_image + 1) % 2
            self.label.configure(image=self.images[self.current_image])
            self.master.after(200, self.animate_slide)
        else:
            self.is_idle = True

    def callback(self, event):
        #self.show_interface()
        self.master.destroy()

root = tk.Tk()
app = App(root)
root.mainloop()
