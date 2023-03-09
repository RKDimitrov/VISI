import os
from tkinter import Tk, Canvas, Button
from PIL import ImageTk, Image

def on_click(root, app_name):
    # destroy the root window
    os.system("start " + app_name)
    root.destroy()

def overlay_image(image_path, app_name):
    # load the image to overlay
    image = Image.open(image_path)

    # create a Tkinter window to display the image
    root = Tk()
    root.overrideredirect(True)
    root.geometry("+0+0")
    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    canvas = Canvas(root, width=image.width, height=image.height, highlightthickness=0)
    canvas.pack()
    img = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor="nw", image=img)

    # create a button to close the image and bring the app to the foreground
    

    # bind the <Button-1> event to the canvas widget
    canvas.bind("<Button-1>", lambda event: on_click(root, app_name))


    # run the Tkinter main loop to display the image and button
    root.mainloop()

    button = Button(root, text="Click to Continue", bg="white", fg="black", bd=0)
    button.pack(side="right", padx=500)
    button.config(width=5, height=5)





    # bring the specified app to the foreground
    



overlay_image("rabbit.png", "chrome.exe")
