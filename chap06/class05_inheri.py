# 상속(Inheritance) : 자원 재사용
# 형식: class 하위(자식)클래스명(부모,상위클래스):

# 부모(상위) 클래스 정의
class Super:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('name:%s, age: %d' % (self.name, self.age))

print("-- 부모클래스 객체 생성하기")
my_super = Super('상위(부모)클래스', 100)

print("-- 자식클래스 객체 생성하기")
class Sub(Super):
    gender = None   

    def __init__(self, name, age, gender):
        # 부모클래스의 멤버 변수
        self.name = name
        self.age = age

        # 자식클래스의 멤버변수
        self.gender = gender 

    def display(self):
        return print(f"이름:{self.name}, 나이:{self.age}, 성별:{self.gender}")
    
    

