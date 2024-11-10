# 클래스 : 메서드(함수) + 멤버변수(속성)
# 함수(메서드):기능수행
# 멤버변수(속성): 상태-> 데이터 저장소
# 사용자가 원하는 특정한 자료형을 설계(기능 수행)

# 기본자료형(단일), 자료구조(복합구조,여러개의 자료): [10,True, ]


# 1. 함수 정의

def calc_func(a,b):
    x = a
    y = b

    def plus():
        p = x+y
        return p
    def minus():
        m = x-y
        return m
    
    return plus, minus # 함수를 반환
    
# 함수 수행후 반환값을 저장 => 반환값 (함수식)
p, m = calc_func(10,20)
print('plus():', p())
print('minus():', m() )


# 2. 클래스 선언
# print("-- 클래스 선언")
class calc_class:
    # 멤버변수 기본설정값 공개형(public):외부에서 접근가능
    x = y = 0

    # 생성자 함수(특수 함수)
    def __init__(self, a,b):
        self.x = a
        self.y = b

    # 일반함수(메서드)
    def plus(self):
        p = self.x + self.y
        return p
    def minus(self):
        m = self.x - self.y
        return m
    
# 클래스 -> 생성  -> 참조형변수(객체, 인스턴스)
myCalc = calc_class(10,20)
print('plus=',myCalc.x, myCalc.y, myCalc.plus() )
print('minus=', myCalc.x, myCalc.y,myCalc.minus())
