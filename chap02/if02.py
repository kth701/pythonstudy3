
# 숫자를 입력하면 그숫자가 2,3,4,5로 나누어 떨어지는지 
# 확인하고 출력하는 프로그램 구현하시오.

#정수를 입력해주세요? 273
#273은 2로 나누어 떨어지는 숫자가 아닙니다.
#273은 3로 나누어 떨어지는 숫자입니다.
#273은 4로 나누어 떨어지는 숫자가 아닙니다.
#273은 5로 나누어 떨어지는 숫자가 아닙니다.

print("-- 2,3,4,5나누어 떨어지는 숫자인지 판별하기")
inputNum = int(input('정수를 입력해주세요: '))

if inputNum%2 == 0:
    print(f"{inputNum}은 2로 나누어 떨어지는 숫자 입니다.")
else:
    print(f"{inputNum}은 2로 나누어 떨어지는 숫자가 입니다.")

if inputNum%3 == 0:
    print(f"{inputNum}은 3로 나누어 떨어지는 숫자 입니다.")
else:
    print(f"{inputNum}은 3로 나누어 떨어지는 숫자가 입니다.")

if inputNum%4 == 0:
    print(f"{inputNum}은 4로 나누어 떨어지는 숫자 입니다.")
else:
    print(f"{inputNum}은 4로 나누어 떨어지는 숫자가 입니다.")

if inputNum%5 == 0:
    print(f"{inputNum}은 5로 나누어 떨어지는 숫자 입니다.")
else:
    print(f"{inputNum}은 5로 나누어 떨어지는 숫자가 입니다.")    