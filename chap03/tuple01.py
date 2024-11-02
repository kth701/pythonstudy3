# 튜플(tuple): 리스트구조유사, 수정,삭제가 불가 (읽기 전용)
# 인덱싱, 슬라이싱, 연결, 반복, 요소검사 등 가능
# 리스트보다 처리속도가 빠르다

t1 = (10,) # 튜플은 1개 원소만 설정 할 경우 콤마(,)있어야 한다.
temp = (10) # int 정수1개
print(t1,type(t1), temp, type(temp)) # (10,) <class 'tuple'> 10 <class 'int'>


t2 = (1,2,3,4,5,3)
print(t2)
print(t2[0], t2[:3], t2[1:4])

# t2[0] = 100 # 수정,삭제 불가
for i in t2:
    print(i, end=" ")
print()    
print( 100 in t2) # False
print( 1 in t2) # True

# 1. 튜플 자료형 변환
lst = list(range(1,5+1))
t3 = tuple(lst) # 리스트 구조 -> 튜플 구조
print(lst, t3)

# 튜플 함수
print(len(t3), type(t3))
t4 =(1,1,11,1,1,1,1,1,11)
print(t4.count(1)) # 튜플에 특정 데이터의 갯수
print(t4.count(11))
print(t4.index(11)) # 튜플에 특정 데이터의 위치(인덱스번호)

