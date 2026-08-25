import os
import importlib
import inspect
import customtkinter as ctk


class PageManager:
    def __init__(self, master):
        self.master = master

        self.pages = {}
        self.current_page = None

    def register(self, name, page_class):
        self.pages[name] = page_class

    def show(self, name):
        if name not in self.pages:
            raise ValueError(f"Page '{name}' is not registered.")

        if self.current_page is not None:
            self.current_page.destroy()

        page_class = self.pages[name]

        self.current_page = page_class(self.master.main)

        self.current_page.pack(
            fill="both",
            expand=True
        )

    def remove(self, name):
        if name in self.pages:
            del self.pages[name]

    def scan_pages(self):
        page_dir = "ui/pages"

        for filename in os.listdir(page_dir):
            if not filename.endswith(".py"):
                continue

            if filename.startswith("__"):
                continue

            name = filename[:-3]

            print("Page 발견:", filename)

            module = importlib.import_module(
                f"ui.pages.{name}"
            )

            # 모듈 안의 클래스 검색
            for class_name, page_class in inspect.getmembers(
                module,
                inspect.isclass
            ):
                # CTkFrame을 상속한 클래스인지 확인
                if (
                    issubclass(page_class, ctk.CTkFrame)
                    and page_class is not ctk.CTkFrame
                ):
                    print(
                        "Page 클래스 발견:",
                        class_name
                    )

                    self.register(
                        name,
                        page_class
                    )

                    break