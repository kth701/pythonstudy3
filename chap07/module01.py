# 파일 단위 : 모듈(함수와 클래스구성)

# 파이썬에서 제공하는 내장 클래스 : import 모듈 포함
# 1. import 모듈명
# 2. from 모듈명 import 클래스1,....

# import math as m
# print(m.sin(1), m.cos(1))

# from math import sin as s # sin 대신 s를 사용
# print(s(1)) # 모듈(클래스)명 생략

# print(cos(1)) # error


import random

print("-- random()")
for i in range(3):
    print(random.random())
print()    


print("-- uniform(min, max)")
for i in range(3):
    print(random.uniform(10,20))
print()    

print("-- randrange(min, max)")
for i in range(10):
    print(random.randrange(10), random.randrange(1,5))
print()    


