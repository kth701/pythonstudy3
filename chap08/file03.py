# os 모듈: 작업 디렉토리설정, 이동, 삭제, 생성 등...
import os
# 현재 작업 디렉토리 확인
path = os.getcwd()
print('현재 작업 폴더:',path)

# 작업 디렉토리 변경
# 'D:\python_study\pythonstudy3\chap08'
os.chdir('chap08') 
path = os.getcwd()
print('변경 후 현재 작업 폴더:',path)

os.chdir('..') # '.' 현재, '..' 상위폴더
path = os.getcwd()
print('변경 후 현재 작업 폴더:',path)

# 현재 폴더 목록
list_dir = os.listdir('.')
print(list_dir)

# 폴더 생성( 하나, 여러개)
os.mkdir('test')
list_dir = os.listdir('.')
print(list_dir)



