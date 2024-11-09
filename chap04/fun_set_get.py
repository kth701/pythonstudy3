# 획득자(getter),지정자(setter), nonlocal
# nonlocal: 내부 함수에서 외부함수의 변수를 사용할 경우

# 1. 중첩 함수
def main_func(num):#outer function
    num_val = num  

    # inner function
    def getter(): # 획득자함, return 있음
        return num_val
    
    def setter(value):
        nonlocal num_val # 외부함수에 있는 변수를 의미 선언문
        num_val = value
    
    return getter, setter   # 함수 클로저 반환

# 외부 함수 호출
getter, setter = main_func(100)
print('getter():', getter())

setter(3000)
print('getter():', getter())


