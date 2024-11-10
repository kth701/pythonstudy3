# 특수한 이름이 메서드 
# "__call__()"

class C:
    def __call__(self, num):
        return num*2
    def n_duble(self, num):
        return num*2


print("--- __call__()")
# 객체 생성자
c_inst = C() 

# 인스턴스를 함수처럼 이용
num1 = c_inst(10)  # c_inst(10) => c_inst.__call__(10)
num2 = c_inst.n_duble(20)
print(num1,num2)

print("--- __len__()")
class C2:
    def __init__(self,attr) :
        self.attr = attr

    def __len__(self):
        return self.attr

len_inst = C2(10)
print(len(len_inst), len_inst.__len__())

print("--- __getitem__()")
class C3:
    def __init__(self, attr):
        self.attr = attr

    def __getitem__(self, idx):
        return self.attr[idx]
    
getitem_inst = C3([10,100,20])
list_idx = getitem_inst[2]
print(list_idx)

print("--- @property :인스턴스변수를 간접적으로 접근")
class XY:
    def __init__(self, x,y):
        # 객체멤버 변수
        self.x = x
        self.y = y
        print("초기값설정:",self.x, self.y)

    @property
    def _x(self):
        return self.x
    
    def _y(self):
        return self.y

xy_inst = XY(100,200) # 생성자 이용하여 초기값 설정
print(xy_inst.x, xy_inst._y())







