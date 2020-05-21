# 탭을 4개의 공백으로 바꾸기
import sys

src = sys.argv[1] # 탭을 포함하고 있는 원본 파일 이름
dst = sys.argv[2] # 파일 안의 탭을 공백 4개로 변환한 결과를 저장할 것.

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t"," "*4) # \t == 탭

f = open(dst, 'w')
f.write(space_content)
f.close()