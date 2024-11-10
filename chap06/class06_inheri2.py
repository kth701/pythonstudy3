# 오버로딩, 오버라이딩(재정의)

# 사원 
class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name
    def pay_calc(self): # 추상 메서드
        pass

# 사원 -> 정규직
class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name) # 부모생성자 초기화

    # 상속 받은 메서드 재정의, 오버로딩
    def pay_calc(self, base, bonus):
        self.pay = base + bonus # 급여 = 기본급+상여금
        print(f"총 수령액: {self.pay}원")
        
# 사원-> 임시직        
class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)

    # 재정의, 오버로딩(동일한 함수이름은 인자개수,타입으로 구분)
    def pay_calc(self, tpay, time):
        self.pay = tpay * time # 급여 = 작업시간 * 시급
        print(f"총 수령액: {self.pay}원")

p = Permanent("이순신")
p.pay_calc(300, 20)

t = Temporary("홍길순")
t.pay_calc(200, 10)


