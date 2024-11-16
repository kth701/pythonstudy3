

# 상속 : 기능확장 목표, 부모클래스(공통기능), 자식클래스(공통기능+기능확장)
#상위클래스: 공통기능
class FindPath:

    def __init__(self):
        print("부모생성자 호출: FindPath()")

    def find(self, start, dest):
        print(start, dest)

#하위클래스: 기능확장
class FPbicycle(FindPath):

    def __init__(self):
        super().__init__()
        print("자식 생성자: Fpbicycle()")

    def get_bicycle_road(self):
        print("get bicycle road")

    # 오버라이딩(재정의)
    def find(self, start, dest):
        super().find(start, dest) # 부모클래스 메서드 호출
        print("bicycle:",start, dest)

bicycle = FPbicycle()

# 상속받은 부모클래스 메서드 그대로 사용 가능
bicycle.find("Seoul","Busan") 
bicycle.get_bicycle_road() # 자식클래스 메서드

# 상속받은 부모클래스 메서드를 자식클래스에서 재정의 사용가능(오버라이딩)



