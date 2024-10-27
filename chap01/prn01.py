# 표준입력(키보드)출력(모니터)장치
# print(value)

print("-- 출력 형식: %d,%o,%x,%f,  %s,%c")
print("원주율=", format( 3.14159, "8.3f" ) )
print("금액=", format(10000,"10d"))
print("금액=", format(125000, "3,d") )

print("--")
name = "홍길동"
age = 15
price = 125.456
# 1. 형식
print("당신의 이름은 %s입니다. 나이는` %d세, 가진 돈은 %.2f원입니다." 
      % (name, age, price) )
# 2. 형식
print("--")
print("당신의 이름은 {}입니다. 나이는 {}세, 가진 돈은 {}원입니다.".format(name,age,price))
print("당신의 이름은 {2}입니다. 나이는 {0}세, 가진 돈은 {1}원입니다.".format(name,age,price))
print("--")
str = f"당신의 이름은 {name}입니다. 나이는 {age}세, 가진 돈은 {price}원입니다."
print(str)



print("---------")
# value
print(100,200,300)

# print(value, sep, end , file, flush)
# sep(구분자)
print("010","1234","5678", sep="-")
# end
print("value=", 10, end=", ") # 생략시: end="\n"
print("value=", 20)



