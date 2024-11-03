# set : 중복 불가, 인덱싱, 슬라이싱 사용 불가

nums = {1,2,3,1,2,3}
print(nums)
# print(nums[1]) # index에러 발생

print("-- 집합연산 : 기호연산")
set1 = {1,2,3,4,5}
set2 = {4,5,6}

print(set1, set2)
print(set1 | set2) # 합집합=> set1.union(set2)
print(set1 & set2) # 교집합=> set1.intersection(set2)
print(set1 - set2) # 합집합=> set1.difference(set2)

# None 타입
print("- None Type 확인하기")

dict_a = {}
dict_b = {"a":"100"}

print(dict_a, dict_b)

print(dict_a.get("a"), dict_b.get("a"))
if dict_a.get("a") is None: # None
    print("None Type: 데이터가 비어있는 상태")
else:
    print("Not None type: 데이터가 있음")

if dict_b.get("a") is not None: # None 아니면 수행
    print("Not None type: 데이터가 있음")
else:
    print("None Type: 데이터가 비어있는 상태")
    