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
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# Explicitly wait 설정
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def test_input_methods():
    driver = setup_chrome_driver()
    
    try:
        driver.get("https://www.naver.com")
        wait = WebDriverWait(driver, 10)
        
        # 검색창 찾기
        search_box = wait.until(EC.visibility_of_element_located((By.ID,"query")))
        
        # 1. 기본 입력
        print("텍스트 입력 ...")
        search_box.clear()
        search_box.send_keys("python")
        
        # 2. 입력 내용 지우기
        print("입력 내용 지우기...")
        search_box.clear()
        time.sleep(1)
        
        # 3. 한 글자씩 입력(타이핑)
        print("한 글자씩 입력...")
        search_word = "selenium"
        for char in search_word:
            search_box.send_keys(char)
            time.sleep(0.3) # 타이핑 속도 조절
        time.sleep(2)
        
        # 4. 전체 블록 삭제
        print("전체 블록 삭제...")
        search_box.send_keys(Keys.CONTROL, 'a') # 전체 선택
        time.sleep(0.5)
        search_box.send_keys(Keys.DELETE) # 삭제
        time.sleep(2)
        
        # 5. 입력 후 엔터
        print("입력 후 엔터...")
        search_box.send_keys("검색어")
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)
        
        # 결과 페이지 대기
        wait.until(
            lambda driver : "search.naver.com" in driver.current_url
            and
            "검색어" in unquote(driver.current_url)
                   )
        
        print("검색 완료")
    except Exception as e : 
        print("에러 발생")
        print(e)
    finally:
        driver.quit()

if __name__ == "__main__":
    test_input_methods()
        
        
        
        
        
        
    