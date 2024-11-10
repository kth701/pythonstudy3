# 캡슐화 : 여러 정보를 1개 단위 묶어주는 기능
# 정보 은닉 : 외부에서 접근 불가능 하게 하는 기능

class Account:
    # 은닉 멤버변수(비공개) => "__변수이름" => private
    __balance = 0 # 잔액
    __accName = None # 예금주
    __accNo = None # 계좌 번호
    

    # 생성자
    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accName = name
        self.__accNo = no

    # 잔액, 계좌번호 확인하는 메서드
    def getBalance(self):
        return self.__balance, self.__accNo, self.__accName
    
    # 입금하기(setter)
    def deposit(self, money):
        if money<0:
            print('금액 확인')
            return # 함수(메서드) 종료
        
        self.__balance += money

    # 출금하기(getter)
    def withdraw(self, money):
        if self.__balance < money:
            print('잔액 부족')
            return 
        self.__balance -= money

# 객체 생성
acc = Account(100, '홍길동', '123-123-1234-12')  

# Getter 호출
# acc.__balance # error 접근 불가
bal = acc.getBalance()
print(bal, type(bal))

# 메서드를 이용하여  private 변수에 값을 전달
acc.deposit(10000) 
bal = acc.getBalance()
print(bal, type(bal))

acc.withdraw(50000)
bal = acc.getBalance()
print(bal, type(bal))




    
    


