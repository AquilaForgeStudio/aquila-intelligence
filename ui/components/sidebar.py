import customtkinter as ctk
from .sidebar_button import SidebarButton


class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=220)

        self.pack_propagate(False)

        button = SidebarButton(
            self,
            icon="assets/icons/Planit-Logo.png",
            text="Dashboard",
            command=self.test
        )

        button.pack(
            fill="x",
            padx=8,
            pady=8
        )

    def test(self):
        print("클릭!")