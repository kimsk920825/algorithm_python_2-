import sys

sys.stdin = open("input.txt", "r")

row, column = map(int, input().split())
result = 0
######
# 방법1#
######
# for i in range(row):
#     data = list(map(int, input().split()))
#     if min(data) > result:
#         result = min(data)

######
# 방법2#
######
# for i in range(row):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
######
# 방법3#
######

for i in range(row):
    data = list(map(int, input().split()))
    min_value = 2147000
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)
