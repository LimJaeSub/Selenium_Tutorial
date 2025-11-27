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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException





def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    driver = webdriver.Chrome(options=options)
    
    # ✅ Implicit Wait 설정 - 모든 find_element에 적용됨
    driver.implicitly_wait(10)  # 최대 10초 대기
    
    return driver

driver = setup_driver()
driver.get("https://www.naver.com")

# 이제 요소가 로드될 때까지 자동으로 기다림
search_box = driver.find_element(By.ID, "query")
print("✅ 검색창 찾음")

driver.quit()
