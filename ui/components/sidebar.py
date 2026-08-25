import customtkinter as ctk
from .sidebar_button import SidebarButton
from utils import easing


class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=70)

        self.pack_propagate(False)

        # 버튼 목록
        self.btnlist = []

        # 애니메이션
        self.animation_step = 0
        self.is_hovered = False
        self.animation_id = None

        self.create_buttons()

        self.after(20, self.check_mouse_position)

    # --------------------------------------------------
    # Buttons
    # --------------------------------------------------

    def create_buttons(self):

        menus = [
            ("Dashboard", "assets/icons/layout-dashboard.png"),
            ("Chat", "assets/icons/message-circle.png"),
            ("History", "assets/icons/rotate-ccw-clock.png"),
            ("Schedule", "assets/icons/calendar-days.png"),
            ("Memo", "assets/icons/notebook-pen.png"),
        ]

        for text, icon in menus:
            button = SidebarButton(
                self,
                icon=icon,
                text=text,
                command=self.test
            )

            self.btnlist.append(button)

            button.pack(
                fill="x",
                padx=8,
                pady=4
            )

        # Settings
        self.Settings = SidebarButton(
            self,
            icon="assets/icons/settings.png",
            text="Settings",
            command=self.test
        )

        self.btnlist.append(self.Settings)

        self.Settings.pack(
            fill="x",
            padx=8,
            pady=4
        )

        # Logout
        self.Logout = SidebarButton(
            self,
            icon="assets/icons/log-out.png",
            text="Logout",
            command=self.test
        )

        self.btnlist.append(self.Logout)

        self.Logout.text_label.configure(
            text_color="red"
        )

        self.Logout.pack(
            fill="x",
            padx=8,
            pady=4
        )

    # --------------------------------------------------
    # Test
    # --------------------------------------------------

    def test(self):
        print("클릭!")

    # --------------------------------------------------
    # Mouse detection
    # --------------------------------------------------

    def check_mouse_position(self):

        x = self.winfo_pointerx()
        y = self.winfo_pointery()

        left = self.winfo_rootx()
        top = self.winfo_rooty()

        # Sidebar가 접혀 있어도 220px 영역까지 hover
        hover_width = 220

        right = left + hover_width
        bottom = top + self.winfo_height()

        inside = (
            left <= x <= right
            and top <= y <= bottom
        )

        if inside and not self.is_hovered:

            self.is_hovered = True
            self.animation_step = 0

            self.hover_animation()

        elif not inside and self.is_hovered:

            self.is_hovered = False
            self.animation_step = 0

            self.leave_animation()

        self.after(
            20,
            self.check_mouse_position
        )

    # --------------------------------------------------
    # Hover animation
    # --------------------------------------------------

    def hover_animation(self):

        duration = 30

        if self.animation_step >= duration:

            self.configure(width=220)

            self.animation_id = None
            return

        t = self.animation_step / duration

        eased = easing.ease_out_cubic(t)

        width = 70 + (220 - 70) * eased

        self.configure(
            width=round(width)
        )

        for btn in self.btnlist:
            btn.expand()

        self.animation_step += 1

        self.animation_id = self.after(
            16,
            self.hover_animation
        )

    # --------------------------------------------------
    # Leave animation
    # --------------------------------------------------

    def leave_animation(self):

        duration = 30

        if self.animation_step >= duration:

            self.configure(width=70)

            self.animation_id = None
            return

        t = self.animation_step / duration

        eased = easing.ease_out_cubic(t)

        width = 220 - (220 - 70) * eased

        self.configure(
            width=round(width)
        )

        # 버튼 collapse는 애니메이션 시작 시 한 번만
        if self.animation_step == 0:

            for btn in self.btnlist:
                btn.collapse()

        self.animation_step += 1

        self.animation_id = self.after(
            16,
            self.leave_animation
        )