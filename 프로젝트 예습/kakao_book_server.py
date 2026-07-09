from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
import re
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urlparse
from urllib.request import Request, urlopen


HOST = "localhost"
PORT = 8000
BASE_DIR = Path(__file__).resolve().parent
KAKAO_REST_API_KEY = os.environ.get(
    "KAKAO_REST_API_KEY",
    "5e010a1d2719cb4c1e3ac7e9bc3d80d0",
)


class KakaoBookHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        parsed_url = urlparse(self.path)

        if parsed_url.path == "/api/kakao-books":
            self.handle_kakao_books(parsed_url.query)
            return

        super().do_GET()

    def handle_kakao_books(self, query_string):
        params = parse_qs(query_string)
        query = params.get("query", [""])[0].strip()
        author = params.get("author", [""])[0].strip()
        size = params.get("size", ["5"])[0]

        if not query:
            self.send_json({"error": "검색어를 입력해 주세요."}, status=400)
            return

        try:
            data = self.search_kakao_books(query, size, author)
        except HTTPError as error:
            self.send_json(
                {"error": f"카카오 API 요청 실패: {error.code}"},
                status=error.code,
            )
            return
        except URLError:
            self.send_json(
                {"error": "카카오 API 서버에 연결하지 못했습니다."},
                status=502,
            )
            return

        self.send_json(data)

    def search_kakao_books(self, query, size, author):
        data = None

        for search_query in self.build_search_queries(query, author):
            data = self.request_kakao_books(search_query, size)
            documents = data.get("documents", [])

            if documents:
                data["search_query_used"] = search_query
                return data

        if data is None:
            data = {"documents": [], "meta": {"total_count": 0}}

        data["search_query_used"] = query
        return data

    def build_search_queries(self, query, author):
        base_query = re.split(r"\s+-\s+|\(|\[", query, maxsplit=1)[0].strip()
        compact_query = re.sub(r"\s+", " ", base_query)
        candidates = [
            query,
            compact_query,
            f"{compact_query} {author}".strip(),
            f"{author} {compact_query}".strip(),
            author,
        ]
        unique_queries = []

        for candidate in candidates:
            if candidate and candidate not in unique_queries:
                unique_queries.append(candidate)

        return unique_queries

    def request_kakao_books(self, query, size):
        kakao_query = urlencode({"query": query, "size": size})
        request = Request(
            f"https://dapi.kakao.com/v3/search/book?{kakao_query}",
            headers={"Authorization": f"KakaoAK {KAKAO_REST_API_KEY}"},
        )

        with urlopen(request, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))

    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    server = ThreadingHTTPServer((HOST, PORT), KakaoBookHandler)
    print(f"서버 실행 중: http://{HOST}:{PORT}/")
    print("종료하려면 Ctrl+C를 누르세요.")
    server.serve_forever()


if __name__ == "__main__":
    main()
