# 리스트 내부 요소 정렬
list_a = [1,2,3,4,1,2,3,4]
print(list_a)

list_a.sort() # [1, 1, 2, 2, 3, 3, 4, 4]
print(list_a)

# 내림차순
list_a.sort(reverse=True) # [4, 4, 3, 3, 2, 2, 1, 1]
print(list_a)


# 리스트 요소 검사
import random
r = [] # 비어 있는 list
for i in range(5):
    # random.randint(1,5): 1-5사이 숫자 무작위 발생 리스트에 저장
    r.append(random.randint(1,5))

print(r)
if 4 in r:
    print('4 숫자 있음')
else:
    print('4 숫자 없음')

# 리스트 내부에 데이터 확인하기: in / not in
print( 10 in list_a)  # False:  10 있으면 True, 없으면 False
print( 1 in list_a)   # True
print( 5 not in list_a) # 해당 값이 없는지 확인

# 표준 함수: sorted()
numbers = [10,20,30, 100,1,2,3]
print(numbers)          # [10, 20, 30, 100, 1, 2, 3]
print(sorted(numbers))  # [1, 2, 3, 10, 20, 30, 100]
print(sorted(numbers, reverse=True)) # [100, 30, 20, 10, 3, 2, 1]

# 특정 기준으로 정렬
numbers2 = [1,-2,5, -10]
print(numbers2)
print(sorted(numbers2))

# 리스트를 절대치 전환 -> 오름차순 결과 -> 표시
# [1,-2,5, -10] -> [1,2,5,10]
print(sorted(numbers2, key=abs))




