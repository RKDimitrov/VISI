import customtkinter as CTk
import updater
import app_finder


AppsToUpdates = updater.AppsToUpdates
forUpdate = {
    "Windows 10 Update": "{}".format(AppsToUpdates["Windows 10"]),
    "VS Code Update": "{}".format(AppsToUpdates["VS-Code"]),
}

def overAllFunction():
    class MyGUI:
        def __init__(self, master):
            self.master = master
            self.master.geometry('850x600')
            self.master.iconbitmap('../VISI/img/icon.ico')
            self.master.title('VISI Security')
            #self.master.widthdraw()

            # Creating a menu with scrollbar
            self.menu = CTk.CTkFrame(self.master)
            self.menu.pack(side='left', fill='both', expand=False, padx=20, pady=20)

            self.menu_label = CTk.CTkLabel(self.menu, text='MENU', font=('Segoe UI', 20, 'bold'), anchor='center')
            self.menu_label.pack(padx=10, pady=10)

            self.menu_options = CTk.CTkScrollableFrame(self.menu, corner_radius=0)
            self.menu_options.pack(side='left', fill='both', expand=False)

            for key, value in forUpdate.items():
                option = CTk.CTkButton(master=self.menu_options, text=key, font=('Segoe UI', 14))
                option.configure(fg_color="transparent", anchor='center')
                option.configure(width=int(self.menu_options.cget('width'))-10)
                option.configure(command=lambda key=key, value=value: self.update_content(key, value))
                option.pack(padx=5, pady=3)

            #creating content box
            self.content_box = CTk.CTkFrame(self.master)
            self.content_box.pack(padx=20, pady=20, fill='both', expand=True)

            # Add widgets to content box
            self.title_label = CTk.CTkLabel(self.content_box, text='Welcome to VISI', font=('Segoe UI', 20, 'bold'), anchor='center')
            self.title_label.pack(padx=10, pady=10)
            self.subtitle_label = CTk.CTkLabel(self.content_box, text='Select an option from the menu on the left to get started.', font=('Segoe UI', 14), wraplength=500, anchor='center')
            self.subtitle_label.pack(padx=10, pady=10)
           

        def update_content(self, title, text):
            self.title_label.configure(text=title)
            self.subtitle_label.configure(text=text)
            
            selected_index = list(forUpdate.keys()).index(title)
            


            if hasattr(self, 'button'):
                self.button.pack_forget()
            self.button = CTk.CTkButton(self.content_box, text='Go to website', command=lambda: self.open_website(updater.url_values[str(selected_index)]))
            self.button.pack(padx=10, pady=10)
           
           
        def open_website(self, url):
            import webbrowser
            webbrowser.open(url)

    if __name__ == '__main__':
        CTk.set_appearance_mode("dark")
        root = CTk.CTk()
        app = MyGUI(root)
        root.mainloop()

overAllFunction()

