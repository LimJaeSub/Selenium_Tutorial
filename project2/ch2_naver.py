import sys
import os

current_file = os.path.abspath(__file__) # 현재 파일
current_dir = os.path.dirname(current_file) # project2
parent_dir = os.path.dirname(current_dir) # Selenium_Tutorial
sys.path.insert(0, parent_dir) 

from utils.driver_setup import setup_chrome_driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

def id_selector(driver):
    print("***id_selector 시작***")
    print("테스트 목표 : id로 검색창 찾기")
    try:
        element = driver.find_element(By.CSS_SELECTOR,"#query")
        print(f"찾은 요소의 태그: {element.tag_name}")
        return True
    except NoSuchElementException:
        print("* 검색창을 찾지 못함")
        return False
    except Exception as e:
        print(f"오류 발생 : {e}")
        return False 

def class_selector(driver):
    print("***class_selector 시작***")
    print("테스트 목표 : class로검색창 요소 찾기")
    try:
        element = driver.find_element(By.CSS_SELECTOR,".search_input")
        print(f"찾은 요소의 id : {element.get_attribute('id')}")
        return True
    except NoSuchElementException:
        print("* 검색창을 찾지 못함")
        return False   
    except Exception as e:
        print(f"오류 발생 : {e}")
        return False

def tag_selector(driver):
    print("***tag_selector 시작***")
    print("테스트 목표 : 모든 input 태그 요소 중 검색창 찾기")
    try:
        elements = driver.find_elements(By.CSS_SELECTOR,"input")
        print(f"찾은 input 태그 개수 : {len(elements)}")
        
        # elements에서 class명이 .search_input인 요소 찾기
        for it in elements:
            if(it.get_attribute("class")=="search_input"):
                print(f"검색창 요소 찾음, 해당 요소의 ID : {it.get_attribute('id')}")
        return True
    except NoSuchElementException:
        print("* input 태그를 찾지 못함")
        return False   
    except Exception as e:
        print(f"오류 발생 : {e}")
        return False
def main():
    driver = None
    try:
        driver = setup_chrome_driver()
        driver.get("https://www.naver.com")
        print("**** 브라우저 실행 완료 ****")
        time.sleep(2)
        
        testcase = []
        testcase.append(id_selector(driver))
        testcase.append(class_selector(driver))
        testcase.append(tag_selector(driver))
        print("==== TC 완료 ====")
        
        total_tc = len(testcase)
        passed_tc = 0
        
        for i in testcase:
            if i:
                passed_tc = passed_tc + 1
        
        print(f"총 {total_tc}개의 TC 중 {passed_tc}개의 TC 통과")
        print(f"TC 통과율 : {passed_tc/total_tc*100:.2f}%")
        
        
    except Exception as e:
        print(f"✗ 오류 발생: {e}") 
    finally:
        print("브라우저 종료")
        if(driver):
            input("종료하려면 엔터 키를 누르세요...")
            driver.quit()
              
        
        
    


if __name__ == "__main__":
    main()
    