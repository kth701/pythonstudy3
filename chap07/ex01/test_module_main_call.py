
# 다른 모듈 호출하기
import test_module01_called
import test_module02_called



print("# test_module_call.py 모듈의 __name__ 출력하기")
print("__name__의이름:" ,__name__)
print()

if __name__ == "__main__":
    print("프로그램 시작하는 모듈입니다.")
    print()