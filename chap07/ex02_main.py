# 상위폴더(chap07)에서 하위폴더(chap07/ex02)에 있는 모듈을 
# import한 구조형식

# 1. 호출방식
# import ex02.module_a as a
# import ex02.module_b as b
# print(a.num_a, b.num_b )


# 2. 호출 방식
# 특정 패키지(폴더)에 있는 모든 모듈 호출
#  - "__init__.py" 파일있는 
#  - 폴더는 python에서 패키지로 인식시켜줘야 사용할 수 있음
from ex02 import *

print(module_a.num_a)
print(module_b.num_b)


