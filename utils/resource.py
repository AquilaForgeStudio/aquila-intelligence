from pathlib import Path
import sys


def resource_path(*paths: str) -> Path:
    if getattr(sys, "frozen", False):
        # PyInstaller 실행 환경
        base_path = Path(sys.executable).resolve().parent
    else:
        # 개발 환경
        base_path = Path(__file__).resolve().parent.parent

    return base_path.joinpath(*paths)