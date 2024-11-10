# 다형성(Polymorphisim)
# 1개의 메세지으로 통해 여러타입의 동작을 수행
# 10+20 => 30, "10"+"20" => "1020"


# 비행:날다() -> 비행기:날다(), 새:날다(), 종이비행기:날다()

# 1. 부모
class Flight:
    def fly(self):
        print('날다, fly원형 메서드')

# 2. 자식(비행기)
class AirPlane(Flight):

    # 함수 재정의
    def fly(self):
        print('비행기가 날다')

# 2. 자식(새)
class Bird(Flight):

    # 함수 재정의
    def fly(self):
        print('새가 날다')

# 2. 자식(종이비행기)
class PaperAirplane(Flight):

    # 함수 재정의
    def fly(self):
        print('종이 비행기가 날다')                


# 객체 생성
flight = Flight() # 부모 객체

air = AirPlane()    # 자식:비행기
bird = Bird()       # 자식: 새
paper = PaperAirplane() # 자식: 종이 비행기

# 다형성
flight.fly()

flight = air # 부모참조형변수 = 자식참조형변수
flight.fly()

flight = bird
flight.fly()

flight = paper
flight.fly()
