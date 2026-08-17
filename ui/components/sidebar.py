import customtkinter as ctk
from .sidebar_button import SidebarButton


class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=220)

        self.pack_propagate(False)

        Dashboard = SidebarButton(
            self,
            icon="assets/icons/layout-dashboard.png",
            text="Dashboard",
            command=self.test
        )

        Dashboard.pack(
            fill="x",
            padx=8,
            pady=4
        )
        Chat = SidebarButton(
            self,
            icon="assets/icons/message-circle.png",
            text="Chat",
            command=self.test
        )

        Chat.pack(
            fill="x",
            padx=8,
            pady=4
        )
        History = SidebarButton(
            self,
            icon="assets/icons/rotate-ccw-clock.png",
            text="History",
            command=self.test
        )

        History.pack(
            fill="x",
            padx=8,
            pady=4
        )
        Schedule = SidebarButton(
            self,
            icon="assets/icons/calendar-days.png",
            text="Schedule",
            command=self.test
        )

        Schedule.pack(
            fill="x",
            padx=8,
            pady=4
        )

        Memo = SidebarButton(
            self,
            icon="assets/icons/notebook-pen.png",
            text="Memo",
            command=self.test
        )

        Memo.pack(
            fill="x",
            padx=8,
            pady=4
        )

        Settings = SidebarButton(
            self,
            icon="assets/icons/settings.png",
            text="Settings",
            command=self.test
        )

        Settings.pack(
            fill="x",
            padx=8,
            pady=4
        )

        Logout = SidebarButton(
            self,
            icon="assets/icons/log-out.png",
            text="Logout",
            command=self.test
        )
        Logout.text_label.configure(text_color="red")
        Logout.pack(
            fill="x",
            padx=8,
            pady=4
        )

    def test(self):
        print("클릭!")