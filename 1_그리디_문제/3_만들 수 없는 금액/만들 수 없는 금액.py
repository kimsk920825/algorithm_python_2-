import sys

sys.stdin = open("input.txt", "r")

numberOfCoins = int(input())

coinLists = list(map(int, input().split()))
coinLists.sort()

target = 1

for coin in coinLists:
    if target < coin:
        break
    target += coin
print(target)
