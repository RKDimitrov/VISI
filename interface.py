import tkinter as tk
from tkinter import ttk
import updater

delition = 0
AppsToUpdates = updater.AppsToUpdates
forUpdate = {
    "Windows 10 Update": "{}".format(AppsToUpdates["Windows 10"]),
    "linux": "mqu2",
    "mac": "mqu3",
    "android": "mqu4",
}
def overAllFunction():
    class MyGUI:
        def __init__(self, master):
            self.master = master
            self.master.geometry('800x600')
            self.master.title('VISI Security')
            self.create_widgets()

        def create_widgets(self):
            # Create left frame with scrollbar
            self.left_frame = tk.Frame(self.master, bg='#1B1B1B')
            self.left_frame.pack(side='left', fill='both', expand=False, padx=10, pady=10)
            self.scrollbar = tk.Scrollbar(self.left_frame)
            self.scrollbar.pack(side='right', fill='y')
            self.menu = ttk.Treeview(self.left_frame, yscrollcommand=self.scrollbar.set, style='Custom.Treeview')
            self.menu.pack(side='left', fill='both', expand=False)
            self.scrollbar.config(command=self.menu.yview)
            
            self.menu.heading('#0', text='', anchor='w')    

            #creating content box
            self.content_box = tk.Frame(self.master, bg='#ECECEC', padx=20, pady=20)
            self.content_box.pack(side='right', fill='both', expand=True)
            

            #mapping dictionary to treeview
            for key, value in forUpdate.items():
                self.menu.insert('', 'end', text=key, values=value)
                
            
            #selected option to content box
            self.menu.bind('<<TreeviewSelect>>', self.update_content)

            # Create right content box
            self.content_box = tk.Frame(self.master, bg='#ECECEC', padx=20, pady=20)
            self.content_box.pack(side='right', fill='both', expand=True)

            # Add widgets to content box
            self.title_label = tk.Label(self.content_box, text='Welcome to my GUI', font=('Segoe UI', 20, 'bold'), bg='#ECECEC', fg='#1B1B1B', anchor='center')
            self.title_label.pack(padx=10, pady=10)
            self.subtitle_label = tk.Label(self.content_box, text='Select an option from the menu on the left to get started.', font=('Segoe UI', 14), bg='#ECECEC', fg='#1B1B1B', wraplength=500, anchor='center')
            self.subtitle_label.pack(padx=10, pady=10)
            
            # Define custom style for Treeview
            style = ttk.Style()
            style.theme_use('clam')
            style.configure('Custom.Treeview', background='#1B1B1B', fieldbackground='#1B1B1B', foreground='#ECECEC', rowheight=70, font=('Segoe UI', 14))
            style.map('Custom.Treeview', background=[('selected', '#0078D7')], foreground=[('selected', '#ECECEC')])

        def update_content(self, event):
            
            # Get selected item
            selected_item = self.menu.selection()
            # Get selected item text
            selected_text = self.menu.item(selected_item, 'text')
            # Get selected item value
            selected_value = self.menu.item(selected_item, 'values')
            # Update content box
            self.title_label.config(text=selected_text)
            self.subtitle_label.config(text=selected_value)
            #create button to website
            self.button = tk.Button(self.content_box, text='Go to website', command=lambda: self.open_website(updater.windows_update()[1]))
            self.button.pack(padx=10, pady=10)
            #delete button
            if delition > 0:
                self.button.destroy()
            delition+=1
            print(delition)
            
    

            
        def open_website(self, url):
            import webbrowser
            webbrowser.open(url)

    if __name__ == '__main__':
        root = tk.Tk()
        app = MyGUI(root)
        root.mainloop()

overAllFunction()