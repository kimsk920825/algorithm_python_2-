import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
a, b, d = map(int, input().split())
geo = []
for _ in range(n):
    geo.append(list(map(int, input().split())))
check = [[0] * m for _ in range(n)]
check[a][b] = 1

############################데이터 입력 완료############################
# 북,동,남,서
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

# 캐릭터 왼쪽으로 돌기 --> 함수로 바꾸기
def turn_left():
    global d
    d = d - 1
    if d == -1:
        d = 3


# 4방향을 돌고, 갈 공간이 없을 때 뒤로 갈려고 하나 뒤에도 바다일 떄 멈춤. 아니라면 계속
count = 1
turn_time = 0
while True:
    turn_left()
    na = a + da[d]
    nb = b + db[d]
    if geo[na][nb] == 0 and check[na][nb] == 0:
        check[na][nb] = 1
        a = na
        b = nb
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        na = a - da[d]
        nb = b - db[d]
        if geo[na][nb] == 0:
            a = na
            b = nb
        else:
            break
        turn_time = 0
print(count)
