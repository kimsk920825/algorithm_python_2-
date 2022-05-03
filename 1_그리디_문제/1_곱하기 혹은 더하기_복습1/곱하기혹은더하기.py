import sys

sys.stdin = open("input.txt", "r")

# 문자열로 받기
number = input()
result = 0
for i in number:
    # i를 받을때마다 숫자로 바꾸기.
    i = int(i)
    # 만약 result가 0 또는 1이라면 "+"
    if result == 0 or result == 1:
        result += i
    # 만약 result가 2 이상이라면
    else:
        if i == 0 or i == 1:
            result += i
        else:
            result *= i
print(result)
