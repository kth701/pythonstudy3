# 반복문: 특정 부분을 반복해서 실행하는 명려문
# while(반복횟수가 명확하지 않을 때), for(반복횟수가 명확할 때)

# cnt += 숫자 : 숫자 카운터
# tot += 변수 : 변수들의 합(누적)
cnt = tot = 0 # 변수 초기화
while cnt < 5: #cnt가 5보다 작은 경우일 때만 반복 수행
    cnt += 1  # cnt = cnt + 1
    tot += cnt # 숫자를 누적(합계) # +1, +2,+3,+4,+5
    print(cnt, tot)



print("---")
# 1-100사이 3의 배수 합과 3의 배수 추출하기
cnt2 = 0
tot2 = 0
numList = []
while cnt2 < 100:
    cnt2 += 1
    # 3의 배수만 추출
    if cnt2%3 == 0:
        numList.append(cnt2) # list구조에 3의 배수만 추가
        tot2 += cnt2
        #print(cnt2)

print('1-100까지 3의 배수:',numList)
print('1-100까지 3의 배수이 합:', tot2)



