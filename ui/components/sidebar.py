import customtkinter as ctk
from .sidebar_button import SidebarButton
from utils import easing


class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=70)
        self.pack_propagate(False)

        self.btnlist = []

        self.animation_step = 0
        self.is_hovered = False

        self.animation_id = None

        self.create_buttons()
        self.after(20, self.check_mouse_position)

        

    def create_buttons(self):
        self.Dashboard = SidebarButton(
                    self,
                    icon="assets/icons/layout-dashboard.png",
                    text="Dashboard",
                    command=self.test
                )

        self.btnlist.append(self.Dashboard)
        
        self.Dashboard.pack(
                    fill="x",
                    padx=8,
                    pady=4
                )
        self.Chat = SidebarButton(
                    self,
                    icon="assets/icons/message-circle.png",
                    text="Chat",
                    command=self.test
                )
        self.btnlist.append(self.Chat)
        self.Chat.pack(
                    fill="x",
                    padx=8,
                    pady=4
                )
                
        self.History = SidebarButton(
                    self,
                    icon="assets/icons/rotate-ccw-clock.png",
                    text="History",
                    command=self.test
                )
        self.btnlist.append(self.History)
        self.History.pack(
                    fill="x",
                    padx=8,
                    pady=4
                )
        self.Schedule = SidebarButton(
                    self,
                    icon="assets/icons/calendar-days.png",
                    text="Schedule",
                    command=self.test
                )
        self.btnlist.append(self.Schedule)
        self.Schedule.pack(
                    fill="x",
                    padx=8,
                    pady=4
                )
        
        self.Memo = SidebarButton(
                    self,
                    icon="assets/icons/notebook-pen.png",
                    text="Memo",
                    command=self.test
                )
        self.btnlist.append(self.Memo)
        self.Memo.pack(
                    fill="x",
                    padx=8,
                    pady=4
                )
        
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
        
        self.Logout = SidebarButton(
                    self,
                    icon="assets/icons/log-out.png",
                    text="Logout",
                    command=self.test
                )
        self.btnlist.append(self.Logout)
        self.Logout.text_label.configure(text_color="red")
        self.Logout.pack(
                    fill="x",
                    padx=8,
                    pady=4
                )
    def test(self):
        print("클릭!")

    def check_mouse_position(self):
        x = self.winfo_pointerx()
        y = self.winfo_pointery()

        left = self.winfo_rootx()
        top = self.winfo_rooty()
        right = left + self.winfo_width()
        bottom = top + self.winfo_height()

        inside = left <= x <= right and top <= y <= bottom


        if inside and not self.is_hovered:
            self.is_hovered = True
            self.animation_step = 0
            self.hover_animation()

        elif not inside and self.is_hovered:
            self.is_hovered = False
            self.animation_step = 0
            self.leave_animation()

        self.after(20, self.check_mouse_position)

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

        if self.animation_step == 0:
            for btn in self.btnlist:
                btn.collapse()

        self.animation_step += 1

        self.animation_id = self.after(
            16,
            self.leave_animation
        )