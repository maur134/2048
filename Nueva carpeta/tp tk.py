from tkinter import *
import tkinter as tk
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class Menu_principal:
    def __init__(self, menu_prin):
        self.menu_prin = menu_prin
        menu_prin.update_idletasks()
        self.x = menu_prin.winfo_screenwidth()
        self.y = menu_prin.winfo_screenheight()
        self.menu_prin.geometry(f"{self.x}x{self.y}+0+0")
        self.menu_prin.title("Inicio")
        self.main_menu()
    
    def main_menu (self):
        frame_jueguito = ctk.CTkFrame(master = self.menu_prin, fg_color= "red", width= 500)
        frame_jueguito.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

if __name__ == "__main__":
    """root = ctk.CTk()
    Login(root)
    root.mainloop()"""
    menu_prin = ctk.CTk()
    Menu_principal(menu_prin)
    menu_prin.mainloop()