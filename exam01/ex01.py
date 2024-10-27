# 문제1
# 처리조건
#수량 변수 : su = 5
#단가 변수 : dan = 800
#su, dan변수 주소 확인
#금액 계산 = 수량 * 단가

# 출력 예시
#su 주소: 142258886
#dan 주소: 65496783
#금액 = 400

print("1. 문제")
su = 5
dan = 800
price = su * dan

print('su 주소:', id(su), '데이터:',su)
print('dan 주소:', id(dan), '데이터:',dan)
print("-"*10)
print('금액 = ',price)


# 문제2
# 3개의 단어를 키보드로 입력받아서 각 단어의 첫글자 추출하여 
# 단어의 약자를 출력

# 처리 조건
# - 각 단어 변수(word1, word2, word3)저장
# - 입력과 출력 구분선 : 문자열 연산
# - 각 변수와 첫 단어만 추출하여 변수(abbr)저장


# 출력 예시
#첫번째 단어: Korean
#두번째 단어: Baseball
#세번째 단어: Orag
#===========
#약자: KBO

print("2. 문제")
word1 = input('첫번째 단어: ')
word2 = input('두번째 단어: ')
word3 = input('세번째 단어: ')
print(word1, word2, word3)
# 첫글자 추출해서 글자연결
abbr = word1[0] +word2[0] +word3[0]
print("="*15)
print("약자: "+abbr)
