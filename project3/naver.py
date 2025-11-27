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

# Explicitly wait 설정
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def safe_find_click(driver, wait, retries=3):
    # 안전하게 요소 찾기
    for attempt in range(retries):
        try:
            # 해당 함수는 자동완성이 생긴 뒤 호출되는 함수이므로
            # 굳이 presence_of_element_located로 대기할 필요 없음
            second_item_click_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '.kwd_lst .item:nth-child(2) .kwd')
                )
            )
            print("요소 찾음")
            return second_item_click_btn
        except TimeoutException:
            print("버튼 찾기 실패")
            print(f"❌ {attempt+1}번째 시도: 두 번째 자동완성 요소를 찾지 못했습니다. 재시도 중...")
            if attempt == retries - 1:
                raise
            time.sleep(1)

    
def main():
    driver = setup_chrome_driver()
     
    try:
        # driver & wait 설정
        driver.get("https://www.naver.com")
        wait = WebDriverWait(driver, 10)
        
        # 검색창 찾기
        search_box = wait.until(EC.visibility_of_element_located((By.ID,"query")))
        
        # 자동완성 확인
        search_word = input("자동완성 검색어 입력 : ")
        for char in search_word:
            search_box.send_keys(char) # search_word의 글자 하나씩 입력
            time.sleep(0.3) # 자동완성 나타나는 시간
        
        print(f"{search_word} 입력 완료")
        time.sleep(1)
        
        page_source = driver.page_source
        
        if 'role="listbox"' in page_source:
            print("✅ 페이지에 role='listbox' 존재함")
        else:
            print("❌ 페이지에 role='listbox' 없음")
        
        if 'kwd_lst' in page_source:
            print("✅ 페이지에 'kwd_lst' 클래스 존재함")
        else:
            print("❌ 페이지에 'kwd_lst' 클래스 없음")
            
            
        try:
            autocomplete_list = wait.until(
                 EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".kwd_lst")
                )
            )
            print("✅ 자동완성 항목이 나타났습니다.")
            
            list_items = wait.until(
                EC.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, '.kwd_lst .item .kwd_txt') # 자동완성 항목들
                )
            )
            
            print(f"자동완성 항목 개수 : {len(list_items)}")
            for item in list_items:
                print(f"- {item.text}")
                
        except TimeoutException:
            print("❌ 자동완성 항목이 나타나지 않았습니다.")
            
        second_item = list_items[1]
        print(f"자동완성 두 번째 요소 : {second_item.text}")
        
        # 두 번째 요소 클릭
        print("두 번째 요소 클릭 대기 중")
        second_btn = safe_find_click(driver,wait,retries=3)
        
        second_btn.click()
        print("두 번째 요소 클릭 완료")
        
        # 결과 페이지가 변경되었는지 확인
        # 페이지 url에 search_word가 포함되었는지 확인
        
        time.sleep(2) # 페이지 변환 대기
        current_url = unquote(driver.current_url) # URL 디코딩
        
        print(f"현재 URL: {current_url}")
        print(f"검색어: {search_word}")
        
        if(search_word in current_url):
            print("✅ 결과 페이지 URL에 검색어가 포함되어 있습니다.")
        else:
            print("❌ 결과 페이지 URL에 검색어가 포함되어 있지 않습니다.")
        
    except Exception as e:
        print(f"❌ 에러 발생: {e}")
    
    finally:
        input("엔터키 누르면 종료...")
        driver.quit()    
        
if __name__=="__main__":
    main()
    