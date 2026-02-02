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


def test_dropdown():
    driver = setup_chrome_driver()
    driver.get("https://nid.naver.com/user2/join/agree") #회원가입 페이지 이동
    time.sleep(2)
    
    # 전체 동의하기 체크박스 클릭
    try:
        agree_all_checkbox = driver.find_element(By.CSS_SELECTOR, "div.check_wrap.all")
        agree_all_checkbox.click()
        time.sleep(1)
        
        try:
            # aria_checked 속성 값 확인
            is_aria_checked = agree_all_checkbox.get_attribute("aria-checked")
            print(f"전체 동의하기 체크박스 aria-checked 속성 값: {is_aria_checked}")
        except Exception as e:
            print(f"aria-checked 속성 값을 가져오는 중 오류 발생: {e}")
    except NoSuchElementException:
        print("전체 동의하기 체크박스를 찾지 못함")
    except Exception as e:
        print(f"오류 발생 : {e}")
