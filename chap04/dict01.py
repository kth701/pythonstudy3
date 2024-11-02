# 비선형 구조: <키,값> 형식 쌍으로 보관
# 형식 : 변수 = {'key':'값', ....}

dic = dict(a=100,b=200,c=300)
print(dic)

person = {'name':'홍길동', 'age':10,'address':'서울시'}
print(person)

print(person['name'], person['age'], person['address'])

person['age'] = 15 # 키로 통해 원소 수정
print(person)

del person['address'] # 키로 통해 원소 삭제
print(person)

person['pay'] = 350 # 없는 키 사용시 추가
print(person)

# 요소 검사
print( 'age' in person) # True
if 'age' in person: # True
    print(person['age'])

# 딕셔너리 -> 키만, 값만
print("- 1. keys(): 키만 추출")
for key in person.keys():
    print(key, end=' ')
print()   
print("- 2. values(): 값만 추출")
for value in person.values():
    print(value, end=' ') 
print()
print("- 3. items(): 키와값 모두 추출")
for item in person.items():
    print(item, end = ' ')
print()




