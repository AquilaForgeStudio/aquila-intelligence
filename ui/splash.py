import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk


class SplashFrame(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="#1b1b1b"
        )

        self.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        # =========================
        # Canvas
        # =========================

        self.canvas = tk.Canvas(
            self,
            bg="#1b1b1b",
            highlightthickness=0
        )

        self.canvas.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        # =========================
        # Logo
        # =========================

        logo = Image.open(
            "assets/BI/Aquila-Logo.png"
        )

        logo = logo.resize(
            (300, 300),
            Image.Resampling.LANCZOS
        )

        self.logo_image = ImageTk.PhotoImage(logo)

        self.logo = self.canvas.create_image(
            0,
            0,
            image=self.logo_image,
            anchor="center"
        )

        # =========================
        # Text
        # =========================

        self.text = self.canvas.create_text(
            -10000,
            -10000,
            text="Aquila AI",
            fill="#E0E0E0",
            font=("Russo One", 80),
            anchor="w"
        )

        # =========================
        # Animation
        # =========================

        self.animation_running = False

        self.canvas.bind(
            "<Configure>",
            self.on_canvas_resize
        )

        # Canvas가 실제 크기를 잡은 후 시작
        self.after(
            300,
            self.start_animation
        )

    # ==================================================
    # Canvas Resize
    # ==================================================

    def on_canvas_resize(self, event):
        # 애니메이션 중에는 Resize 이벤트가
        # 현재 애니메이션 위치를 덮어쓰지 않도록 한다.
        if self.animation_running:
            return

        self.canvas.coords(
            self.logo,
            event.width / 2,
            event.height / 2
        )

    # ==================================================
    # Start Animation
    # ==================================================

    def start_animation(self):

        if self.animation_running:
            return

        self.animation_running = True

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        center_x = width / 2
        center_y = height / 2

        # -------------------------
        # Layout
        # -------------------------

        logo_width = 300
        gap = 30

        # -------------------------
        # Text Width
        # -------------------------

        bbox = self.canvas.bbox(
            self.text
        )

        if bbox:
            text_width = bbox[2] - bbox[0]
        else:
            text_width = 0

        # -------------------------
        # 전체 그룹 크기
        # -------------------------

        total_width = (
            logo_width
            + gap
            + text_width
        )

        # -------------------------
        # 최종 위치
        # -------------------------

        target_logo_x = (
            center_x
            - total_width / 2
            + logo_width / 2
        )

        target_text_x = (
            center_x
            - total_width / 2
            + logo_width
            + gap
        )

        # -------------------------
        # 시작 위치
        # -------------------------

        # 독수리는 처음 중앙
        start_logo_x = center_x

        # 텍스트는 화면 오른쪽 바깥
        start_text_x = (
            width
            + text_width
        )

        # -------------------------
        # 초기 위치
        # -------------------------

        self.canvas.coords(
            self.logo,
            start_logo_x,
            center_y
        )

        self.canvas.coords(
            self.text,
            start_text_x,
            center_y
        )

        # -------------------------
        # 애니메이션
        # -------------------------

        self.animate_position(
            start_logo_x,
            target_logo_x,
            start_text_x,
            target_text_x,
            center_y
        )

    # ==================================================
    # Easing
    # ==================================================

    def ease_out_cubic(self, t):
        return 1 - (1 - t) ** 3

    # ==================================================
    # Position Animation
    # ==================================================

    def animate_position(
        self,
        start_logo_x,
        target_logo_x,
        start_text_x,
        target_text_x,
        y,
        step=0
    ):

        duration = 40

        # 0 ~ 1
        t = step / duration

        if t > 1:
            t = 1

        # Easing
        eased = self.ease_out_cubic(t)

        # -------------------------
        # Logo Position
        # -------------------------

        logo_x = (
            start_logo_x
            + (
                target_logo_x
                - start_logo_x
            ) * eased
        )

        # -------------------------
        # Text Position
        # -------------------------

        text_x = (
            start_text_x
            + (
                target_text_x
                - start_text_x
            ) * eased
        )

        # -------------------------
        # Canvas Update
        # -------------------------

        self.canvas.coords(
            self.logo,
            logo_x,
            y
        )

        self.canvas.coords(
            self.text,
            text_x,
            y
        )

        # -------------------------
        # 다음 프레임
        # -------------------------

        if step < duration:

            self.after(
                16,
                self.animate_position,
                start_logo_x,
                target_logo_x,
                start_text_x,
                target_text_x,
                y,
                step + 1
            )

        else:
            self.animation_finished()

    # ==================================================
    # Animation Finished
    # ==================================================

    def animation_finished(self):

        # 애니메이션 종료
        self.animation_running = False

        # 현재는 0.8초 후 종료
        # 나중에 Firebase 로딩이 들어오면
        # 이 부분을 외부에서 close() 호출하는 구조로 변경
        self.after(
            800,
            self.close
        )

    # ==================================================
    # Close
    # ==================================================

    def close(self):

        if self.winfo_exists():
            self.destroy()