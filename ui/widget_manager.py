import os
import importlib
import inspect
import customtkinter as ctk

from utils import resource, reader


class WidgetManager:
    def __init__(self, master):
        self.master = master
        self.widgets = {}

    # ==================================================
    # Widget Scan
    # ==================================================

    def scan_widgets(self):
        widget_dir = resource.resource_path(
            "ui",
            "widgets"
        )

        if not os.path.isdir(widget_dir):
            raise FileNotFoundError(
                f"Widget directory not found: {widget_dir}"
            )

        for filename in os.listdir(widget_dir):

            # Python 파일만
            if not filename.endswith(".py"):
                continue

            # __init__.py 등 제외
            if filename.startswith("__"):
                continue

            name = filename[:-3]

            print("Widget 발견:", filename)

            # ------------------------------------------
            # Module Import
            # ------------------------------------------

            module = importlib.import_module(
                f"ui.widgets.{name}"
            )

            # ------------------------------------------
            # Class Scan
            # ------------------------------------------

            for class_name, widget_class in inspect.getmembers(
                module,
                inspect.isclass
            ):

                # 현재 모듈에서 직접 정의된 클래스인지 확인
                if widget_class.__module__ != module.__name__:
                    continue

                # CTkFrame인지 확인
                if not issubclass(
                    widget_class,
                    ctk.CTkFrame
                ):
                    continue

                # CTkFrame 자체는 제외
                if widget_class is ctk.CTkFrame:
                    continue

                print(
                    "Widget 클래스 발견:",
                    class_name
                )

                # --------------------------------------
                # Widget 생성
                # --------------------------------------

                self.create(
                    widget_class,
                    name
                )

                break

    # ==================================================
    # Widget Create
    # ==================================================

    def create(self, widget_class, name):

        # ------------------------------------------
        # 설정 불러오기
        # ------------------------------------------

        try:
            widgetinfo = (
                reader.USERDATA
                ["setting"]
                ["widget"]
                [name]
            )

        except KeyError:
            raise KeyError(
                f"Widget '{name}'의 설정을 "
                f"userdata.json에서 찾을 수 없습니다."
            )

        # ------------------------------------------
        # Widget 생성
        # ------------------------------------------

        widget = widget_class(
            master=self.master
        )

        # ------------------------------------------
        # Grid 배치
        # ------------------------------------------

        widget.grid(
            row=widgetinfo["row"],
            column=widgetinfo["column"],
            columnspan=widgetinfo["columnspan"],
            rowspan=widgetinfo["rowspan"],
            sticky="nsew",
            padx=5,
            pady=5
        )

        # ------------------------------------------
        # Widget 저장
        # ------------------------------------------

        self.widgets[name] = widget

        print(
            f"Widget 생성 완료: {name}"
        )

        return widget

    # ==================================================
    # Widget Remove
    # ==================================================

    def remove(self, name):

        if name not in self.widgets:
            return

        widget = self.widgets[name]

        if widget.winfo_exists():
            widget.destroy()

        del self.widgets[name]

    # ==================================================
    # Widget Get
    # ==================================================

    def get(self, name):

        return self.widgets.get(name)

    # ==================================================
    # Widget Clear
    # ==================================================

    def clear(self):

        for widget in self.widgets.values():

            if widget.winfo_exists():
                widget.destroy()

        self.widgets.clear()