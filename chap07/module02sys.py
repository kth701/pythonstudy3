import sys
print(sys.argv)
#sys.exit() #프로그램 강제 종료
# print(sys.copyright)
# print(sys.version)

import os
print(os.name)
print(os.getcwd())
print(os.listdir())

print("-- 폴더 생성 및 삭제")
# os.mkdir("test100")
# os.rmdir("test100")

print("-- 파일 생성 및 삭제")
# with open("test.txt", "w",encoding="utf-8") as file:
#     file.write("안녕하세요... 파일생성 테스트...")
#     file.write("Hello Python!!!!")

# os.remove("test.txt")
# os.system("dir")

print("-- datetime")
import datetime
now = datetime.datetime.now()
print(now)
print("{}년 {}월 {}일 ".format(now.year, now.month, now.day))
print("{}시 {}분 {}초 ".format(now.hour, now.minute, now.second))
print("{}요일 ".format(now.weekday()))

from datetime import date, time
today_week = ["월","화","수","목","금","토","일"]
print(today_week[0])

print("---")
today = date(2024,11,10)
print(today.year, today.month, today.day, 
      '요일을 번호=>',today.weekday(), 
      today_week[today.weekday()]+"요일")

today_time = time(12,30,20)
isoTime = today_time.isoformat()
print(today_time.hour, 
      today_time.minute, 
      today_time.second, 
      isoTime)


print("-- urllib")
from urllib import request
url = request.urlopen("https://google.com")
google_home = url.read()
print(google_home)








