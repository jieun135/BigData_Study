# 프로그램을 짤 때 입력과 출력은 먼저 생각해라
# 구구단
def GuGu(n):
    result = []
    i = 1
    while i<10:
        result.append(n*i)
        i = i+1
    return result

print(GuGu(2))