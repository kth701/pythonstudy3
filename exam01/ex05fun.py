print("-- 전역변수, 지역변수")
g_num = 100
def number():
    #global g_num #전역변수
    #g_num = 100 # 지역변수
    #l_num = 10 # 지역변수
    #print("지역변수(함수안에있는 변수):",l_num)
    #print("전역변수(함수밖에있는 변수):", g_num)
    print("전역/지역변수 동일한 이름이면 지역변수우선:", g_num)

number()


print("---")
# 리스트 구조 : [0,1,...]
def mySlicing(s, start=0, end=1):
    return s[start:end] #  start <= x < end

str = "python"
print( mySlicing(str))
print( mySlicing(str, 1,5))


print("-- 함수 및 default")
def calc_area(height=5, width=4):
    area = height * width

    # 반환값이 1개일 경우
    #return area

    # 반환값이 2개이상
    border = height*2 + width*2
    return area, border

# 함수 호출(실행)
#result1 = calc_area(5,4)
#print(result1, calc_area(10,2))

rs1, rs2 = calc_area(10)
print("area={}".format(rs1))
print(f"border= {rs2}")