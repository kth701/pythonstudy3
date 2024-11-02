# 비순서 자료구조: set, dict
# set : 중복을 허용하지 않는다, 순서를 보장하지 않는 다
# 인덱스번호 없음

s1 = {1,3,5,3,1}
print(s1, len(s1))
# print(s1[0]) # index 사용 불가

for i in s1:
    print(i, end=" ")

print()
# set: 집합관련 함수
s2 = {3, 6}
print(s1, s2) # {1, 3, 5} {3, 6}

print(s1.union(s2)) #합집합       {1, 3, 5, 6}
print(s1.difference(s2)) #차집합  {1, 5}
print(s1.intersection(s2))#교집합 {3}

s3 = {1,3,5}

s3.add(7) # 요소 추가
print(s3) # {1, 3, 5, 7}

s3.discard(3) # 요소 삭제
print(s3) # {1, 5, 7}

# 중복 제거
gender = ['남','여','남','여']
print(gender)

sgender = set(gender) # list -> set
gender = list(sgender) # set -> list
print(gender, sgender)



