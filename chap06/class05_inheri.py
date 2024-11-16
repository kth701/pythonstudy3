# 상속(Inheritance) : 자원 재사용
# 형식: class 하위(자식)클래스명(부모,상위클래스):

# 부모(상위) 클래스 정의
class Super:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("부모클래스 생성자 수행")

    def display(self):
        print('name:%s, age: %d' % (self.name, self.age))

    def super_prn(self):
        print("super 클래스에서 생성한 super_prn()메서드입니다.")

print("-- 부모클래스 객체 생성하기")
my_super = Super('상위(부모)클래스', 100)
my_super.display()
print(my_super.name, my_super.age)



class Sub(Super):
    # age, name
    gender = None   

    def __init__(self, name, age, gender):
        # 부모클래스의 멤버 변수
        # super: 부모클래스 , self: 자신 클래스
        # super(): 부모 클래스 생성자
        super().__init__(name, age)  # 부모 클래스 생성자 호출

        # 자식클래스의 멤버 변수
        #self.name = name
        #self.age = age

        # 자식클래스의 멤버변수
        self.gender = gender 
        print("자식클래스 생성자 수행")

    #def display(self): #오버라이딩
    #    return print(f"이름:{self.name}, 나이:{self.age}, 성별:{self.gender}")


print()
print("-- 자식클래스 객체 생성하기")

my_sub = Sub('하위(자식)클래스', 20, '여자')
my_sub.display() # 상속 받은 메소드

print(my_sub.age, my_sub.name) # 상속 받은 멤버변수
print(my_sub.gender) # 자식 클래스 멤버변수
my_sub.super_prn() # 상속 받은 메서드


# 부모 클래스 -> 자식 클래스 : 부모클래스 메서드이름, 자식클래스 메서드 동일 => 오버라이딩 기능
#   

