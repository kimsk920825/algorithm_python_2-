import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0

# n:5 m:3
# 1 3 2 3 2
for i in range(n):
    j = i + 1
    if j == n:
        # print(j)
        break
    else:
        for k in range(j, n):
            print(data[i], data[k])
            if data[i] == data[k]:
                result += 0
            if data[i] != data[k]:
                result += 1
        # if data[i] == data[i + 1]:
        #     result += 0
        # if data[i] != data[i + 1]:
        #     result += 1
print(result)
