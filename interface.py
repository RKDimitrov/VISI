import tkinter as tk
from tkinter import ttk


class MyGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x600')
        self.master.title('My Awesome GUI')
        self.create_widgets()

    def create_widgets(self):
        # Create left frame with scrollbar
        self.left_frame = tk.Frame(self.master, bg='#1B1B1B', activebackground='#1B1B1B', padx=10, pady=10)
        self.left_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        self.scrollbar = tk.Scrollbar(self.left_frame)
        self.scrollbar.pack(side='right', fill='y')
        self.menu = ttk.Treeview(self.left_frame, yscrollcommand=self.scrollbar.set, style='Custom.Treeview')
        self.menu.pack(side='left', fill='both', expand=True)
        self.scrollbar.config(command=self.menu.yview)

        # Add menu options
        self.menu.insert("", "end", "item1", text="Option 1")
        self.menu.insert("", "end", "item2", text="Option 2")
        self.menu.insert("", "end", "item3", text="Option 3")
        self.menu.insert("", "end", "item4", text="Option 4")
        self.menu.insert("", "end", "item5", text="Option 5")
        self.menu.insert("", "end", "item6", text="Option 6")
        self.menu.insert("", "end", "item7", text="Option 7")
        self.menu.insert("", "end", "item8", text="Option 8")
        self.menu.insert("", "end", "item9", text="Option 9")
        self.menu.insert("", "end", "item10", text="Option 10")
        self.menu.insert("", "end", "item11", text="Option 11")
        self.menu.insert("", "end", "item12", text="Option 12")
        self.menu.insert("", "end", "item13", text="Option 13")
        

        # Create right content box
        self.content_box = tk.Frame(self.master, bg='#ECECEC', padx=20, pady=20)
        self.content_box.pack(side='right', fill='both', expand=True)

        # Add widgets to content box
        self.title_label = tk.Label(self.content_box, text='Welcome to my GUI', font=('Segoe UI', 20, 'bold'), bg='#ECECEC', fg='#1B1B1B')
        self.title_label.pack(padx=10, pady=10)
        self.subtitle_label = tk.Label(self.content_box, text='Select an option from the menu on the left to get started.', font=('Segoe UI', 14), bg='#ECECEC', fg='#1B1B1B')
        self.subtitle_label.pack(padx=10, pady=10)

        # Define custom style for Treeview
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Custom.Treeview', background='#1B1B1B', fieldbackground='#1B1B1B', foreground='#ECECEC', rowheight=40, font=('Segoe UI', 14))
        style.map('Custom.Treeview', background=[('selected', '#0078D7')], foreground=[('selected', '#ECECEC')])


if __name__ == '__main__':
    root = tk.Tk()
    app = MyGUI(root)
    root.mainloop()
