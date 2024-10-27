# 제어문: 프로그램의 흐름을 변경해 주고자 할 경우
# 조건에 따른 제어: if문
# if 조건식:
# [들여쓰기4칸]  처리할 내용1
# [들여쓰기4칸]  처리할 내용2...

num1 = 10
if num1>=5:
    print("조건이 참일 경우 처리하는 블록 구간")
    print('num1='+str(num1))

print('다음 제어문 실행')

print("--- datetime 모듈")
import datetime
# 현재 시스템 날짜/시간을 구함
now = datetime.datetime.now()

# 봄
if 3 <= now.month <= 5 :
    print("이번 달은 {}월로 봄입니다.".format(now.month))

# 여름
if 6<=now.month<=8:
    print("이번 달은 {}월로 여름입니다.".format(now.month))

# 가을
if 9<=now.month<=11:
    print("이번 달은 {}월로 가을입니다.".format(now.month))

# 겨울
if 12<=now.month<=2:
    print("이번 달은 {}월로 겨울입니다.".format(now.month))

print("-- if else")
if 9<=(now.month+3)<=11:
    print("이번 달은 {}월로 가을입니다.".format(now.month))
else:
    print("이번 달은 {}월로 가을이 아닙니다.".format(now.month))

print("---- 키보드로 입력받은 수가 짝수인지 홀수인지 판별") 
# input():키보드 -> string:문자열 -> int:숫자형
number1 = int(input("숫자:"))   
print(number1, type(number1))

# 모든 짝수 2로 나누어 떨어진다.=> 나머지가 0 => '%'연산자통해 처리
# '%'나머지 연산자로 통해서 나온 결과를 가자고 조건 처리
if number1%2 == 0:
    print("숫자 {}는 짝수입니다.".format(number1))
else :
    print("숫자 {}는 홀수입니다.".format(number1))

print("-- else if(중첩조건문)")    
number2 = 100
if number2>0:
    print('0보다 크다')
else:
    if number2==0:
        print('0이다')
    else:
        print('0보다 작다')

print("---")
score = int(input('점수 입력: '))
grade = ''  # 등급

# 조건식 : 85<= score <= 100
if score>=85 and score <= 100:
    grade = '우수'
elif score >= 70: # 나머지 조건에서 재조건
    grade = '보통'
elif score >= 60:
    grade = '미흡'
else:
    grade = '저조'
print("당신의 점수는 {}이고, 등급은 {}".format(score, grade))

# 삼항 조건문: 변수 = 참 if (조건문) else 거짓
number3 = 9
result = number3*2 if number3>=5 else number3+2
print(number3, result)

