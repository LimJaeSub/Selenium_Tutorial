import sys
import os

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

# Explicitly wait 설정
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def find_element_retry(driver,by,value,timeout=10,retries=3):
    # 대기시간
    wait = WebDriverWait(driver,timeout)
    
    for i in range(retries):
        try:
            element = wait.until(
                EC.visibility_of_element_located((by,value))
            )
            print(f"✅ 요소를 찾았습니다: {value}")
            return element
        except TimeoutException:
            print(f"❌ 요소를 찾지 못했습니다. 재시도 {i+1}/{retries}: {value}")
            if i == retries-1:
                raise ValueError("재시도 횟수 초과")
            time.sleep(1) # 재시도 전 대기 시간
    
def main():
    driver = setup_chrome_driver()
     
    try:
        driver.get("https://www.naver.com")
        wait = WebDriverWait(driver,10) # 10초 대기
        
        # 재시도 로직이 포함된 search_box 찾기
        search_box = find_element_retry(
            driver,By.ID,"query",timeout=10,retries=3
        )
        
        # 검색어 입력
        search_box.send_keys("검색어임")
        
        # 버튼 렌더링 대기
        search_button = wait.until(
            EC.element_to_be_clickable((By.ID, "search-btn"))
        )
        print("✅ 검색 버튼 준비 완료")
        
        # 검색버튼 클릭
        search_button.click()
        
        # 페이지 이동 대기
        try:
            wait.until(EC.url_contains("search.naver.com")) # URL에 search.naver.com 이 포함되어있을때까지 대기
            print(f"✅ 페이지 이동 완료: {driver.current_url}")
        except TimeoutException:
            print("❌ 페이지 이동 대기 시간 초과")
            
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
    
    finally:
        driver.quit()    
        
if __name__=="__main__":
    main()
    