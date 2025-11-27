# Selenium_Tutorial
<details>
   <summary>
      Selenium 1단계: 기초
   </summary>
   ---

## 1️⃣ 환경 설정

### 필수 패키지 설치
```bash
pip install selenium
pip install webdriver-manager
```

### 기본 코드 구조
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 추가적인 import
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Chrome 브라우저 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

---

## 2️⃣ 브라우저 제어

### 페이지 열기
```python
driver.get("https://www.naver.com")
```

### 브라우저 닫기
```python
driver.quit()   # 브라우저 완전 종료 (모든 탭)
driver.close()  # 현재 탭만 닫기
```

### 페이지 정보 가져오기
```python
current_url = driver.current_url  # 현재 URL
title = driver.title              # 페이지 제목
page_source = driver.page_source  # 페이지 소스 HTML
```

---

## 3️⃣ 웹 요소 찾기

```python
from selenium.webdriver.common.by import By
```

### 요소 찾는 4가지 방법

| 방법 | 코드 예시 | 설명 |
|------|----------|------|
| **ID** | `driver.find_element(By.ID, "query")` | 가장 정확하고 빠름 |
| **Name** | `driver.find_element(By.NAME, "q")` | form 요소에 많이 사용 |
| **Class Name** | `driver.find_element(By.CLASS_NAME, "btn")` | 하나의 클래스만 가능 |
| **Tag Name** | `driver.find_element(By.TAG_NAME, "h1")` | HTML 태그로 찾기 |


---

## 4️⃣ 요소 상호작용

### 텍스트 입력
```python
from selenium.webdriver.common.keys import Keys

search_box = driver.find_element(By.ID, "query")
search_box.send_keys("검색어 입력")
```

### 클릭
```python
button = driver.find_element(By.ID, "search-btn")
button.click()
```

### Enter 키 입력
```python
search_box.send_keys(Keys.RETURN)
```

### 요소의 텍스트 가져오기
```python
element = driver.find_element(By.TAG_NAME, "h1")
print(element.text)
```

---

## 5️⃣ 시간 대기

### 단순 대기
```python
import time
time.sleep(3)  # 3초 대기
```

time.sleep()은 페이지 렌더링 확인용으로만 사용

### 사용자 입력 대기
```python
input("브라우저를 닫으려면 Enter를 누르세요...")
```

사용자 입력 대기 방법을 위주로 사용할 것

---

## 🎯 실습 예제 (네이버 검색)

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 브라우저 오픈
# webdriver.Chrome() # 크롬 브라우저 열기
# ChromeDriverManager().install() # 크롬 드라이버 설치
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# URL 접속
driver.get("https://naver.com")


# ID로 요소 찾기(검색창)
search_box = driver.find_element(By.ID,"query")

# 검색어 입력
search_box.send_keys("검색테스트")

# 검색
# 1. 엔터키 누르기
search_box.send_keys(Keys.RETURN)

# 2. 검색 버튼 클릭
#search_button = driver.find_element(By.ID,"search-btn")
#search_button.click()


# 페이지 확인용 3초 대기
import time
time.sleep(3)


#3. 검색 결과 확인
first_result = driver.find_element(By.TAG_NAME, "h2")
print(f"첫 번째 검색 결과: {first_result.text}")

# 브라우저 닫기
# 스크립트가 종료되면 driver는 메모리가 해제되어 자동으로 브라우저가 닫힘.
#driver.quit()
```


### 추가 예제 (CSS_SELECTOR를 이용)
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://news.naver.com/")

# 페이지 로드 확인
time.sleep(2)

# 검색버튼 클릭
search_button = driver.find_element(By.CLASS_NAME, "Nicon_search")
search_button.click()

time.sleep(1)  # 검색창이 나타날 때까지 대기

# 검색 칸에 검색어 입력 (CSS_SELECTOR 사용)
search_box = driver.find_element(By.CSS_SELECTOR, "input._search_input")
search_box.send_keys("스포츠")

# 검색 버튼 클릭 (CSS_SELECTOR 사용)
search_submit_button = driver.find_element(By.CSS_SELECTOR, "button._submit_btn")
search_submit_button.click()

time.sleep(3)

# 검색 결과 출력
result = driver.find_element(By.TAG_NAME, "span")
print(f"검색 결과: {result.text}")

input("브라우저를 닫으려면 Enter를 누르세요...")
driver.quit()
```

---

## 📌 핵심 정리

### 필수 import
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
```

### 기본 흐름
1. **브라우저 실행** → `driver = webdriver.Chrome(...)`
2. **페이지 이동** → `driver.get(url)`
3. **요소 찾기** → `driver.find_element(By.ID, "...")`
4. **상호작용** → `element.send_keys()` / `element.click()`
5. **브라우저 종료** → `driver.quit()`

---

## ⚠️ 주의사항

1. **요소를 찾을 수 없을 때**
   - 페이지가 로딩 중일 수 있음 → `time.sleep()` 추가
   - ID, Name 등이 정확한지 개발자 도구로 확인

2. **브라우저가 바로 닫힐 때**
   - 스크립트가 끝나면 자동으로 닫힘
   - `input()` 또는 `time.sleep()`으로 대기 추가

---
</details>
<details>
   <summary>Selenium 2단계 : CSS Selector</summary>

## 📚 학습 목표

1. CSS Selector 기본 문법 이해
2. 다양한 CSS Selector 패턴 실습
3. 복잡한 요소 정확하게 찾기
4. 개발자 도구로 Selector 검증하기

---


## 📖 주요 CSS Selector 패턴

### 1. 기본 선택자

| 선택자 | 문법 | 예시 | 설명 |
|--------|------|------|------|
| **태그** | `태그명` | `"input"`, `"div"` | 특정 태그의 모든 요소 |
| **ID** | `#id값` | `"#query"` | 고유한 ID를 가진 요소 |
| **Class** | `.class명` | `".search_input"` | 특정 클래스를 가진 요소 |
| **속성** | `[속성='값']` | `"[name='q']"` | 특정 속성을 가진 요소 |

### 2. 조합 선택자

```python
# 태그 + Class
driver.find_element(By.CSS_SELECTOR, "input.search-box")

# 여러 Class (공백 없이!)
driver.find_element(By.CSS_SELECTOR, ".class1.class2")

# 속성 여러개
driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='query']")
```

### 3. 계층 구조 선택자

```python
# 자식 (직계 자식만)
driver.find_element(By.CSS_SELECTOR, "div > input")

# 후손 (모든 하위 요소)
driver.find_element(By.CSS_SELECTOR, "form input")

# 형제 (바로 다음)
driver.find_element(By.CSS_SELECTOR, "label + input")
```

### 4. 속성 매칭 선택자

```python
# 시작 문자열
driver.find_element(By.CSS_SELECTOR, "[class^='btn-']")  # btn-으로 시작

# 끝 문자열
driver.find_element(By.CSS_SELECTOR, "[class$='-box']")  # -box로 끝

# 포함
driver.find_element(By.CSS_SELECTOR, "[class*='search']")  # search 포함
```

### 5. 가상 선택자

```python
# 첫 번째 자식
driver.find_element(By.CSS_SELECTOR, "li:first-child")

# 마지막 자식
driver.find_element(By.CSS_SELECTOR, "li:last-child")

# n번째 자식
driver.find_element(By.CSS_SELECTOR, "li:nth-child(2)")
```

---

## 🔍 요소 정보 가져오기

### 요소 자체 정보 (전용 속성/메서드)

요소의 기본 정보는 **속성(property)** 또는 **메서드(method)**로 접근합니다.

| 정보 | 코드 | 반환 타입 | 예시 |
|------|------|-----------|------|
| **태그명** | `element.tag_name` | 속성 | `"input"`, `"div"`, `"a"` |
| **텍스트 내용** | `element.text` | 속성 | 요소의 텍스트 |
| **크기** | `element.size` | 속성 | `{'width': 100, 'height': 50}` |
| **위치** | `element.location` | 속성 | `{'x': 10, 'y': 20}` |
| **위치+크기** | `element.rect` | 속성 | 크기와 위치 정보 |
| **표시 여부** | `element.is_displayed()` | 메서드 | `True`/`False` |
| **활성화 여부** | `element.is_enabled()` | 메서드 | `True`/`False` |
| **선택 여부** | `element.is_selected()` | 메서드 | `True`/`False` (체크박스, 라디오) |

```python
element = driver.find_element(By.CSS_SELECTOR, "#query")

# 요소 자체 정보
print(element.tag_name)        # input
print(element.text)            # 텍스트 내용
print(element.size)            # {'width': 586, 'height': 49}
print(element.location)        # {'x': 100, 'y': 200}
print(element.is_displayed())  # True
```

### HTML 속성값 가져오기 (get_attribute)

HTML 태그에 실제로 작성된 **속성(attribute)**은 `get_attribute()` 메서드로 접근합니다.

#### 자주 사용하는 HTML 속성들

| 속성 | 코드 | 설명 | 예시 |
|------|------|------|------|
| **id** | `element.get_attribute("id")` | 요소의 고유 ID | `"query"` |
| **class** | `element.get_attribute("class")` | CSS 클래스명 | `"search_input"` |
| **name** | `element.get_attribute("name")` | input의 name 속성 | `"q"` |
| **type** | `element.get_attribute("type")` | input 타입 | `"text"`, `"password"` |
| **value** | `element.get_attribute("value")` | input의 값 | 입력된 텍스트 |
| **placeholder** | `element.get_attribute("placeholder")` | 안내 텍스트 | `"검색어를 입력하세요"` |
| **href** | `element.get_attribute("href")` | 링크 주소 | `"https://..."` |
| **src** | `element.get_attribute("src")` | 이미지/스크립트 경로 | `"image.png"` |
| **alt** | `element.get_attribute("alt")` | 이미지 대체 텍스트 | `"로고"` |
| **title** | `element.get_attribute("title")` | 툴팁 텍스트 | `"클릭하세요"` |
| **style** | `element.get_attribute("style")` | 인라인 CSS | `"color: red;"` |
| **disabled** | `element.get_attribute("disabled")` | 비활성화 여부 | `"true"` 또는 `None` |
| **readonly** | `element.get_attribute("readonly")` | 읽기 전용 여부 | `"true"` 또는 `None` |
| **data-*** | `element.get_attribute("data-id")` | 커스텀 데이터 속성 | 임의의 값 |

```python
# HTML 예시:
# <input id="query" class="search_input" name="q" type="text" 
#        placeholder="검색어 입력" data-testid="search-box">

element = driver.find_element(By.CSS_SELECTOR, "#query")

# HTML 속성 가져오기
print(element.get_attribute("id"))          # query
print(element.get_attribute("class"))       # search_input
print(element.get_attribute("name"))        # q
print(element.get_attribute("type"))        # text
print(element.get_attribute("placeholder")) # 검색어 입력
print(element.get_attribute("data-testid")) # search-box
```

#### 여러 class가 있는 경우

```python
# HTML: <div class="btn btn-primary btn-large">버튼</div>

element = driver.find_element(By.CSS_SELECTOR, "div")
class_name = element.get_attribute("class")
print(class_name)  # "btn btn-primary btn-large"

# 개별 class로 분리
classes = class_name.split()
print(classes)  # ['btn', 'btn-primary', 'btn-large']

# 특정 class 포함 여부 확인
if "btn-primary" in classes:
    print("btn-primary 클래스가 있습니다!")
```

### 🔑 핵심 차이점

| 구분 | 접근 방법 | 예시 | 괄호 |
|------|-----------|------|------|
| **요소 자체 정보** | 속성/메서드 | `element.tag_name`, `element.text` | 속성은 없음, 메서드는 `()` |
| **HTML 속성** | `get_attribute()` | `element.get_attribute("class")` | 항상 `()` 필요 |

```python
# ❌ 잘못된 사용
element.get_attribute("tag")      # None (tag는 속성이 아님!)
element.tag_name()                # TypeError! (tag_name은 속성)

# ✅ 올바른 사용
element.tag_name                  # "input" (속성)
element.get_attribute("class")    # "search_input" (HTML 속성)
```

---

## 💻 실습 코드

### 네이버 검색창 찾기 (3가지 방법 : id / class / tag-input)

```python
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
    
```


## 🔧 추가 학습 내용

### 1. 절대 경로 설정

프로젝트에서 상위 폴더의 모듈을 import 하기 위한 절대 경로 설정 방법
모듈 폴더를 따로 만들어서 실제 사용하는 py 파일에 가져다 쓰는 방법법

#### 파일 구조
```
Selenium_Tutorial/
├── utils/
│   ├── __init__.py
│   └── driver_setup.py
└── project2/
    └── ch2.py
```

#### 절대 경로 코드
```python
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
```

#### 각 함수 설명

| 함수 | 역할 | 예시 |
|------|------|------|
| `__file__` | 현재 실행 중인 파일 | `"ch2.py"` |
| `os.path.abspath()` | 상대 경로 → 절대 경로 변환 | `"C:\...\project2\ch2.py"` |
| `os.path.dirname()` | 파일/폴더의 부모 디렉토리 추출 | `"C:\...\project2"` |
| `sys.path.insert(0, path)` | Python 모듈 검색 경로 맨 앞에 추가 | 우선순위 최고 |


### 2. driver_setup 모듈화

반복적으로 사용하는 드라이버 설정 코드를 별도 파일로 분리하여 재사용합니다.

#### utils/driver_setup.py

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def setup_chrome_driver():
    """크롬 드라이버 설정 (봇 탐지 방지 포함)"""
    chrome_options = Options()
    
    # 자동화 탐지 방지 설정
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # WebDriver 속성 숨기기
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

def setup_simple_driver():
    """간단한 크롬 드라이버 (봇 탐지 방지 없음)"""
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)
```

#### 봇 탐지 방지 설정 설명

| 설정 | 역할 |
|------|------|
| `--disable-blink-features=AutomationControlled` | 자동화 플래그 비활성화 |
| `excludeSwitches: ["enable-automation"]` | "자동화 중" 배너 제거 |
| `useAutomationExtension: False` | 자동화 확장 프로그램 제거 |
| `execute_script(...)` | navigator.webdriver 속성 완전 제거 |

#### 사용 방법

```python
# 다른 파일에서 import해서 사용
from utils.driver_setup import setup_chrome_driver

driver = setup_chrome_driver() # main에 선언 및 할당
driver.get("https://www.naver.com")
# 작업 수행
driver.quit()
```



## 📝 주요 학습 내용 정리

### CSS Selector 핵심

1. **ID 선택자**: `#id명` - 가장 빠르고 명확
2. **Class 선택자**: `.class명` - 여러 요소에 사용
3. **태그 선택자**: `태그명` - 모든 해당 태그
4. **속성 선택자**: `[속성='값']` - 유연한 검색
5. **조합 선택자**: `태그.class`, `태그[속성='값']` - 정확한 타겟팅

### Python/Selenium 핵심

1. **요소 정보 접근**:
   - 요소 자체: `element.tag_name`, `element.text` (속성)
   - HTML 속성: `element.get_attribute("속성명")` (메서드)

2. **코드 구조**:
   - 함수에 `driver` 파라미터 전달
   - `try-except-finally`로 안전한 예외 처리
   - 모듈화로 코드 재사용성 향상

3. **경로 설정**:
   - 절대 경로로 실행 위치 무관하게 import
   - `sys.path.insert(0, parent_dir)`로 우선순위 설정

---


**작성일**: 2025-11-19

</details>

<details>
    <summary>
      Selenium 3단계: Wait
    </summary>
    

### 주요 학습 내용
- Implicit Wait (암묵적 대기)
- Explicit Wait (명시적 대기)
- Expected Conditions (EC)
- Timeout 예외 처리
- 커스텀 Wait 조건
- 동적 페이지 요소 다루기

---

## 🎯 핵심 개념

### 1. Wait가 필요한 이유

```python
# ❌ 이렇게 하면 에러 발생 가능
driver.get("https://example.com")
element = driver.find_element(By.ID, "button")  # 페이지 로딩 중이라 요소가 없을 수 있음!
element.click()
```

페이지가 완전히 로드되기 전에 요소를 찾으려고 하면 `NoSuchElementException` 에러가 발생

### 2. Wait의 3가지 종류

#### 1) Implicit Wait (암묵적 대기)
```python
driver.implicitly_wait(10)  # 최대 10초까지 기다림
```
- 모든 `find_element()`에 **자동으로 적용**되는 전역 대기 시간
- 요소를 못 찾으면 최대 10초까지 0.5초마다 재시도

#### 2) Explicit Wait (명시적 대기)
```python
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "button")))
```
- **특정 요소**에만 적용하는 대기
- **조건**(Condition)을 만족할 때까지 기다림

#### 3) Expected Conditions (EC)
- Explicit Wait에서 사용하는 **미리 정의된 조건들**
- 예: `presence_of_element_located`, `element_to_be_clickable`, `visibility_of_element_located` 등 
- 

---

## 🔧 주요 Expected Conditions

```python
# 1. 요소가 DOM에 존재할 때까지 대기
EC.presence_of_element_located((By.ID, "element"))

# 2. 요소가 보일 때까지 대기 (visibility)
EC.visibility_of_element_located((By.ID, "element"))

# 3. 요소가 클릭 가능할 때까지 대기
EC.element_to_be_clickable((By.ID, "button"))

# 4. 텍스트가 포함될 때까지 대기
EC.text_to_be_present_in_element((By.ID, "message"), "완료")

# 5. input 필드의 value에 텍스트가 포함될 때까지 대기
EC.text_to_be_present_in_element_value((By.ID, "query"), "Python")

# 6. 요소가 사라질 때까지 대기
EC.invisibility_of_element_located((By.ID, "loading"))

# 7. URL이 변경될 때까지 대기
EC.url_contains("search.naver.com")
```

---

## 💡 presence vs visibility - 중요한 차이점!

### presence_of_element_located
```python
# ✅ DOM에 존재하기만 하면 OK
wait.until(EC.presence_of_element_located((By.ID, "element")))

# 다음 경우에도 찾을 수 있음:
# - display: none 이어도 OK
# - opacity: 0 이어도 OK
# - 화면 밖에 있어도 OK
```

### visibility_of_element_located
```python
# ✅ DOM에 존재 + 화면에 보여야 함
wait.until(EC.visibility_of_element_located((By.ID, "element")))

# 다음 경우에는 찾을 수 없음:
# - display: none → ❌
# - opacity: 0 → ❌
# - width/height가 0 → ❌
```

### 언제 무엇을 사용할까?

| 상황 | 추천 | 이유 |
|------|------|------|
| 동적으로 추가되는 요소 | `presence` | DOM 추가가 중요 |
| 애니메이션 효과 있는 요소 | `presence` → 확인 | 애니메이션 완료 전에도 작업 가능 |
| 클릭/입력해야 하는 요소 | `visibility` 또는 `clickable` | 실제로 보여야 상호작용 가능 |
| 단순 정보 추출 | `presence` | 화면에 안 보여도 데이터는 있음 |

**실전 패턴:**
```python
# 1. presence로 빠르게 찾기
element = wait.until(EC.presence_of_element_located((By.ID, "element")))

# 2. 필요시 화면에 보일 때까지 추가 대기
wait.until(lambda driver: element.is_displayed())
```

---

## 📝 실습 코드

### 1. Implicit Wait 기본 사용

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

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
```

### 2. Explicit Wait로 조건 대기

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.naver.com")

# Explicit Wait 객체 생성
wait = WebDriverWait(driver, 10)

# 검색창이 보일 때까지 대기
search_box = wait.until(
    EC.visibility_of_element_located((By.ID, "query"))
)

# 검색어 입력
search_box.send_keys("Python")

# input 필드의 value에 "Python"이 포함될 때까지 대기
wait.until(
    EC.text_to_be_present_in_element_value((By.ID, "query"), "Python")
)
print("✅ 검색어 입력 확인됨!")

driver.quit()
```

### 3. Timeout 예외 처리

```python
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

try:
    driver.get("https://www.naver.com")
    
    # 존재하지 않는 요소 찾기 시도
    element = wait.until(
        EC.presence_of_element_located((By.ID, "nonexistent-element"))
    )
    print("✅ 요소 찾음")
    
except TimeoutException:
    print("⏰ Timeout 발생: 5초 안에 요소를 못 찾음")
    print("→ 대체 동작 수행 가능")

finally:
    driver.quit()
```

### 4. 커스텀 Wait 조건 (Lambda)

```python
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

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
```

### 5. 재시도 로직을 포함한 헬퍼 함수

```python
from selenium.common.exceptions import TimeoutException
import time

def wait_for_element_with_retry(driver, by, value, timeout=10, retry_count=3):
    """
    요소를 찾을 때까지 재시도하는 헬퍼 함수
    """
    wait = WebDriverWait(driver, timeout)
    
    for attempt in range(retry_count):
        try:
            element = wait.until(
                EC.presence_of_element_located((by, value))
            )
            print(f"✅ 요소 찾음 (시도 {attempt + 1}회)")
            return element
        except TimeoutException:
            print(f"⏰ 시도 {attempt + 1}회 실패")
            if attempt == retry_count - 1:
                raise
            time.sleep(1)

# 사용 예시
driver = webdriver.Chrome()
driver.get("https://www.naver.com")

search_box = wait_for_element_with_retry(
    driver, By.ID, "query", timeout=5, retry_count=3
)

driver.quit()
```

---

## 🚀 네이버 자동완성 처리


```python
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
```

### 주요 학습 포인트

1. **CSS Selector 심화**
   ```python
   # attribute 선택자
   'ul[role="listbox"]'  # role 속성이 "listbox"인 ul
   
   # 자손 선택자
   '.kwd_lst .item .kwd_txt'  # .kwd_lst 안의 .item 안의 .kwd_txt
   
   # nth-child 선택자
   '.kwd_lst .item:nth-child(2)'  # 두 번째 항목
   ```

2. **Wait 전략**
   - 자동완성 컨테이너: `presence_of_element_located` (애니메이션 중에도 찾을 수 있음)
   - 자동완성 항목들: `visibility_of_all_elements_located` (실제로 보이는 항목만)
   - 클릭 버튼: `element_to_be_clickable` (클릭 가능할 때까지 대기)

3. **에러 처리**
   ```python
   try:
       # 메인 로직
   except TimeoutException:
       # Timeout 발생 시 처리
   except Exception as e:
       # 기타 예외 처리
   finally:
       # 항상 실행 (브라우저 종료)
   ```

---

## 📌 추가 학습: URL 디코딩

### 문제 상황

브라우저 URL에서 한글이나 특수문자는 **URL 인코딩**되어 표시됩니다:

```python
# 실제 브라우저 URL
https://search.naver.com/search.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 우리가 보고 싶은 형태
https://search.naver.com/search.naver?query=파이썬
```

### 해결 방법: urllib.parse 모듈

```python
from urllib.parse import unquote, quote

# 1. URL 디코딩 (인코딩된 → 한글)
encoded_url = "https://search.naver.com/search.naver?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
decoded_url = unquote(encoded_url)
print(decoded_url)  # https://search.naver.com/search.naver?query=파이썬

# 2. URL 인코딩 (한글 → 인코딩)
search_word = "파이썬"
encoded_word = quote(search_word)
print(encoded_word)  # %ED%8C%8C%EC%9D%B4%EC%8D%AC

# 3. Selenium에서 사용
current_url = driver.current_url
decoded_url = unquote(current_url)

if "파이썬" in decoded_url:
    print("✅ 검색어 확인!")
```

### URL 파라미터 파싱 (고급)

```python
from urllib.parse import urlparse, parse_qs

url = "https://search.naver.com/search.naver?where=nexearch&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC&sm=top"

# URL 파싱
parsed_url = urlparse(url)
print(f"도메인: {parsed_url.netloc}")  # search.naver.com
print(f"경로: {parsed_url.path}")      # /search.naver

# 파라미터 추출
params = parse_qs(parsed_url.query)
print(f"파라미터: {params}")
# {'where': ['nexearch'], 'query': ['파이썬'], 'sm': ['top']}

# 특정 파라미터 값 가져오기
search_query = params['query'][0]
print(f"검색어: {search_query}")  # 파이썬
```

---

## 🎓 Stage 3에서 배운 것

### 핵심 개념
1. **Implicit Wait** - 전역 대기 시간 설정
2. **Explicit Wait** - 특정 조건까지 명시적 대기
3. **Expected Conditions** - 자주 사용하는 대기 조건들
4. **presence vs visibility** - DOM 존재 vs 화면 표시의 차이
5. **Timeout 처리** - `TimeoutException`으로 예외 처리
6. **커스텀 Wait** - Lambda 함수로 복잡한 조건 만들기
7. **재시도 로직** - 요소를 찾을 때까지 반복 시도
8. **URL 디코딩** - `unquote()`로 한글 URL 처리

### 실전 스킬
- 동적으로 생성되는 요소 안전하게 처리
- 자동완성, 드롭다운 등 동적 UI 요소 다루기
- CSS Selector의 attribute, nth-child 사용
- 재사용 가능한 헬퍼 함수 작성
- 적절한 예외 처리로 안정적인 코드 작성

### 문제 해결 경험
1. **변수명 충돌** - `time` 모듈과 `time` 변수명 충돌 해결
2. **CSS Selector 공백** - `.item .class` vs `.item.class` 차이 이해
3. **visibility 실패** - 애니메이션 중 요소를 `presence`로 먼저 찾기 (DOM 체크부터)
4. **URL 인코딩** - 한글 검색어 URL 확인을 위한 디코딩

---


## 📂 프로젝트 구조

```
project3/
├── utils/
│   └── driver_setup.py      # 공통 드라이버 설정
├── ch1_implicit_wait.py      # Implicit Wait 실습
├── ch2_explicit_wait.py      # Explicit Wait 실습
├── ch3_timeout_handling.py   # Timeout 처리 실습
├── ch4_custom_conditions.py  # 커스텀 조건 실습
├── ch5_autocomplete.py       # 네이버 자동완성 프로젝트
└── README.md                 # 이 문서
```

---


</details>






