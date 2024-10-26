# 메모리(RAM): 프로그램 데이터 보관 장소
# 변수 : 단일 기억장소
# 상수 : 기억장소에 넣을 값(데이터)

# 대입(할당문) : 변수 = 데이터, 변수 = 변수, 변수 = 수식

var1 = "Hello Python!! 안녕 파이썬"
print(var1) # 콘솔창에 출력
print( id(var1) )

print("---")
var2 = 100
var3 = 150.25
var4 = True

print("var2=",var1)
print("var type: ", type(var2))
print(type(var2), type(var3), type(var4))


# 기본 자료형 : 
# 숫자형(정수,실수), 문자형(문자, 문자열), 논리형(True,Fals)

# 실수 -> 정수
a = 10.5
b = int(10.234) # 형변환
print(a,type(a), b, type(b))
# 정수 -> 실수
a1 = 10
b1 = float(20)
print( type(a1), type(b1))
# 논리형 -> 정수
# True: 0이 아닌 정수, False: 0
print(True, int(True))
print(False, int(False))

# 문자형 -> 정수
strtest = '100'
print(strtest, type(strtest), type(int(strtest))  )
print( int(strtest)+100)

# 문자열(string):'+'연산자=> 연결하기
str1 = "Hello"
str2 = 'python'
hello = "안녕'홍길동'님"
print(str1, str2, hello)
print("안녕 "+'홍길동'+str(10*2))
print("Hello \n\n\n Python!!!")

long_str = """\
first
second
하나
둘
셋\
"""
print(long_str)





