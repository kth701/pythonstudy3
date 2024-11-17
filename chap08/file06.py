# 텍스트 자료 수집
import os
# 1. 경로 설정
print(os.getcwd())
txt_data = './txt_data'

# 2. 디렉터리 목록 반환
sub_dir = os.listdir(txt_data)
print(sub_dir)

# 각 디렉터리의 텍스트 자료 수집 기능
def textPro(sub_dir): # 'first', 'second' 디렉터리
    first_txt = []
    second_txt = []

    # 디렉터리 구성
    for sdir in sub_dir: # ['first', 'second']
        #print(sdir)
        
        # txt_data=> ./txt_data => pythonstudy3/txt_data 지칭
        dirname = txt_data +'/'+ sdir # './txt_data/first
        #print(dirname)
        file_list = os.listdir(dirname)
        print(file_list)

        # 파일 구성
        print("------")
        # first, second에 있는 파일목록
        for fname in file_list:
            file_path = dirname+"/"+fname
            #print(file_path)

            # file 선택
            if os.path.isfile(file_path):
                try:
                    file = open(file_path, mode='r', encoding='utf-8')
                    if sdir == 'first':
                        first_txt.append(file.read())   
                    else:
                        second_txt.append(file.read())   
                    
                except Exception as e:
                    print('error:', e)
                finally:
                    file.close()
                # end if
            # end for(inner)
        # end for (outer)
    
    return first_txt, second_txt
    # end function


# 함수 호출(실행)
first, second = textPro(sub_dir)


print('first_txt 길이=', len(first))
print('second_txt 길이=', len(second))


    



