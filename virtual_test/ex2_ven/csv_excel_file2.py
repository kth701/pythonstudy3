# pandas 패키지 import
import pandas as pd
from statistics import mean
import os


# excel 파일 읽기
sam = pd.ExcelFile('./sam_kospi.xlsx')

# excel 파싱
kospi = sam.parse("sam_kospi")
print(kospi.info())

# 컬럼 추출
high = kospi['High']
low = kospi['Low']

# 평균 계산
print('high 평균: ', mean(high))
print('low 평균: ', mean(low))

print('high 평균: ', high.mean())
print('low 평균: ', low.mean())