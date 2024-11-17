# for 변수 in 열거형 객체:
#       반복처리할 내용...

#  문자열 열거형 객체
char1 = "홍길동홍길순"
for c in char1:
    print(c)

lst = [1,2,100,200, 1000,2000, "홍길동", "동순이"]
for data in lst:
    print('원소:', data)

print("-- range: 숫자 발생")    
num1 = range(3)
print('1. range(3):', num1)
# for n in num1:
#     print(n)
for n in range(3):# 0,1,2 반복수행하는 형식
    print('안녕하세요')

print('2. range(시작번호,n-1)')
for n in range(1,5):
    #print(n, end='\n') # print(n)
    print(n, end=' ')

print('\n3. range(시작번호,n-1, 증감)')
for n in range(1, 10, 2):
    print(n, end=' ')

print("-- continue")
for n in range(1,100+1):
    print(n, end=",")

    if n == 10:
        break # 제어문 완전히 빠져나옴

print("\n--  break")   
for n in range(1,10+1):
    if n%3 == 0:
        continue # 다음 제어문으로 이동

    print(n, end=",")

print()
print("-- random모듈 : random(), randint(a,b),....")

# 난수 : import random모듈 호출
import random


# random.random() : 0<n<1사이 숫자 발생
for i in range(1,10+1):
    rnd = random.random()
    print(i, rnd, rnd*10, int(rnd*10), int(rnd*10)+1)
print("---")
for i in range(1, 5+1):
    rnd = random.randint(0,3) #0~3사이 난수(정수) 발생
    print(rnd)

print("-- randint(시작정수,마지막정수) 예시")  
names = ["홍길동","홍길순","동길이","동길이홍","김길순","박길동"]
for name in names:
    print(name, end=" ")

print("")    
print("----------")
for i in range(1,5+1): # 5번 반복
    idx = random.randint(0,5) # 0에서 5사이 숫자
    print(idx, names[idx])


