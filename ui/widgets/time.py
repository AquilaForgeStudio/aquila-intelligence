import customtkinter as ctk
from datetime import datetime


class Time(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            fg_color="#242424",
            corner_radius=16
        )

        # =========================
        # 제목
        # =========================

        self.title_label = ctk.CTkLabel(
            self,
            text="현재 시간",
            font=("Pretendard", 16, "bold"),
            text_color="#AAAAAA"
        )

        self.title_label.pack(
            anchor="w",
            padx=20,
            pady=(18, 0)
        )

        # =========================
        # 시간
        # =========================

        self.time_label = ctk.CTkLabel(
            self,
            text="00:00:00",
            font=("Pretendard", 36, "bold"),
            text_color="#E0E0E0"
        )

        self.time_label.pack(
            pady=(8, 0)
        )

        # =========================
        # 날짜
        # =========================

        self.date_label = ctk.CTkLabel(
            self,
            text="0000년 00월 00일",
            font=("Pretendard", 15),
            text_color="#888888"
        )

        self.date_label.pack(
            pady=(0, 4)
        )

        # =========================
        # 요일
        # =========================

        self.day_label = ctk.CTkLabel(
            self,
            text="월요일",
            font=("Pretendard", 14),
            text_color="#FC4E00"
        )

        self.day_label.pack(
            pady=(0, 15)
        )

        # =========================
        # 시간 갱신
        # =========================

        self.update_time()

    # ==================================================
    # Time Update
    # ==================================================

    def update_time(self):

        now = datetime.now()

        # 시간
        self.time_label.configure(
            text=now.strftime("%H:%M:%S")
        )

        # 날짜
        self.date_label.configure(
            text=now.strftime("%Y년 %m월 %d일")
        )

        # 요일
        days = [
            "월요일",
            "화요일",
            "수요일",
            "목요일",
            "금요일",
            "토요일",
            "일요일"
        ]

        self.day_label.configure(
            text=days[now.weekday()]
        )

        # 1초 후 다시 실행
        self.after(
            1000,
            self.update_time
        )