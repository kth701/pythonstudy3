
# 재귀함수(Recursive function)
# - 함수 내부에서 자신의 함수를 반복적으로 호출


# 재귀함수

# 3. 5! (5x4x3x2x1)
def  Factorial(n):
    if n==1: # 종료 조건
        return 1
    else:
        return n*Factorial(n-1)
        # 5*Factorial(4)->4*Factorial(3)->... 2*Factorial(1)
        
print('Factorial(5):', Factorial(3))
print("----")


# 2. sum()
def Adder(n):
    if n==1:
        return 1
    else:
        return  n + Adder(n-1) # 재귀호출
    
print('Addr(n)=', Adder(100))



# 1.
def counter(n):
     print(n)
     
     if n==0:
          return 0
     else:
        return counter(n-1) 
        # counter(2) -> counter(1) -> counter(0)

counter(3)