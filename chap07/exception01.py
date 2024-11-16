# 예외 처리

print('-- 시작')
x = [10,30,25.2, 'num', 14, 51]
print(x)

for i in x:

    try:
        print(i)
        y= i**2 # 예외가 발생
    except: 
        print('숫자가 아님:',i)

print('-- 종료')