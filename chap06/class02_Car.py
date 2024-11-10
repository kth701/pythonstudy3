
class Car:
    cc = 0
    door = 0
    carType = None # null

    # 생성자
    def __init__(self, cc, door, carType):
        # 멤버변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType

    # 소멸자(생성자 반대 역할)
    def __del__(self):
        print('소멸자')
        print(self.cc)

        del self.cc # 변수 무효화
        print(self.cc)

        del self.door
        print(self.door)
        
        del self.carType
        print(self.carType)


    # 메서드
    def display(self):
        print("자동차는 %d cc이고, 문짝은 %d개, 타입은 %s" % (self.cc, self.door, self.carType))
        print(f"자동차는 {self.cc} cc이고, 문짝은 {self.door}개, 타입은 {self.carType}")
        print("자동차는 {} cc이고, 문짝은 {}개, 타입은 {}".format(self.cc, self.door, self.carType))
        

# 객체 생성
car1 = Car(2000, 4, "승용차")
car2 = Car(3000, 5, "SUV")

# 멤버메서드 호출
print("--")
car1.display() # 참조형변수(객체).변수 또는 참조형변수(객체).메서드
print("--")
car2.display()

