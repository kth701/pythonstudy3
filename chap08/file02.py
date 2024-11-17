# 텍스트 자료 읽기 관련함수
# read()        : 전체 텍스트 읽어오기 -> 문자열(str)반환
# readlines()   : 전체 텍스트 줄단위 읽어오기 -> list 자료형으로 반환
# readline()    : 한 줄 단위 읽어오기 -> str반환

try:
    # 1. read()
    ftest = open('chap08/data/test_data.txt', mode='r')
    full_text = ftest.read() # 문자열(str반환)
    print('-- 1. read()')
    # print(full_text) 
    print('-- read()반환 type:', type(full_text))
    print()

    # readlines();: 전체를 줄단위 , list
    print('-- 2. readlines()')
    ftest = open('chap08/data/test_data.txt', mode='r')
    lines = ftest.readlines() # list구조 반환
    print(lines)
    print('-- readlines()반환 type:', type(lines))
    print('문단 수:', len(lines))

    # list -> 문장 추출
    docs = []
    for line in lines:
        print(line.strip())
        docs.append(line.strip())
    print('-- 문장 추출')
    print(docs)
    print()

    # readline():  한 줄 읽기
    ftest = open('chap08/data/test_data.txt', mode='r')
    line = ftest.readline() # 한 줄 읽기
    print(line)
    print('-- readline()반환 type:', type(line))


    # with 블럭: 블럭을 벗어나면 autoclose 기능 수행
    with open('chap08/data/test_data.txt', mode='r') as ftest2:
        print(ftest.readline())

except Exception as e:
    print('Error발생:',e)
    
finally:
    ftest.close()