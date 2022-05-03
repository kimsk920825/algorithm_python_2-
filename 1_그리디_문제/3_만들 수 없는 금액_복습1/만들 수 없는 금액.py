import sys

sys.stdin = open("input.txt", "r")

numberofCoins = int(input())

coins = list(map(int, input().split()))
coins.sort()

check = 1
for i in coins:
    if check < i:
        break
    check += i
print(check)
