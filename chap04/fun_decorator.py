
# 함수 장식자(decoration)
# 기존 함수의 시작부분과 종료부분에 기능을 장식해서 추가해주는 별도의 함수
# 형식: @데코레이터 선언후 def함수 선언


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