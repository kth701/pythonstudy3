# 중첩 예외처리

print('-- 시작')
try:
    div = 1000/2.53
    print('div=%5.2f' % (div))

    #div = 1000/0 # 1차 예외발생-> 산술적 예외
    #f = open('c:\\abc.txt') # 2차 예외발생 -> 파일 예외
    num = int(input('숫자입력:')) # 3차 

    print('num=', num)
except ZeroDivisionError as e:
    print('오류정보:',e)
except FileExistsError as e:
    print('오류정보:',e)
except Exception as e:
    print('오류정보:',e)
finally:
    print('무조건 수행')


print('-- 종료')