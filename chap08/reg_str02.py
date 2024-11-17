# 문자열 검사

from re import match

# 패턴가 일치여부
jumin = '123456-9234567'
result = match('[0-9]{6}-[1-4][0-9]{6}',jumin)


if result:
    print('주민번호 일치')
else:
    print('잘못된 주민번호')

# 문자열 치환
from re import sub
st3 = 'test^홍길동 abc 대한*민국 123$tbc'    

# 특수문자 제거
text1 = sub('[\^*$]+','', st3)

print(st3)
print("-"*50)
print(text1)

text2 = sub('[0-9]','', text1)
print(text2)