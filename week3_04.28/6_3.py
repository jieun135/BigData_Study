# 게시판 페이징하기
def getTotalPage(m, n):
    return m // n+1
print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(33,10))