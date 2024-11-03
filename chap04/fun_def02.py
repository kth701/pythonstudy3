# 사용자 정의 함수: 산포도 구하기

from statistics import mean, variance
from math import sqrt

dataset = [2,4,5,6,1,8]
# 1. 산술평균
def Avg(data):
    avg = mean(data) # 평균
    return avg

print('dataset=', dataset)
print('산술평균=', Avg(dataset))

# 2. 분산/표준편차
def var_sd(data):
    # 산술평균함수 실행(호출)
    avg = Avg(data) 
    # list 내포
    diff = [ (d-avg)**2 for d in data]
    
    var = sum(diff)/(len(data)-1)
    sd = sqrt(var)

    return var,sd

# 함수 호출
v, s = var_sd(dataset)
print('분산=', v)
print('표준편차=',s)

print("-- 피타고라스 정리")
# 인자 있고, 반환 값 없는 형식
def pytha(s,t):
    a = s**2 - t**2
    b = 2*s*t
    c = s**2 + t**2
    print("3변의 길이: ", a,b,c)

pytha(2,1)


