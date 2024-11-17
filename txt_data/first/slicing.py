# 문자열 처리 : 슬라이싱(slicing)
oneLine = "this is one line string"
print(oneLine, len(oneLine))
# 문자열[시작인덱스번호:끝색인번호(n-1):증감값]
# 1. 왼쪽 기준 -> 인덱스번호가 양수
print(oneLine[0:4])
print(oneLine[:4])
print(oneLine[:]) # 전체 원소(요소)
print(oneLine[::2]) # 2의 배수 인덱스

# 2. 오른쪽 기준
print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])

# 3. 부분 문자열 생성
substr = oneLine[-11:]
print(substr)

# 문자열 역순
name = "PYTHON"
print("[012345]")
print( "["  +  name + "]")

print(name[0], name[1])
print(name[-1],name[-2])

print("-"*10)
# str(10): 10 -> "10"
print("홍길동"+ str(10*2) +"입니다.")

print("홍길동\nHongGilDong")
print("홍길동\tHongGilDong")
print("홍길동\\HongGilDong")
print("홍길동\'HongGilDong")

print("-"*10)
#num = input('숫자입력:')
#num = int(num) # 형전환 : string -> int
#print(num*2, type(num)) # print("100"*2)


print("---")
num2 = float(  input("숫자입력:")  )
print(num2, num2*2)

