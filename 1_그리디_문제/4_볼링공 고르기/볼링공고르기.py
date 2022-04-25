import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

balls = list(map(int, input().split()))

array = [0] * 11
for weight in balls:
    array[weight] += 1
cnt = 0

for i in range(1, m + 1):
    n -= array[i]
    cnt += array[i] * n
print(cnt)
