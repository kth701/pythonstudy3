# 가변인자 함수(인자의 개수가 고정된 개수가 아님)
# "*":튜플 또는 "**": 딕셔너리

# 형식: def 함수명(매개변수, *매개변수, **매개변수):

# 튜플형 가변인자
def Func1(name, *names):
    print(name)
    print(names)

Func1("홍길동", "홍길순","동순이", "김길동")

# 딕셔너리 가변인자
def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)

# 함수 호출
emp_func("홍길동", 10, addr='부산시',height=175)

# 튜플 가인자 예
from statistics import mean, variance, stdev
def statis(func, *data):
    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std':
        return stdev(data)
    else:
        return 'TypeError'
    
# statis 함수 호출
print('avg=', statis('avg',1,2,3,4,5))
print('var=', statis('var',1,2,3))
print('std=', statis('std',1,2,3,4))
print('abc=', statis('abc',1,2,3,4,5,6))

# 람다 함수: 익명함수
# 1. 일반함수
def Adder(x,y):
    #add = x + y
    #return add
    return x+y
print('add=', Adder(10,20))

# 2.람다함수
print('add=', (lambda x,y: x+y )(10,20) )



    