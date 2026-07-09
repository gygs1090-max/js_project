from pathlib import Path
import runpy


SERVER_PATH = Path(__file__).resolve().parent / "프로젝트 예습" / "kakao_book_server.py"


if __name__ == "__main__":
    runpy.run_path(str(SERVER_PATH), run_name="__main__")
