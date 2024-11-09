
# 함수 장식자(decoration)
# 기존 함수의 시작부분과 종료부분에 기능을 장식해서 추가해주는 별도의 함수
# 형식: @데코레이터 선언후 def함수 선언

print("----")
def func_with_print(f): # f는 double()함수가 전달
    def new_func(x):
        print("***")
        y = f(x)  # double(x)함수가 호출
        print(y)

        return y
    
    # return하면 new_func(5)=>double(5) 인식하여 실행
    return new_func 

@func_with_print
def double(x):
    return x*2

double(5)



print("----")
# 2.
def deco(f): # hi() 함수전달

    def new_f():
        print("f() is called")

        #return f    # hi()함수 반환 
        return  f()  # hi()함수실행 반환값이 리턴

    # return하면 new_f() 인식하여 실행  
    return new_f

@deco
def hi():
    print("하하하하하...")

hi()

print("-----")
def deco2(f2): # hi() 함수전달

    def new_f2():
        print("f2() is called")
        return  f2()  # hi()함수실행 반환값이 리턴
        
    return new_f2

def hi2():
    print("하하하하하2...")

hi_result = deco2(hi2) # new_f2()함수를 반환
hi_result()



print("----")





# 1. 래퍼 함수
def my_wrap(fun): #  함수식을 넘겨받음
    def my_decorated():
        print('반가워요!!!')

        fun()   # 함수 호출(실행)
        
        print('잘가요!!!')

    return my_decorated #함수식을 반환

# 2. 함수 장식자 적용
@my_wrap # 래퍼함수 
def hello():
    print('Hi~~~~','홍길동')

# 3.  함수 호출
hello()
