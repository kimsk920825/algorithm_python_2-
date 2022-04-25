import sys
import itertools

sys.stdin = open("input.txt", "r")

n = int(input())
coins = list(input().split())
print(coins)
result = 2170000
permutation_result = list(map("".join, itertools.permutations(coins)))
for number in permutation_result:
    total = 0
    for each_number in number:
        each_number = int(each_number)
        total += each_number
    if result > total:
        result = total


print(result)
