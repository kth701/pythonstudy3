# 문장과 단어 추출 예
string="""나는 홍길동 입니다.
주소는 부산시 입니다.
나이는 10세 입니다.
성별 남자 입니다."""
#print(string)

sents = [] # 문장 저장
words = [] # 단어 저장

#test = string.split(sep='\n')
#print(test)
#test2 = string.split(sep=' ')
#print(test2)

# 1. 문단 -> 문장
for sen in string.split(sep='\n'):
    sents.append(sen)
    # 2. 문장 -> 단어
    for word in sen.split(' '):
        words.append(word)

print('문장:', sents)
print('문장수:', len(sents))
print('단어:', words)
print('단어수:', len(words))


