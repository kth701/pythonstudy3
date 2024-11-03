# 함수(메서드): 
#  - 독립된 단위 프로그램
#  - 특정 기능을 수행하는 단위 프로그램   
# 내장함수와 사용자 정의 함수

# 파이썬 모듈: 다수의 함수나 클래스를 묶어서  파일 형식(*.py)으로 제공
# 파이썬 패키지: 비슷한 유형의 모듈이 많은 경우  폴더 형태로 묶어서 꾸러미로 제공

# import 모듈명: 패키지 또는 모듈이 포함고 있는  모든 구성요소를 포함
# from 모듈명 import 함수명1,...

# 내장함수 = builtins모듈

#import builtins
#print(dir(builtins))

# 1. builtins 모듈
print("- 1. builtins 모듈에 포함된 내장함수")
data = list(range(1,5+1))
print(data)

print('len=', len(data))
print('sum=', sum(data))
print('max=', max(data))
print('min=', min(data))

# 2. import 모듈
print("- 2. builtins 모듈외 모듈은 import로 호출")
# 1. 방법
#import statistics

#print('평균=', statistics.mean(data))
#print('중위수=', statistics.median(data))
#print('표본 분산=', statistics.variance(data))
#print('표본 표준편차=', statistics.stdev(data))

# 2. 방법
from statistics import variance, stdev,mean, median

print("- 2. from 모듈명 함수명: 모듈이름 생략하고 함수이름만 사용하여 호출")
print('평균=', mean(data))
print('중위수=', median(data))
print('표본 분산=', variance(data))
print('표본 표준편차=', stdev(data))


