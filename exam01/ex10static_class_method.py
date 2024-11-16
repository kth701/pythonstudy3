# 클래스이름으로 메서드 접근 가능
# staticmethod: 인스턴스 변수 수정 불가
# classmethod: 클래스변수 수정 가능

class XY:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 클래스이름 or 객체이름으로 접근 가능
    @staticmethod # self 첫번째가 없다
    def magintude(x,y):
        return(x**2+y**2)**(1/2)

test = XY(3,4)

print(test.x, test.y)
print(test.magintude(test.x, test.y))
print(XY.magintude(test.x, test.y))

print("-- classmethod")
class Korean:
    country = "Korea"

    # classmethod : 첫번째 인자 cls가 반드시 있어야함.
    @classmethod
    def channge_country(cls, name):
        cls.country = name



k1 = Korean()
k2 = Korean()
k1.channge_country("South Korea")
print(k1.channge_country)

