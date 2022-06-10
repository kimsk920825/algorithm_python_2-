import sys

sys.stdin = open("input.txt", "r")
n, m = input().split()
a, b, d = input().split()
a = int(a)
b = int(b)
d = int(d)
geo = []
for _ in range(int(n)):
    geo.append(list(input().split()))
print(geo[a][b])
############################데이터 입력 완료############################
# 북,서,남,동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 캐릭터가 보고있는 방향 북,동,남,서
news = [0, 1, 2, 3]
# 캐릭터 왼쪽으로 돌기
d = d - 1
if d == -1:
    d = 3
# 왼쪽으로 돌았을 때 해당 방향이 1인지 아닌지 확인하기.
##왼쪽으로 돌았을때 방향이 0이라면 geo[a+dx[0],[b]+dy[0]]
if d == 0:
    if geo[a + dx[0], [b] + dy[0]] == 1 or geo[a + dx[0], [b] + dy[0]] == 2:
        pass
    if geo[a + dx[0], [b] + dy[0]] == 0:
        geo[a][b] = 2
        a = a + dx[0]
        b = b + dy[0]
