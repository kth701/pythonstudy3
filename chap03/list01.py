# 자료구조 :  데이터(객체)가 메모리에 배정될 때 
# 기억공간에 적재되는 구조

# 순서 자료구조(순서): 리스트 구조,스트링(문자열), 튜플(tuple)
# 비순서 구조(순서없음): 딕셔너리


# 1. str 클래스
print("-- 선형구조: string")
str1 = str(object='안녕하세요 string입니다.')
print(str1, type(str1))
print(str1[0],str1[2], str1[-1])

print("-- 리스트 구조")
print("1. 단일 리스트")

lst = [1,2,3,4,5,6,7,8,9,10]
# print(lst, type(lst))

# for i in lst: # 1, 2, 3, 4, 5
#     print(lst[:i]) # i전까지

print(lst[:5]) # [시작인덱스번호:마지막인덱스번호-1]
print(lst[-5:]) # [6, 7, 8, 9, 10]
print(lst[::2]) # [1, 3, 5, 7, 9]

print("2. 리스트 연산(+)")
lst1 = [10,20,30]
lst2 = ["홍길동","동길이","동순이"]
lst_sum = lst1 + lst2
# test = [1,2,3] +100 # 타입 에러
print(lst1, lst2, lst_sum)






