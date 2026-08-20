import customtkinter as ctk
from PIL import Image
from typing import Callable
from config.reader import UI_CONFIG
from utils import color , easing


class SidebarButton(ctk.CTkFrame):
    def __init__(self, master, icon: str, text: str, command: Callable, expanded : bool = False):
        """
        Sidebar의 버튼을 생성합니다.
        """
        super().__init__(
            master,
            height=UI_CONFIG["Sidebar"]["Button"]["Height"],
            corner_radius=UI_CONFIG["Sidebar"]["Button"]["CornerRadius"]
        )

        self.pack_propagate(False)

        self.icon = icon
        self.text = text
        self.command = command
        self.expanded = expanded
        self.normal_color = UI_CONFIG["Sidebar"]["Button"]["NormalColor"]
        self.hover_color = UI_CONFIG["Sidebar"]["Button"]["HoverColor"]
        self.current_color = self.hover_color

        self.animation_step = 0
        self.position_step = 0
        self.position_animation_id = None

        self.animation_id = None

        self.is_hovered = False

        self.after(20, self.check_mouse_position)

        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        # 아이콘 생성
        self.icon_image = ctk.CTkImage(
            light_image=Image.open(self.icon),
            dark_image=Image.open(self.icon),
            size=tuple(UI_CONFIG["Sidebar"]["Icon"]["Size"])
        )

        self.icon_label = ctk.CTkLabel(
            self,
            image=self.icon_image,
            text="",
            width=UI_CONFIG["Sidebar"]["Icon"]["AreaWidth"],
            height=UI_CONFIG["Sidebar"]["Icon"]["AreaHeight"]
        )

        self.icon_label.pack(
            side="left",
            padx=(8, 4)
        )
        # 텍스트 생성
        self.text_label = ctk.CTkLabel(
            self,
            text=self.text,
            anchor="w"
        )

        if self.expanded :
            self.text_label.pack(
                side="left",
                fill="x",
                expand=True
            )

    def bind_events(self):
        widgets = [self, self.icon_label, self.text_label]

        for widget in widgets:
            widget.bind("<Enter>", self.on_enter)
            widget.bind("<Leave>", self.on_leave)
            widget.bind("<Button-1>", self.on_click)

    def on_enter(self, event):
        pass

    def hover_animation(self):
        if self.animation_id is not None:
            self.after_cancel(self.animation_id)
        if self.animation_step >= 10 :
            return
        self.configure(fg_color=color.rgb_to_hex(
            color.interpolate_color(
                color.hex_to_rgb(self.normal_color),
                color.hex_to_rgb(self.hover_color),
                self.animation_step / 10
            )
        ))
        self.animation_step += 1
        self.animation_id = self.after(10, self.hover_animation)

    def on_leave(self, event):
        self.after(1,self.check_mouse_position)

    def leave_animation(self):
        if self.animation_id is not None:
            self.after_cancel(self.animation_id)
        if self.animation_step >= 10 :
            return
        self.configure(fg_color=color.rgb_to_hex(
            color.interpolate_color(
                color.hex_to_rgb(self.hover_color),
                color.hex_to_rgb(self.normal_color),
                self.animation_step / 10
            )
        ))
        self.animation_step += 1
        self.animation_id = self.after(10, self.leave_animation)

    def on_click(self, event):
        if self.command:
            self.command()

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

    def config(self, text=None, icon=None, command=None):
        if text is not None:
            self.text = text
        if icon is not None:
            self.icon = icon
        if command is not None:
            self.command = command

        self.icon_image = ctk.CTkImage(
                    light_image=Image.open(self.icon),
                    dark_image=Image.open(self.icon),
                    size=tuple(UI_CONFIG["Sidebar"]["Icon"]["Size"])
                )
        
        self.icon_lable.configure(image=self.icon_image)
        self.text_label.configure(text=self.text)
        self.command = command

    def expand(self):
        duration = 30

        if self.position_animation_id is not None:
            self.after_cancel(self.position_animation_id)

        if self.position_step >= duration:
            self.position_step = duration
            self.position_animation_id = None
            return

        # 진행도
        t = self.position_step / duration

        # easing
        eased = easing.ease_out_cubic(t)

        # SidebarButton 크기/위치 애니메이션
        # ...
        width = 70 + (220 - 70) * eased

        self.configure(
            width=round(width)
        )

        
        # 중간에 텍스트 등장
        if self.position_step >= 15:
            self.text_label.pack(
                side="left",
                fill="x",
                expand=True
                        )

        self.position_step += 1

        self.position_animation_id = self.after(
            16,
            self.expand
        )

    def collapse(self) :
        duration = 30

        if self.position_animation_id is not None:
            self.after_cancel(self.position_animation_id)

        if self.position_step >= duration:
            self.position_step = duration
            self.position_animation_id = None
            return

        # 진행도
        t = self.position_step / duration

        # easing
        eased = easing.ease_in_cubic(t)

        # SidebarButton 크기/위치 애니메이션
        # ...
        width = 220 - (220 - 70) * eased

        self.configure(
            width=round(width)
        )

        
        # 중간에 텍스트 등장
        if self.position_step >= 15:
            self.text_label.pack_forget()

        self.position_step += 1

        self.position_animation_id = self.after(
            16,
            self.collapse
        )