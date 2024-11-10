# 멤버메서드(self)
# 클래스메서드(cls), @classmethod :  클래스 단위로 메서드

class DatePro:
    # 1. 객체(멤버) 변수
    content = "날짜 처리 클래스"

    # 2. 객체 생성자
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 3. 객체 메서드
    def display(self):
        print("%d-%d-%d" % (self.year, self.month, self.day))

    # 4. 클래스 메서드
    @classmethod
    def date_string(cls, dateStr):
        year = dateStr[:4]
        month= dateStr[4:6]
        day = dateStr[6:]

        print(f"{year}년 {month}월 {day}일")

# 객체 생성
print("-- 1. 객체")
date = DatePro(2024,11,10)
print( date.content, date.year,date.month, date.day)
date.display()

# 클래스 메서드 호출
print("-- 2. 클래스메서드")
DatePro.date_string('20241110')
# print(DatePro.display()) # error 클래스 단위로 접근 불가
# print(DatePro.year) # error 클래스 단위로 접근 불가
print(DatePro.content)


    


