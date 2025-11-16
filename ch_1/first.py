from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 브라우저 오픈
# webdriver.Chrome() # 크롬 브라우저 열기
# ChromeDriverManager().install() # 크롬 드라이버 설치
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# URL 접속
driver.get("https://naver.com")


# ID로 요소 찾기(검색창)
search_box = driver.find_element(By.ID,"query")

# 검색어 입력
search_box.send_keys("검색테스트")

# 검색
# 1. 엔터키 누르기
search_box.send_keys(Keys.RETURN)

# 2. 검색 버튼 클릭
#search_button = driver.find_element(By.ID,"search-btn")
#search_button.click()


# 페이지 확인용 3초 대기
import time
time.sleep(3)


#3. 검색 결과 확인
first_result = driver.find_element(By.TAG_NAME, "h2")
print(f"첫 번째 검색 결과: {first_result.text}")

# 브라우저 닫기
# 스크립트가 종료되면 driver는 메모리가 해제되어 자동으로 브라우저가 닫힘.
#driver.quit()