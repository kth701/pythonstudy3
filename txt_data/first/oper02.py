
# 관계 연산자(>, >=,<,<=, !=, ==) 
# : 연산결과 Boolean값:True, False
print(5>2, 5>=2)
print(5<2, 5<=2, 5!=2, 5==2)

# 논리연산자(not, and, or)
print( not(5>2) )
# 이고, 중에서 
print( (5>2 and 5>3 and 5>4))
# 이거나 , 또는 
print( 5<2 or 5<3 or 5<4 )

print("-- 동시 대입")
v1, v2 = 100, 200
print(v1,v2)

print("--- 대입")
i = 100
print(i)

i = i + 1  # 100+1
print(i)

i = i + 1  # 101 + 1
print(i)

# 패킹(packing) 할당
# 리스트 => 여러개의 데이터를 보관하는 저장소
lst = [10,20,30,40,50]
print(lst)
print(lst[0], lst[1]) # 객체[인덱스번호]=> 0,1,... => 0~n-1

print("-- packing(): 여러개의 값을 묶어서 변수에 할당")
v1, *v2 = lst
print(v1, v2)

*v1, v2 = lst
print(v1, v2)
