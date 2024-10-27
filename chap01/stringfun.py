
# 문자열: 인덱싱[2], 슬라이싱[0:n-1]
# 1. 특정 글자 수 반환
oneLine = "this is one line string"

print("'t'글자 수:", oneLine.count('t'))
# 2. 접두어 문자 비교 판단
print('특정문자로 시작하는 단어 포함여부:',oneLine.startswith('this')) # True/False => True
print(oneLine.startswith('that')) # False
# 3.문자열 교체
print('문자열교체:', oneLine.replace('this', 'that') )
print('문자열교체(제거):', oneLine.replace(' ', '') )
# 4. 문자열 분리(split): 문단 -> 문장
multiLine="""\
Tempor consectetur incididunt aliqua non tempor. 
Commodo eu dolor sit ut nostrud reprehenderit minim ad cillum amet enim id. 
Minim magna et deserunt ad.
"""
print('문장:\n'+multiLine)

# 특정 문자를 기준으로 분리해서 리스트구조로 저장
sent = multiLine.split('\n')   
print('분리된 문장:',sent)

# 문자열 결합(join): 던어 -> 문장
words = oneLine.split(' ')
print(words)
sent2 = ', '.join(words)
print('join()=> '+sent2)
print("-- 기타")

word1 = "Qui incididunt incididunt elit nulla mollit tempor culpa exercitation aliqua anim sint."
print(word1)
print(word1.upper()) # 대문자
print(word1.lower()) # 소문자
print(word1.swapcase()) # 대<->소
word2 = "   abcd    "
print(word2,'문자길이:', len(word2))
print(word2.strip(),'문자길이:', len(word2.strip()))

# isdigit(), islower(), isupper(),...
print("--- 판별: isXXXX()")
print("TrainA10".isalpha())
print("TrainA10".isdecimal())

print("-- find(), rfind()")
# 특정 문자가 있으면 문자의 인덱스번호
# "excelTest.xls"
str2 = "안녕a하세a요a".rfind("a") 
print(str2)
fileName = "excelTest.xls"
extPos = fileName.rfind('xls')
print(fileName,'=>확장자=>',fileName[10:])










# 대입문(할당문): 데이터(값)을 저장하는 것
# 대입연산자: 연산+할당
# +=, -=, *=,/=,....
num1 = 100
num1 = num1 + 10
print(num1)

num1 += 10 # 10을 추가
print(num1)

str = "홍"
str = str + "길" # 연결
print(str)
str += "동"
print(str)
