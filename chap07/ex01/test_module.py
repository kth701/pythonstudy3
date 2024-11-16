PI = 3.141592

def number_input():
    output = input("숫자 입력>") # 문자열입력 -> 숫자형
    return float(output)

def get_cirumference(radius):
    return 2*PI*radius
def get_circle_area(radius):
    return PI*radius*radius

if __name__ == "__main__":
    print("-"*30)
    print("현재모듈이름:",__name__)
    print("-"*30)