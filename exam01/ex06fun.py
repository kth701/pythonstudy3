print("-- 람다(Lambda)")
def mul(x,y):
    return x*y
print( mul(2,3) )
print( (lambda x,y: x*y)(3,4)  )

mul2 = lambda x: 2*x
print( mul2(4))

print("-- lambda test2")
nums = [5,0,-7, -10]
print("nums:",nums)

print( sorted(nums), sorted(nums, reverse=True) )
print( sorted(nums, key=lambda x: x**2))


print("---")
def free_arg(*args, **kwargs):
    print("args = {}".format(args))
    print("kwargs = {}".format(kwargs))

#free_arg()
#free_arg(1,2)
free_arg(10,20, 30,first="1st", second="2nd")


print("--- ")
def group_by_age(**kwargs):
    print(kwargs)

    group = {"adult":[], "non-adult":[]}
    for name, age in kwargs.items():
        print(name, age)

        if age>18:
            group["adult"] += [name]
            # group["key"] => value호출
            # [] += ['kim'] : ['kim'] => ['kim','park'],...
        else:
            group["non-adult"] += [name]
        
    return group

group_result = group_by_age(kim=25, jeong=16,park=11, hong=21, tea=12)
print(group_result)


# 가변인자("*매개변수","**매개변수")
print("-- **가변인자(딕셔너리)")
def mydicFun(name, **other):
    print("**other type:", type(other), other)


mydicFun("홍길동", age=10, addr='부산시')

print("--- *가변인자(튜플)")
def mul(*nums):
    # *가변인자 -> 튜플구조
    print("*가변인자 type:", nums, type(nums))
    
    result = 1
    for i in nums: # (3,4), (1,2,3,4,5)
        result *= i 
    return result

print( mul(3,4),mul(1,2,3,4,5))