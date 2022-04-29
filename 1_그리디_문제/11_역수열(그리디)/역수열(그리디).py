from collections import deque
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

number = int(input())
data = list(map(int, input().split()))
seq = [0] * number

for i in range(number):  # 역수열 탐색
    for j in range(number):  # 수열 탐색
        if data[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            data[i] -= 1
for x in seq:
    print(x, end=" ")
