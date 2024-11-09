
# 중첩함수
# - 외부함수: bank_account(): 잔액(balance) outer 변수
# - 내부함수: getBalance(): 잔액확인, deposit(money):입금, widtdraw(money):출금
# 출금액이 잔액보다 많은 경우 '잔액이 부족합니다' 메시지 출력

# 예시)
# 최초 계좌의 잔액을 입력하세요: 1000
# 현재 계좌 잔액은 1000원 입니다.
# 입금액을 입력하세요: 15000
# 15000원 입금후 잔액은 1600원 입니다.
# 출금액을 입력하세요: 3000
# 3000원 출금후 잔액은 13000원 입니다.

# 함수 정의
def bank_account(bal):
    balance = bal

    def getBalance() : # 잔액확인
        return balance
    def deposit(money): #입금
        nonlocal balance
        balance += money
    def withdraw(money): # 출금
        nonlocal balance # 외부함수에 있는 변수
        if balance < money:
            print('잔액이 부족합니다.')
        else:
            balance -= money

    return getBalance, deposit, withdraw

# 1.키보드로 초기 잔액 입력
bal = int(input("최초 계좌의 잔액을 입력하세요:"))

# 2.초기 잔액으로 설정
getBalance, deposit, withdraw = bank_account(bal)
print(f"현재 계좌 잔액은 {getBalance()}원 입니다.")

money = int(input("입금액을 입력하세요:"))
deposit(money)
print(f"{money}원 입금후 잔액은 {getBalance()}원 입니다.")

money = int(input("출금액을 입력하세요:"))
withdraw(money)
print(f"{money}원 출금후 잔액은 {getBalance()}원 입니다.")

money = int(input("출금액을 입력하세요:"))
withdraw(money)

               


