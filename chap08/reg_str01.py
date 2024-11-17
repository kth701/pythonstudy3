# 정규 표현식(Regular Expression): 특정한 규칙을 가진 문자열의 집합을 표현
# 메타문자를 이용해서 패턴 규칙 사용

#import re
# re.finall()형식을 호출: 모듈명이 포함되어야함.
from re import findall

st1 = '1234 abc홍길동 ABC_555_6 이사도시'

# 숫자 찾기
print(findall('1234',st1))
print(findall('[0-9]',st1)) #숫자 한자리 추출
print(findall('[0-9]{3}',st1)) #숫자 세자리 추출
print(findall('[0-9]{3,}',st1))
print(findall('\\d{3,}',st1))

# 문자열 찾기
print(findall('[가-힣]',st1)) # 한글 한자씩
print(findall('[가-힣]{3}',st1)) # 한글 세자씩
print(findall('[a-z]{3}',st1))
print(findall('[a-z|A-Z]{3}',st1))
print(findall('[a-zA-Z]{3}',st1))

# 특정 위치의 문자열 찾기
st2 = 'test1abcABC abst 123mbc 45test'

# 접두어/접미어
print(findall('^test',st2))
print(findall('st$',st2))

print(findall('.bc',st2))
print(findall('t.',st2))

st3 = 'test^홍길동 abc 대한*민국 123$tbc'
words = findall('\\w{3,}',st3)
print(words)

# 문자열 제외
print(findall('[^^*$]+',st3))
