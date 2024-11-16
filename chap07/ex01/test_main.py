import test_module as test


# 특수한 변수명 => "__name__"
# 프로그램의 진입점 : 엔트리 포인트
# 엔트포인트: "__name__"변수에 "__main__"값이 설정됨
# 엔트포이트가 아닌 모듈에는 모듈이름이 설정
print("현재모듈이름:",__name__)
radius = test.number_input()
print(test.get_cirumference(radius))
print(test.get_circle_area(radius))