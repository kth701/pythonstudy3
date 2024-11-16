class Korean:

    # 4. 클래스 메서드
    @classmethod
    def date_string(cls, dateStr):
        year = dateStr[:4]
        month= dateStr[4:6]
        day = dateStr[6:]

        print(f"{year}년 {month}월 {day}일")


k1 = Korean()
k1.date_string('20241110')
Korean.date_string('20241110')
