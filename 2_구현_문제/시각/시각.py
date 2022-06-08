import sys

sys.stdin = open("input.txt", "r")

# 크기는 몇인가?
n = int(input())
count = 0
for i in range(n + 1):

    for m in range(60):

        for s in range(60):
            if "3" in str(i) + str(m) + str(s):
                count += 1
print(count)
