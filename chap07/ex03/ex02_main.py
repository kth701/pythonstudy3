# 에러 ex03에서 ex02모듈 호출이 안됨.
# 상위폴더(chap07)에서 하위폴더(chap07/ex02)에 있는 모듈을 
# import한 구조형식
import ex02.module_a as a
import ex02.module_b as b


print(a.num_a, b.num_b )