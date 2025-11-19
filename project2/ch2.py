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
import time




def setup_driver():
    driver = setup_chrome_driver()
    
    return driver

def tag_selector(driver, testurl):
    print("tag_selector 테스트 시작")
    try:
        driver.get(testurl) # testurl 접속
        time.sleep(2) # 페이지 로드 대기
        
        element_inputs = driver.find_elements(By.CSS_SELECTOR, "input") # 모든 input 태그 선택
        print(f"input 태그 개수 : {len(element_inputs)}")
        
        return True
    except Exception as e:
        print(f"오류 발생 / 페이지 로드 실패 : {e}")
        return False
    
def attribute_selector(driver, testurl, attribute_name, attribute_value):
    print("attribute_selector 테스트 시작")
    try:
        driver.get(testurl)
        time.sleep(2)
        
        selector = f'[{attribute_name}="{attribute_value}"]'
        elements = driver.find_elements(By.CSS_SELECTOR, selector)
        
        # ✅elements는 리스트
        if elements:
            print(f"찾은 요소 개수 : {len(elements)}")
            print(f"첫 번째 요소의 TAG명 : {elements[0].tag_name}")
        else:
            print("요소를 찾지 못했습니다")
        
        return True
        
    except NoSuchElementException:
        print("✗ 검색창을 찾을 수 없습니다")
        return False
    
    except Exception as e:
        print(f"✗ 오류 발생: {e}")
        return False
    
def class_selector(driver, testurl):
    print("class_selector 테스트 시작")
    try:
        driver.get(testurl)
        time.sleep(2)
        
        # class로 찾기 (점 사용)
        elements = driver.find_elements(By.CSS_SELECTOR, ".w3-button")
        print(f"✓ .w3-button class 개수: {len(elements)}")
        return True
        
    except Exception as e:
        print(f"✗ 오류 발생: {e}")
        return False
    
def id_selector(driver, testurl):
    print("id_selector 테스트 시작")
    try:
        driver.get(testurl)
        time.sleep(2)
        
        # id로 찾기 (# 사용)
        element = driver.find_element(By.CSS_SELECTOR, "#search2")
        
        class_name = element.get_attribute("class")
        print(f"✓ ID로 찾기 성공")
        print(f"class 속성 값: {class_name}")
        return True
        
    except NoSuchElementException:
        print("✓ 해당 ID 없음 (정상)")
        return True
    except Exception as e:
        print(f"✗ 오류 발생: {e}")
        return False
    
def combination_selector(driver, testurl):
    print("combination_selector 테스트 시작")
    try:
        driver.get(testurl)
        time.sleep(2)
        
        # 태그 + 속성
        element = driver.find_element(By.CSS_SELECTOR, "input[name='search']")
        print(f"✓ input[name='search'] 찾기 성공")
        
        # 태그 + class
        elements = driver.find_elements(By.CSS_SELECTOR, "a.w3-button")
        print(f"✓ a.w3-button 개수: {len(elements)}")
        return True
        
    except NoSuchElementException:
        print("✗ 요소를 찾을 수 없습니다")
        return False
    except Exception as e:
        print(f"✗ 오류 발생: {e}")
        return False
        
def main():
    driver = None
    try:
        driver = setup_driver()
        print("드라이버 실행 완료")
        time.sleep(2)
    
        result = []
        result.append(tag_selector(driver, "https://www.w3schools.com/html/html_forms.asp"))
        result.append(attribute_selector(driver, "https://www.google.com", "name", "q"))
        result.append(class_selector(driver, "https://www.w3schools.com"))
        result.append(id_selector(driver, "https://www.w3schools.com"))
        result.append(combination_selector(driver, "https://www.w3schools.com"))
        
        total_coverage = len(result)
        success_count = sum(1 for isSuccess in result if isSuccess == True)
        
        
        print(f"총 테스트 갯수 : {total_coverage}")
        print(f"테스트 성공 갯수 : {success_count}")
        print("*" * 20)
        print(f"테스트 성공률 : {success_count/total_coverage*100:.2f}%")
        
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        if driver:  # ✅ driver 존재 확인 추가
            driver.quit()
            print("테스트 종료, 드라이버 종료")

if __name__ == "__main__":
    main()