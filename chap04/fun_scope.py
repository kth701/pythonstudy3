# 스코프(scope): 지역변수, 전역변수

# 1. 지역변수

# 함수밖에서 선언 : 전역변수
x = 50  
def local_func(x): # 지역변수
    x += 50
    print('지역변수x=',x)

local_func(x)
print('전역변수x=',x)

# 2. 전역변수
def global_func():
    global x # 전역변수를 사용하겠다
    x+=50

global_func()
print('x=',x)

def locale_test():
    #x = 1
    print(x) #전역변수

locale_test()    

