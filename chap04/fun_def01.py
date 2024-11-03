# 사용자 정의함수
# def 함수명(매개변수):
# [칸들여쓰기]수행할 내용1
# [칸들여쓰기]수행할 내용1
#            return 반환값

# 1. 인수(자)가 없는 함수
def userFunc():
    print("인자가 없는 함수")
    print('나는 인자 없는 userFunc()함수')


# 함수호출(실행): 함수이름()
userFunc()

# 2. 인자가 있는 함수
def userFunc2(x,y):
    print('userFunc2() 실행중')
    z = x+y
    print('z=', z)

userFunc2(10,20) # 인자를 전달

# 3. 인자 있고, return (반환)값
#def userFunc3(x,y):
#    return add, sub, mul, div
def userFunc3(x,y):
    print('userFunc3()')
    
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return add, sub, mul, div

# 인자값 생성 : 키보드
x = int(input('x입력:'))
y = int(input('y입력:'))

add1, sub1, mul1, div1 = userFunc3(x, y)
print(add1, sub1, mul1, div1)



