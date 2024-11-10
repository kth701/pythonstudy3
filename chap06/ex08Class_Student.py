# 클래스명: Student
# 멤버변수:학생이름(name), 국어(kor), 수학(mat), 영어(eng)
# 멤버메서드: 총점(total), 평균(average), 학생정보출(to_string)


class Student:
    name=None
    kor=mat=eng=0
    
    # 생성자
    def __init__(self, name, kor, mat, eng) :
        self.name = name
        self.kor = kor
        self.mat = mat
        self.eng = eng

    def total(self):
        return self.kor+self.mat+self.eng
    
    def average(self):
        return self.total()/3
    
    def to_string(self):
        return "{}\t{}\t{:.2f}".format(self.name, self.total(), self.average())

#학생 리스트를 선언
students = [
    Student("홍길동", 100,100,100),
    Student("동순이", 80,75,60),
    Student("길순이", 65,88,59)
    ]

# 학생을 한 명씩 출력
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())

# 객체를 생성하지 않고 메서드 또는 멤버변수 사용
# st1 = Student("이순신", 100,20,90)
# st1.eng, st1.mat, st1.average()
#    => 클래스 이름으로 접근 => Student.eng, Student.average
