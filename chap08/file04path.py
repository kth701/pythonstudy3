# 경로 관련 함수
import os.path

print("- ", os.getcwd())
os.chdir('chap08')
print('- ', os.getcwd())

# 절대 경로
print('- ', os.path.abspath('./data'))
# 파일의 폴더 위치
print('- ', os.path.dirname('data/test_data.txt'))

# 폴더 유무 학인
print('- ', os.path.exists('./data'))
print('- ', os.path.exists('./data2'))

# 파일인지 판별
print('- 파일인지 판별(file01.py):',os.path.isfile('file01.py'))
print('- 파일인지 판별(./data):',os.path.isfile('data'))
# 디렉토리인 판별
print('- 디렉토리인지 판별(file01.py):',os.path.isdir('file01.py'))
print('- 디렉토리인지 판별(./data):',os.path.isdir('data'))
# 디렉토리분리
list_path = os.path.split('./data/test_data.txt')
print("- path분리:",list_path)
# 디렉토리 결합
join_path = os.path.join('./data','test_data.txt')
print("- join:",join_path )
# 파일 크기
file_size = os.path.getsize('./data/test_data.txt')
print('- 파일 크기:',file_size)


