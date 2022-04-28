import sys

sys.stdin = open("input.txt", "r")

n = int(input())
players = []
for _ in range(n):
    players.append(tuple(map(int, input().split())))
players.sort(key=lambda x: (x[0], x[1]))

for i in range(len(players)):
    for height, weight in players[i + 1 :]:
        if players[i][1] < weight:
            print(players[i])
