import customtkinter as ctk
from sidebar_buttons import SidebarButton
class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=0)  # 로고
        self.grid_rowconfigure(1, weight=0)  # 메뉴 버튼
        self.grid_rowconfigure(2, weight=1)  # 위젯(스크롤)
        self.grid_rowconfigure(3, weight=0)  # 하단 버튼

        button1 = SidebarButton()

