# Selenium_Tutorial
<details>
   <summary>
      ## Selenium 1단계: 기초
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






