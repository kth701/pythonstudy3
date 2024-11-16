# 클래스: Person
# 생성자: 이름, 성별 나이 초기화
# 메서드: display(이름, 성별, 나이 출력 가능)

# 출력 예시)
# 이름 입력 : 홍길동
# 나이 입력: 10
# 성별(male/female)
# ================
# 이름: 홍길동, 성별: 남자
# 나이: 30
# ================

class Persion:
    def __init__(self, name, gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print("="*30)
        if (self.gender == 'female'):
            print("이름:{}, 성별:{}\n나이: {}".format(self.name, "여자", self.age))
        else :
           print("이름:{}, 성별:{}\n나이: {}".format(self.name, "남자", self.age))

        print("="*30)

# 객체를 생성
persion = Persion("홍길동", "male", 10)
persion.display()