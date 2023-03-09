import customtkinter
import tkinter as tk
from tkinter import ttk
import updater

delition = 0
AppsToUpdates = updater.AppsToUpdates
forUpdate = {
    "Windows 10 Update": "{}".format(AppsToUpdates["Windows 10"]),
    "VS Code Update": "{}".format(AppsToUpdates["VS-Code"]),
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
            self.left_frame = customtkinter.CTkFrame(self.master)
            self.left_frame.pack(side='left', fill='both', expand=False, padx=10, pady=10)
            self.scrollbar = customtkinter.CTkScrollbar(self.left_frame)
            self.scrollbar.pack(side='right', fill='y')
            self.menu.pack(side='left', fill='both', expand=False)
            self.scrollbar.configure(command=self.menu.yview)

            self.menu.heading('#0', text='MENU', anchor='center')    

            #creating content box
            self.content_box = customtkinter.CTkFrame(self.master)
            self.content_box.pack(padx=20, pady=20, fill='both', expand=True)
            

            #mapping dictionary to treeview
            for key, value in forUpdate.items():
                self.menu.insert('', 'end', text=key, values=value)
                
            
            #selected option to content box
            self.menu.bind('<<TreeviewSelect>>', self.update_content)


            # Add widgets to content box
            self.title_label = customtkinter.CTkLabel(self.content_box, text='Welcome to my GUI', font=('Segoe UI', 20, 'bold'), anchor='center')
            self.title_label.pack(padx=10, pady=10)
            self.subtitle_label = customtkinter.CTkLabel(self.content_box, text='Select an option from the menu on the left to get started.', font=('Segoe UI', 14), wraplength=500, anchor='center')
            self.subtitle_label.pack(padx=10, pady=10)
            
            # Define custom style for Treeview
            style = ttk.Style()
            style.theme_use('clam')
            style.configure('Custom.Treeview', background='#5c5c5c', fieldbackground='#8a8a8a', foreground='#ffffff', rowheight=70, font=('Segoe UI', 14))
            style.map('Custom.Treeview', background=[('selected', '#7d7d7d')], foreground=[('selected', '#383838')], font=[('selected', ('Segoe UI', 14, 'bold'))])

        def update_content(self, event):
            
            
            # Get selected item
            selected_item = self.menu.selection()
            # Get selected item text
            selected_text = self.menu.item(selected_item, 'text')
            # Get selected item value
            selected_value = self.menu.item(selected_item, 'values')
            # Get selected item index
            selected_index = int(selected_item[0][1:])
            # Update content box
            self.title_label.configure(text=selected_text)
            self.subtitle_label.configure(text=selected_value)
            #create button to website
            if hasattr(self, 'button'):
                self.button.pack_forget()
            self.button = tk.Button(self.content_box, text='Go to website', command=lambda: self.open_website(updater.url_values[str(selected_index)]))
            self.button.pack(padx=10, pady=10)
            
            
        def open_website(self, url):
            import webbrowser
            webbrowser.open(url)

    if __name__ == '__main__':
        customtkinter.set_appearance_mode("dark")
        root = customtkinter.CTk()
        app = MyGUI(root)
        root.mainloop()

overAllFunction()