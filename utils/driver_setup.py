from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# Explicitly wait 설정
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_chrome_driver():
    """크롬 드라이버 설정 (봇 탐지 방지 포함)"""
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") # 블링크 기능 비활성화
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 자동화 플래그 제거(일반 브라우저로 속임)
    chrome_options.add_experimental_option('useAutomationExtension', False) # 자동화 확장 플러그인 비활성화
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    
    
    
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
    # navigator의 webdriver 속성을 get할때 undefined로 반환하여 숨김
    # navigater.webdriver가 true일 경우 chrome의 reCAPTCHA가 발생함
    
    return driver

def setup_simple_driver():
    """간단한 크롬 드라이버 (봇 탐지 방지 없음)"""
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)


