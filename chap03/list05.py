# 중첩 리스트(n차원)

list_a = [1,2,3]
print(list_a[0],list_a[1], list_a[2]) # 1 2 3

list_b = [ [1,2,3,4],[5,6,7,8],[9,10,11,12]]

# [1, 2, 3, 4] [5, 6, 7, 8] [9, 10, 11, 12]
print(list_b[0],list_b[1], list_b[2])
print(list_b[0][0],list_b[1][0],list_b[2][0]) # 1 5 9

print("-- for문 , 중첩 리스트 데이터 출력")
for items in list_b:
    #print(items) # 리스트 구조
    for item in items:
        print(item,end=" ")
