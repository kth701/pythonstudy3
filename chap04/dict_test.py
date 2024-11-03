

# 딕셔너리 : (key,value)=> 추출, 수정, 추가
d1 = {}
print(d1, type(d1))
# 없는 키에 데이터 설정 => 추가
d1["apple"] = 3000

print(d1)
# 수정 : 키가 있을 경우
d1["apple"] = 5000
print(d1)

# 키로 통해 값(데이터) 불러오기
print(d1['apple'], d1.get('apple'))

d2 = {} # 비어있는 딕셔너리 
# print(d2['apple'])        # 없는 키 호출 시-> KeyError: 'apple'
print( d2.get('apple'))     # 텅비어있는 상태: None Type

# key가 없으면 100을 설정
d2['apple'] = d2.get('apple', 100)        
print( d2)

print("-- dict 반복자")
price = {"apple":100, "grap": 200}
for key in price: # key를 반환
    # key->value
    # price['apple'], price['grap']
    value = price[key] 
    print(value)

print("---")
print(price.get('apple'), price.get('apple2'),  price.get('apple2',0))    

