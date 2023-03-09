import tkinter as tk
import os

root = tk.Tk()
root.overrideredirect(True)  # Remove the title bar and window decorations
root.geometry("300x300+0+0")  # Set the size and position of the window
root.lift()  # Move the window to the top of the stacking order
root.wm_attributes("-topmost", True)  # Keep the window on top of other windows

# Load an image and display it in a label
image = tk.PhotoImage(file="rabbit.png")
label = tk.Label(root, image=image, bd=0)
label.pack()

# Open the URL when the user clicks on the image
def on_click(event):
    os.system("start " + "chrome.exe")
    root.destroy()

label.bind("<Button-1>", on_click)

x = root.winfo_screenwidth() - root.winfo_reqwidth()  # Starting x position
y = root.winfo_screenheight() - root.winfo_reqheight()  # Starting y position
root.geometry("+{}+{}".format(x, y))  # Set the new position of the window
for i in range(x, root.winfo_screenwidth() - root.winfo_reqwidth(), -10):
    root.geometry("+{}+{}".format(i, y))
    root.update()
    root.after(10)

root.mainloop()
