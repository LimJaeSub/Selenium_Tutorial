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

try:
    driver.get("https://www.naver.com")
    
    # 존재하지 않는 요소 찾기 시도
    # 5초동안 못찾으면 except로 넘어감
    element = wait.until(
        EC.presence_of_element_located((By.ID, "nonexistent-element"))
    )
    print("✅ 요소 찾음")
    
except TimeoutException:
    print("⏰ Timeout 발생: 5초 안에 요소를 못 찾음")
    print("→ 대체 동작 수행 가능")

finally:
    driver.quit()