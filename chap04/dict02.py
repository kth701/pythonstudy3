# 단어 출현 빈도수 구하기

charset = ['abc','code', 'band', 'band','abc']
wc = {} # 비어있는 셋

# get(key) -> value
for key in charset:
    
    # wc텅빈상태 -> wc.get(abc) -> None
    # 키에 대한 값이 없으면 두번째 인자값을 초기설정
    print(key,"=>", wc.get(key,0), end=', ')
    wc[key] = wc.get(key, 0) + 1

    print("\n---")
    print(wc[key])

print()
print(wc)    

# 자료구조 복제 : 얕은 복사, 깊은 복사
print("-- 객체 주소 복사")

print("- 1. 얕은 복사: 주소 복사")
name = ['홍길동','이순신','강감찬']
print('name=', name)

name2 = name
print("name2=",name2)
print("name주소:",id(name), "name2주소",id(name2))

# 원본 수정
name2[0] = "길길동"
print(name, name2)

# 깊은 복사
import copy
print("- 2. 깊은 복사")
name3 = copy.deepcopy(name)
print(name, name3)
print(id(name), id(name3))

name3[0] = "김길순"
print(name, name3)





    

