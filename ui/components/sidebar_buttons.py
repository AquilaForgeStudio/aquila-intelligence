import customtkinter as ctk

class SidebarButton(ctk.CTkFrame):
    def __init__(self, master, icon : str, text : str , command:callable):
        """
        sidebar의 버튼을 생성합니다
        """
        super().__init__(master)
