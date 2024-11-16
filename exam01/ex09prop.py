# property

class XY:
    
    def __init__(self, x,y,z):
        self._x = x
        self._y = y
        self._z = z
        # private
        self.__name = "홍길동"
        self.addr = "부산"
    
    #일반적인 메서드
    def x(self):
        return self._x
    
    #일반적인 메서드-> @property: 함수이름-> 멤버변수처럼 사용한다는 의미
    @property
    def y(self):
        return self._y
    
    # 함수를 이용하여 값저장, 불러오기// setter, getter
    #
    #def zSetter(self,z):
        self._z = z
    # def zGetter(self):
    #     return self._z
    @property   #getter역할  객체.함수이름
    def z(self):
        return self._z
    @z.setter   #setter역할 객체.함수이름
    def z(self, value):
        self._z = value


    
    
test = XY(100,200,10)
print("일반 메서드(함수):", test.x() )
print("@property데코레이트 메서드(함수):", test.y)
# test.y = 1000 # y는 변수가 아니고 함수이름이므로 error 

print("-- setter, geeter")
# print(test.zGetter())
# test.zSetter(10000)
# print(test.zGetter())

print("z=",test.z)
test.z = 20000
print("z=", test.z)

print("-- public , private")
#print(test.name) #private 속성: 접근불가능 
print(test._XY__name) #private 속성: 접근불가능 => 접근 가능
print(test.addr)

