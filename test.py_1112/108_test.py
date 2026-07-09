# 모듈을 읽어 들입니다.
from pathlib import Path
from urllib import request
from bs4 import BeautifulSoup

# 기상청 RSS 주소는 현재 XML이 아닌 HTML을 반환합니다.
# BeautifulSoup 연습을 위해 같은 형식의 XML 파일을 읽습니다.
sample_path = Path(__file__).with_name("weather_rss_sample.xml")
target = request.urlopen(sample_path.as_uri())
html = target.read()

# BeautifulSoup를 사용해 웹 페이지를 분석합니다.
soup = BeautifulSoup(html, "html.parser")

# location 태그를 찾습니다.
for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx 태그를 찾습니다.
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()


