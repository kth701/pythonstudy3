# 다음 lst변수를 대상ㅇ로 각 단계별로 list를 연산하는 프로그램을 구현
# lst = [10,1,5,2]

# 단계1: [10,1,5,2,10,1,5,2]
# 단계2: [10,1,5,2,10,1,5,2,20]
# 단계3: [1,2,1,2]

# 단계1: lst원소의 2배, result 저장
# 단계2: lst의 첫번째 원소의 2곱하기, resut저장
# 단계3: result의 홀수번째 원소만 추출 result2 저장

lst = [10,1,5,2]
print(lst)

result = lst*2
print(result)

num = result[0] * 2 #첫번째요소 값 * 2
result.append(num)
print(result)

result2 = result[1::2]# 인덱스1번째 부터 2칸씩 건너뛴 인덱스번호만 추출
print(result2)


