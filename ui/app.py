import customtkinter as ctk
from ui.components.sidebar import Sidebar

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class MainUi(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("수리 AI")
        self.geometry("1200x800")

        # 행
        self.grid_rowconfigure(0, weight=1)

        # 열 비율 (2 : 8)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=8)

        # Sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        # Main
        self.main = ctk.CTkFrame(self)
        self.main.grid(row=0, column=1, sticky="nsew")