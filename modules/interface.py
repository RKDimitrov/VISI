import customtkinter as CTk
import updater
import app_finder

import windowsUpToDate
import ubuntuUpToDater
import VSCodeUpToDater


AppsToUpdates = updater.AppsToUpdates

forUpdate = {
    "Windows 10": "{}".format(AppsToUpdates["Windows 10"]),
    "Ubuntu": "UBUNTU",
    "MacOS": "MAC",
    "Code": "{}".format(AppsToUpdates["VS-Code"]),
}


def overAllFunction():
    class MyGUI:
        def __init__(self, master):
            self.master = master
            self.master.geometry('1280x720')
            self.master.iconbitmap('../VISI/img/icon.ico')
            self.master.title('VISI Security')

            # Creating a menu with scrollbar
            self.menu = CTk.CTkFrame(self.master)
            self.menu.pack(side='left', fill='both', expand=False, padx=20, pady=20)

            self.menu_label = CTk.CTkLabel(self.menu, text='MENU', font=('Segoe UI', 20, 'bold'), anchor='center')
            self.menu_label.pack(padx=10, pady=10)

            self.menu_options = CTk.CTkScrollableFrame(self.menu, corner_radius=0)
            self.menu_options.pack(side='left', fill='both', expand=False)

            if app_finder.Os_type() == 1:
                    option = CTk.CTkButton(master=self.menu_options, text=list(forUpdate.keys())[0], font=('Segoe UI', 14))
                    option.configure(fg_color="transparent", anchor='center')
                    option.configure(width=int(self.menu_options.cget('width'))-10)
                    option.configure(command=lambda key=list(forUpdate.keys())[0], value=list(forUpdate.values())[0]: self.update_content(key, value))
                    option.pack(padx=5, pady=3)
            elif app_finder.Os_type() == 2:
                    option = CTk.CTkButton(master=self.menu_options, text=list(forUpdate.keys())[1], font=('Segoe UI', 14))
                    option.configure(fg_color="transparent", anchor='center')
                    option.configure(width=int(self.menu_options.cget('width'))-10)
                    option.configure(command=lambda key=list(forUpdate.keys())[1], value=list(forUpdate.values())[1]: self.update_content(key, value))
                    option.pack(padx=5, pady=3)
            elif app_finder.Os_type() == 3:
                    option = CTk.CTkButton(master=self.menu_options, text=list(forUpdate.keys())[2], font=('Segoe UI', 14))
                    option.configure(fg_color="transparent", anchor='center')
                    option.configure(width=int(self.menu_options.cget('width'))-10)
                    option.configure(command=lambda key=list(forUpdate.keys())[2], value=list(forUpdate.values())[2]: self.update_content(key, value))
                    option.pack(padx=5, pady=3) 

            for key, value in list(forUpdate.items())[3:]:
                checker = 0
                if app_finder.Os_type() == 1:
                    if None != app_finder.search_file_on_windows(str(key)+".exe"):
                        checker = 1

                elif app_finder.Os_type() == 2:
                    if None != app_finder.search_file_on_ubuntu(str(key)+".out"):
                        checker = 1

                elif app_finder.Os_type() == 3:
                    if None != app_finder.search_file_on_mac(str(key)+".out"):
                        checker = 1
                if checker == 1:
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

            self.text1 = CTk.CTkLabel(self.content_box, text=windowsUpToDate.check_windows_update(), font=('Segoe UI', 20, 'bold'), anchor='center')
            self.text1.pack(padx=10, pady=10)

            self.text2 = CTk.CTkLabel(self.content_box, text=ubuntuUpToDater.get_latest_ubuntu_version(), font=('Segoe UI', 20, 'bold'), anchor='center')
            self.text2.pack(padx=10, pady=10)

            self.text3 = CTk.CTkLabel(self.content_box, text=VSCodeUpToDater.check_vscode_version()[0], font=('Segoe UI', 20, 'bold'), anchor='center')
            self.text3.pack(padx=10, pady=10)
           

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

