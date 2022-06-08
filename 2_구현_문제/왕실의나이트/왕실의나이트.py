import sys

sys.stdin = open("input.txt", "r")

# 크기는 몇인가?
data = input()
x = int(ord(data[0])) - int(ord("a")) + 1
y = int(data[1])
count = 0

steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
for xaixs, yaxis in steps:
    nx, ny = 0, 0
    nx = x + xaixs
    ny = y + yaxis
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        print(nx, ny)
        count += 1
print(count)
