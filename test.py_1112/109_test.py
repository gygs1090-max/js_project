# 모듈을 읽어 들입니다.
from pathlib import Path
from flask import Flask
from bs4 import BeautifulSoup

# 웹 서버를 생성합니다.
app = Flask(__name__)
@app.route("/")

def hello():
    # 기상청 RSS 주소는 현재 XML이 아닌 HTML을 반환합니다.
    # BeautifulSoup 연습을 위해 같은 형식의 XML 파일을 읽습니다.
    sample_path = Path(__file__).with_name("weather_rss_sample.xml")

    # BeautifulSoup를 사용해 웹 페이지를 분석합니다.
    with sample_path.open(encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # location 태그를 찾습니다.
    output = ""
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx 태그를 찾습니다.
        city = location.select_one("city").string
        wf = location.select_one("wf").string
        tmn = location.select_one("tmn").string
        tmx = location.select_one("tmx").string

        # 도시, 날씨, 최저기온, 최고기온을 출력합니다.
        output += "<h3>{}</h3>".format(city)
        output += "날씨: {}<br/>".format(wf)
        output += "최저/최고기온: {}℃ / {}℃<br/>".format(tmn, tmx)
        output += "<hr/>"
    return output

if __name__ == "__main__":
    app.run(port=5001)
