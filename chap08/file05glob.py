# glob 모듈: 유닉스(Unix쉘이사용한 규칙에 의해서 지정된 패턴과 일치하는 
# 모든 파일과 디렉터리의 목록을 반환하는 관련 함수를 제공하는 모듈
# 특수문자(*,?,[])

import glob
import os.path

print("- ", os.getcwd())
os.chdir('chap08')
print(os.getcwd())

print("--")
print(glob.glob('*.py'))

print("--")
print(glob.glob('file[0-9]/*.py')) # 정규식 패턴
