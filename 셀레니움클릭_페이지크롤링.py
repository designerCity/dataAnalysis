!pip install pandas
!pip install html_table_parser

from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser

from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver import ActionChains

# 첫 페이지 크롤링
import pandas as pd
from selenium.webdriver import ActionChains

result = urlopen(url)
html = result.read()
soup = BeautifulSoup(html,'html.parser')
a_tag = soup.findAll('a', href = True) 
# for i in a_tag:
#     print(i['href']) # 이 코드에서 살펴보고
# 페이지 이동 버튼만 추출
path = "/Users/kimsh/Downloads/chromedriver" # file 위치는 지정해줘야 한다.
driver = webdriver.Chrome(path)
url = "https://cps.or.kr/safe2/cps5sub1.jsp"
driver.get(url)

time.sleep(0.5)

# df = pd.DataFrame(sample,columns=['시설번호','시설명','설치장소', '주소', '상세'])
df = []
for j in range(1, 10): # 1 ~ 10 까지 페이지 넘기기
    ele = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[2]/div/table[5]/tbody/tr/td/a['+ str(j)+']')
    actions = ActionChains(driver)
    actions.move_to_element(ele)
    actions.click(on_element=ele)
    actions.perform()
    
    
    # 표 크롤링
    table = driver.find_element_by_class_name('table')
    tbody = table.find_element_by_tag_name("tbody")
    for i in range(10):
        rows = tbody.find_elements_by_tag_name("tr")[i] # 해당 row 들
        li = []
        for j in range(5):
            # body 는 셀레니움 리스트인 것 같다.
            body= rows.find_elements_by_tag_name("td")[j]      # row 에 해당하는 요소들
#             print(body.text)
            li.append(body.text)
#         print(li)
        df.append(li)
    
    
    
# 표 크롤링 데이터를 데이터 프레임으로 바꾸기
df = pd.DataFrame(df,columns=['시설번호','시설명','설치장소', '주소', '상세'])
df  




# 두 번째 셀
from selenium.webdriver import ActionChains

url = "https://cps.or.kr/safe2/cps5sub1.jsp"

# 페이지 이동 버튼만 추출
path = "/Users/kimsh/Downloads/chromedriver" # file 위치는 지정해줘야 한다.
driver = webdriver.Chrome(path)
driver.get(url)


df = []
# 다음 페이지로 넘어가게끔 (그래야 index 가 맞는다.)
ele = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[2]/div/table[5]/tbody/tr/td/a[10]')
actions = ActionChains(driver)
actions.move_to_element(ele)
actions.click(on_element=ele)
actions.perform()
for i in range(2): # 10 단위로 다음 페이지로 넘어가게끔 # range 안의 숫자는 10단위로 넘어가는 것
    time.sleep(0.5)
#     '/html/body/div.body/div.main/div.container/div.row/div.col-md-9/div.row/div.col-md-12/table/tbody/a[1]'
    for j in range(3, 13): # 10(i-1) + 1~10 까지
        ele = driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[2]/div/table[5]/tbody/tr/td/a['+ str(j)+']')

        actions = ActionChains(driver)
        actions.move_to_element(ele)
        actions.click(on_element=ele)
        actions.perform()
        
        # 표 크롤링
        table = driver.find_element_by_class_name('table')
        tbody = table.find_element_by_tag_name("tbody")
        for i in range(10):
            rows = tbody.find_elements_by_tag_name("tr")[i] # 해당 row 들
            li = []
            for j in range(5):
                # body 는 셀레니움 리스트인 것 같다.
                body= rows.find_elements_by_tag_name("td")[j]      # row 에 해당하는 요소들
    #             print(body.text)
                li.append(body.text)
    #         print(li)
            df.append(li)

    
    
# 표 크롤링 데이터를 데이터 프레임으로 바꾸기
df = pd.DataFrame(df,columns=['시설번호','시설명','설치장소', '주소', '상세'])
df  

