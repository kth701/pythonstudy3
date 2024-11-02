# 리스트 메서드

print("1. 추가: append(), insert()")
num = ['one','two', 'three', 'four']
print(num,"개수:", len(num))

# 리스트 원소 추가: 마지막 요소 뒤에 추가
num.append('five') # [1, 3, 5, 7, 9]
print(num)

# 특정 위치(인덱스번호)에 추가
num.insert(0, 'zero') # ['zero', 'one', 'two', 'three', 'four', 'five']
print(num)

num.insert(3, 'test') # ['zero', 'one', 'two', 'test', 'three', 'four', 'five']
print(num)

# 삭제
num.remove('test') # ['zero', 'one', 'two', 'three', 'four', 'five']
print(num)

# 수정
num[0] = 0  # [0, 'one', 'two', 'three', 'four', 'five']
print(num)

# 새로운 리스트를 추가=> 리스트 확장
lst_str = ['서울시', '부산시', '대전시']
num.extend(lst_str) # extedn유사 기능 : 리스트+리스트
print(num)

print("-- 리스트 연사자 : +, *")
lst_num = [1,2,3]
result = lst_num * 3
print(lst_num, result)# [1, 2, 3, 1, 2, 3, 1, 2, 3]

print("- 전체 삭제")

lst_num2 = [100,200,300]
print(lst_num2)

lst_num2.clear() # []
print(lst_num2)



