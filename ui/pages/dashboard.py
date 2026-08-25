import customtkinter as ctk
from data.reader import USERDATA

class DashboardPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            fg_color="#1b1b1b"
        )

        self.create_header()

    def create_header(self):
        self.greeting = ctk.CTkLabel(
            self,
            text=f"안녕하세요,  {USERDATA['userNickName']}님 좋은 오후입니다!",
            font=("Pretendard", 28, "bold"),
            anchor="w"
        )

        self.greeting.pack(
            padx=30,
            pady=(30, 10),
            anchor="w"
        )