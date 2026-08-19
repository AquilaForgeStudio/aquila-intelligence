import customtkinter as ctk
from ui.components.sidebar import Sidebar
from ui.splash import SplashFrame

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class MainUi(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("수리 AI")
        self.geometry("1200x800")

        # 전체 레이아웃
        self.grid_rowconfigure(0, weight=1)

        # Sidebar는 폭을 직접 관리하므로 weight=0
        self.grid_columnconfigure(0, weight=0)

        # Main은 남은 공간을 모두 차지
        self.grid_columnconfigure(1, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        # Main
        self.main = ctk.CTkFrame(
            self,
            fg_color="#1b1b1b"
        )

        self.main.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.splash = SplashFrame(self)
        self.splash.place(
    relx=0,
    rely=0,
    relwidth=1,
    relheight=1
)
        self.splash.lift()
