# 하위 디렉터리 검색하기
import os

def search(dirname):
    # 하위 디렉터리를 포함한 모든 파이썬 파일 검색
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            # 확장자가 .py인것들만 추출
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass

search("D:/이지은/대외활동/conseq/2020 활동/빅데이터 스터디/week3_04.28")

