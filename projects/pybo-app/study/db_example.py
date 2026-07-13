"""
[선택] DB 연습용 파일 - 웹 사용과 무관

실행:
    cd "C:\\01. 파이썬\\projects\\pybo-app"
    .\\venv\\Scripts\\python.exe study\\db_example.py
"""

import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from pybo import create_app, db
from pybo.models import Question


def main():
    app = create_app()
    with app.app_context():
        q = Question(
            subject='연습 질문',
            content='study/db_example.py 에서 저장한 데이터',
            create_date=datetime.now(),
        )
        db.session.add(q)
        db.session.commit()
        print(f'저장 완료: id={q.id}')


if __name__ == '__main__':
    main()
