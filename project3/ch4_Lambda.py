import sys
import os
from urllib.parse import unquote  # ✅ URL 디코딩 모듈

current_file = os.path.abspath(__file__) # 현재 파일 경로를 절대 경로로 변환
current_dir = os.path.dirname(current_file) # 현재 파일 경로(절대경로)에서 디렉토리만 남김
parent_dir = os.path.dirname(current_dir) # 디렉토리만 있는 경로의 부모 디렉토리
sys.path.insert(0, parent_dir)
# sys.path 목록에 가장 상단 위치에 parednt_dir를 추가함
# 이렇게 설정하면 parent_dir를 가장 먼저 탐색하여 dirver_setup 모듈을 찾을 수 있음


# 모듈 찾은걸 토대로 import
from utils.driver_setup import setup_chrome_driver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

# Explicitly wait 설정
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = setup_chrome_driver
wait = WebDriverWait(driver, 5)

driver.get("https://www.naver.com")

search_box = wait.until(
    EC.visibility_of_element_located((By.ID, "query"))
)

search_box.send_keys("Python")

# ✅ Lambda 함수로 커스텀 조건 만들기
# input 값의 길이가 6 이상일 때까지 대기
wait.until(
    lambda driver: len(driver.find_element(By.ID, "query").get_attribute("value")) >= 6
)
print("✅ 검색어가 6글자 이상 입력됨")

driver.quit()