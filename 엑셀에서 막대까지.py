import numpy as np

import pandas as pd

#df_test.xlsx 파일을 dataframe으로 변경
df = pd.read_excel("./Downloads/설문지 결과1.xlsx", engine = "openpyxl")

print(df.head())

# 전처리
df_1 = df.drop([df.columns[0].strip(), df.columns[1]], axis=1)
df_1

# 특정 열에 결측치가 있다면, 햐덩 열 제거
q = '1. 알고 계신다면 귀하의 mbti는 무엇입니까?'

len(df_1.dropna(subset=[q],axis=0)) # 42
df_1.dropna(subset=[q],axis=0)

## E vs I

q = '1. 알고 계신다면 귀하의 mbti는 무엇입니까?'

df_e = df_1[(df_1[q].str[0] == 'E')]
df_i = df_1[(df_1[q].str[0] == 'I')]

print(len(df_e))
print(len(df_i))

q = '2. 귀하는 놀러갈 때 사람이 적고 조용한 곳을 선호하시나요? 사람들이 많고 시끌벅적한 곳을 선호하시나요?'
df_e

# df_e[q].value_count().plot.bar(rot=0)
df_e[(df_1[q].str[2] == '들')]  
len(df_e[(df_1[q].str[2] == '들')]) # 14
df_e[(df_1[q].str[2] != '들')]
len(df_e[(df_1[q].str[2] != '들')]) # 9
df_e.describe()

q = '2. 귀하는 놀러갈 때 사람이 적고 조용한 곳을 선호하시나요? 사람들이 많고 시끌벅적한 곳을 선호하시나요?'
cnt_i = df.groupby(q)[q].count()
color = ['yellow', 'red']
cnt_i.plot.bar(alpha = 0.5, color= color, rot = 0, title = '전체의 선호도')

## E 의 선호도

q = '2. 귀하는 놀러갈 때 사람이 적고 조용한 곳을 선호하시나요? 사람들이 많고 시끌벅적한 곳을 선호하시나요?'
cnt_i = df_e.groupby(q)[q].count()
color = ['yellow', 'red']
cnt_i.plot.bar(alpha = 0.5, color= color, rot = 0, title = 'E 의 선호도')

df_i
df_i.describe()

len(df_i[(df_1[q].str[2] == '들')]) # 4 
len(df_i[(df_1[q].str[2] != '들')]) # 15

## 한글 깨짐 방지 코드

from matplotlib import rc  ### 이 줄과
rc('font', family='AppleGothic') 			## 이 두 줄을 
plt.rcParams['axes.unicode_minus'] = False  ## 추가해줍니다. 

## I 의 선호도

import matplotlib.pyplot as plt
q = '2. 귀하는 놀러갈 때 사람이 적고 조용한 곳을 선호하시나요? 사람들이 많고 시끌벅적한 곳을 선호하시나요?'
cnt_i = df_i.groupby(q)[q].count()
color = ['yellow', 'red']
cnt_i.plot.bar(alpha = 0.5, color= color, rot = 0, title = 'I 의 선호도')
