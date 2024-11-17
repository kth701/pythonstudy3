# 이진 파일 (이미지, 동여상,...)

import os
from glob import glob

# 1. image 파일 경로
print('현재위치=> ',os.getcwd())
img_path = 'chap08\\image\\' # 이미지 원본 위치
img_path2 = 'chap08\\data\\' # 이미지 이동할 위치

# 2. 디텍터리 존재유무체크
if os.path.exists(img_path):
   print('해당 폴더가 존재합니다.')

   # image 파일 저장, 이동
   images = []
   #print(os.path.exists(img_path2), not(os.path.exists(img_path2)))
   
   if not(os.path.exists(img_path2)): #존재하지 않으면
        os.mkdir(img_path2) # 디렉토리 생성
   else: # 존재하면
       print('이동할 파일 폴더가 존재합니다.')

       # image 검색
       for pic_path in glob(img_path+'*.gif'): #'chap08/image/*.gif'
           print(pic_path)
           # 경로와 파일 구분
           img_path = os.path.split(pic_path)

           #print(img_path, img_path[0],img_path[1])
           images.append(img_path[1]) #파일만 추출하여 저장

           # 이진파일 읽기
           #open(file='chap08/data/abc.txt', mode='r')
           rfile = open(file=pic_path, mode='rb')
           output = rfile.read()

           # 이진파일 쓰기
           
           wfile = open(file=img_path2+img_path[1], mode='wb')
           wfile.write(output)

           print('이미지파일 복사완료:',img_path2+img_path[1])

           rfile.close()
           wfile.close()

    
