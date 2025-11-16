from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://news.naver.com/")

# 페이지 로드 확인
time.sleep(2)

# 검색버튼 클릭
search_button = driver.find_element(By.CLASS_NAME, "Nicon_search")
search_button.click()

time.sleep(1)  # 검색창이 나타날 때까지 대기

# 검색 칸에 검색어 입력 (CSS_SELECTOR 사용)
search_box = driver.find_element(By.CSS_SELECTOR, "input._search_input")
search_box.send_keys("스포츠")

# 검색 버튼 클릭 (CSS_SELECTOR 사용)
search_submit_button = driver.find_element(By.CSS_SELECTOR, "button._submit_btn")
search_submit_button.click()

time.sleep(3)

# 검색 결과 출력
result = driver.find_element(By.TAG_NAME, "span")
print(f"검색 결과: {result.text}")

input("브라우저를 닫으려면 Enter를 누르세요...")
driver.quit()