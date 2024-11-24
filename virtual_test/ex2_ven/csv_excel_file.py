
# pandas 패키지 import
import pandas as pd
import os


print("-----")
print(os.getcwd())


# csv 파일읽기
score = pd.read_csv("./score.csv")
print(score.info()) # 파일 정보
print(score.head()) # 컬럼명 포함 앞부분 5개 행

# 컬럼 추출
print("-------")

kor=score.kor
mat=score.mat
eng=score.eng
dept=score.dept

#print('kor=>',score.kor)
#print('mat=>',score['eng'])
#print('mat=>',score['mat'])
#print('dept=>',score['dept'])

# 과목별 최고 점수
print("-- 과목별 최고 점수")
print('max kor={}'.format(max(kor)))

# 과목별 최저 점수
print("--- 과목별 최저 점수")
print('min kor={}'.format(min(kor)))

# 과목별 평균 점수

from statistics import mean
print("--- 과목별 평균 점수")
print('avg kor={}'.format( mean(kor) ))

# dept 빈도수
print("--- 빈도수")
dept_count = {} # 딕셔너리 { key, value} 저장하는 자료구조
for key in dept:
    dept_count[key] = dept_count.get(key, 0) + 1
print(dept_count)    