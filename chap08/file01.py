# 텍스트 파일 대상을로 텍스트 자료를 읽기/쓰기
# 형식) open(file, mode:(r,w,x,a,b), encoding )

# 현재 작업디렉토리(폴더)
import os
print('현재경로 : ', os.getcwd())

# 파일처리, 네트워크 등 입출력관련 예외처리
try:
    # 파일 읽기
    ftest1 = open('chap01/oper011.py', mode='r', encoding='utf-8')
    print(ftest1.read()) # 파일 전체 읽기

    # 파일 쓰기
    ftest2 = open('chap08/ftest2.txt', mode='w', encoding='utf-8')
    ftest2.write('my first text ~~~')

    # 파일 쓰기 + 추가
    ftest3 = open('chap08/ftest3.txt', mode='a', encoding='utf-8')
    ftest3.write('my second text !!!')


except Exception as e:
    print('Error 발생:',e)
finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()

print('정상 종료')