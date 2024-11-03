# 내장함수(builtins모듈)

print("1.절대함수: abs()")
print(abs(-100), abs(100), abs(0))

print("2. all(iterable): 모든요소가 True -> True")
all_t1 = all([1, True, 10, -15., 5>2])
all_t2 = all([1, True, 10, -15., None]) # False: 0, None, {}
print('all_t1=', all_t1,', all_t2=', all_t2)

print("3. any(iterable): 모든요소가 False -> False")
all_t1 = any([0, False, None, 5<2])
all_t2 = any([0, False, None, 5>2]) # 하나라도 참일 경우 참
print('all_t1=', all_t1,', all_t2=', all_t2)

print('4. bin(number),oct(),hex(): 10진->2진, 8진, 16진')
print('10을 2진,8진,16진->',bin(10),oct(10), hex(10))

print('5. dir(객체): 객체내에 있는 변수,함수, 클래스 목록')
list_a = [1,2,3,4,5] # list객체에 대한 정보
#print( dir(list_a) )

print("6. eval(문자열식): 문자열식-> 계산식")
print("10+20", eval("10+20"))

print("7. ord(charactor): 특정문자->아스키코드 번호")
print('A:',ord('A'),", a:",ord('a'))