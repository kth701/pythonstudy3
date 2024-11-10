# 특수한 이름이 메서드 : 클래스를 사용할 때 제공해 주는 보조 기능
# "__<이름>__()" 형태 구성
# "__str__"


class Student2:
    name=None
    kor=mat=eng=0
    #생략시 기본을 설정됨
    #def __init__(self):
    #    pass
    
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
    
    # 특수한 이름의 메서드
    def __str__(self):
        return "{}\t{}\t{:.2f}".format(self.name, self.total(), self.average())
    
    def __eq__(self,value) :
        return self.total() == value.total()
    
    def __ne__(self,value) :
        return self.total() != value.total()
    


#학생 리스트를 선언
students = [
    Student2("홍길동", 100,100,100),
    Student2("동순이", 80,75,60),
    Student2("길순이", 65,88,59)
    ]

# 학생을 한 명씩 출력
print("이름", "총점", "평균", sep="\t")
for student in students:
    #print(student.to_string())
    print(str(student))


print("--- 특수한 이름이 메서드 테스트")
st_a = Student2("홍길동", 100,100,100)
st_b = Student2("동순이", 100,100,100)

print( st_a == st_b)
print( st_a.total() == st_b.total())
print( st_a != st_b)