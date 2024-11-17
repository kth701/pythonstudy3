
# 리스트 = 여러 자료를 모아놓은 자료 구조
list_a = [1,2,3,4,5]
list_b = [
    [1,2],
    [3,4],
    [5]
    ]

print(list_a, list_b)
print("list_a:", list_a[1]) # 직접 접근하여 데이터 읽어오기
print("list_b:", list_b[1], list_b[1][0])
print("-- 1차원 리스트 구조")
for i in list_a:
    print(i)
print("-- n차원 리스트 구조")
for i in list_b:
    print(i) # 리스트 개체
    for data in i:
        print(data)

