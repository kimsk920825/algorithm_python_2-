import sys

sys.stdin = open("input.txt", "r")

# 크기는 몇인가?
n = input()
plans = input().split()
x, y = 1, 1
# 이동정보입력
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
move_direction = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(len(move_direction)):
        if plan == move_direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > 5 or ny > 5:
        continue
    x, y = nx, ny
print(x, y)
