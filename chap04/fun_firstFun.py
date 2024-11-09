# 중첩함수 : 외부함수와 내부함수 구조
# 함수 클로저:내부함수는 외부함수의 return명령문을 이용하여 반환하는 형태
# - 외부함수가 종료되어도 내부함수에서 선언된 변수가 메모리에서 소멸되지 않은 상태로 내부함수를 활용

print("----")

# 2. 함수 클로저
data = list(range(1,10+1))

def outer_func(data):
    dataSet = data
    
    #inner
    def tot():
        #tot_val tot()함수안에 있는 변수
        tot_val = sum(dataSet)
        return tot_val

    def avg(tot_val):
        #tot_val, avg_val avg()함수안에 있는 변수
        avg_val = tot_val/len(dataSet)
        return avg_val

    return tot, avg # 내부함수이름을 반환

# outer_func() 수행결과는 함수(식)를 넘겨받음
total, average = outer_func(data) 
t = total() # 함수를 호출
a = average(t) # 함수를  호출
print(data, t, a)
 
    



print("----")
#  1. 일급함수
def a() : 
    # outer
    print('a()함수')
    temp = 100

    def b(): #inner
        print('a()함수안에 있는 b()')

    # outer
    return b

# 변수 = 값 ==> 변수에 있는 값
# 변수 = 함수식 => 함수형변수 => 함수를 수행하는 형태
# a()함수호출 => 실행
rs1 = a() 
rs1() #  b() => rs1()




    
    

