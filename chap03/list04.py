# 리스트 내포
# list안에 for와 if를 사용하는 형식
# 형식) 변수 = [실행문 for문 변수 in 열거형객체]
# 형식) 변수 = [실행문 for문 변수 in 열거형객체 if 조건식]

x = [2,4,1,5,7]
lst = [ i**2 for i in x]
print(x,lst) # [2, 4, 1, 5, 7] [4, 16, 1, 25, 49]

# 동일한 구조
# lst1 = []
# for i in x:
#     lst1.append(i**2)
# print(lst1)

# 1-10 -> 2의 배수 추출 -> list저장
num = list(range(1,10+1)) # 시작번호, 마지막번호-1
lst2 = [ i*2 for i in num if i%2 == 0]
print(lst2)

