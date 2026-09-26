import customtkinter as ctk
from utils import reader, etc
from ui import widget_manager

class DashboardPage(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(
            master,
            fg_color="#1b1b1b"
        )
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.create_header()
        widget_manager.WidgetManager(self).scan_widgets()

    def create_header(self):
        self.greeting = ctk.CTkLabel(
            self,
            text=f"{reader.USERDATA['userNickName']}님, {etc.CurrentTimeReturnSay()}",
            font=("Pretendard", 28, "bold"),
            anchor="w"
        )

        self.greeting.grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10), sticky="w"
        )

    