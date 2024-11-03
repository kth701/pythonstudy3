
names = ["apple", "banana","grap"]
print(names, '=>',"/".join(names))
print(names, '=>',"".join(names))

path_t = "c:/Users/User/"
filename = "main.py"
print("".join([path_t, filename]))

# 변수= 참일 경우 처리할 내용 if 조건식 else 거짓을 경우 처리할 내용
num = 42
odd_even = "odd" if num%2 ==1 else "even"
print(odd_even)

print("-- 리스트 컴프리헨션")
num_strings = [ str(i) for i in range(5)]
print(num_strings)

two = [ str(i) for i in range(10+1) if i%2==0]
print(two)


# all(), any()
files = ["file1.jpg","file2.jpg","file3.txt"]
# "file1.jpg" == ".txt" => False
# "file2.jpg" == ".txt" => False
# "file3.txt" == ".txt" => True
print(any(f[-4:]==".txt" for f in files))

words = ["ape","apple","alligator"]
print(all( w[0] == "a" for w in words))
print(all(len(w)>5 for w in words))

print("-- short circuit evaluation")
if True or 3%2 ==0:
    print("True or")
if False and 3%2==0:
    print("False and")

nums = [1,-5,3]    
if nums[0]>0:
    print("positive")

nums1 = []
if len(nums1)>0 and nums1[0]>0:
    print("positive!!")   



