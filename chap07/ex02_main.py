# 상위폴더(chap07)에서 하위폴더(chap07/ex02)에 있는 모듈을 
# import한 구조형식

# import ex02.module_a as a
# import ex02.module_b as b
# print(a.num_a, b.num_b )

# 특정 패키지(폴더)에 있는 모든 모듈 호출
from ex02 import *

print(module_a.num_a)
print(module_b.num_b)


