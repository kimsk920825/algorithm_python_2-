import sys

sys.stdin = open("input.txt", "r")
schedule = []
n = int(input())
for i in range(n):
    schedule.append(tuple(map(int, input().split())))
schedule.sort(key=lambda x: (x[1], x[0]))
et = 0
cnt = 0

for s, e in schedule:
    if s >= et:
        et = e
        cnt += 1
print(cnt)
