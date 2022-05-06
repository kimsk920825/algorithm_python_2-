import sys


sys.stdin = open("input.txt", "r")

number = int(input())
data = list(map(int, input().split()))
result = 0

# for i in range(number):
#     print(data[i])
#     if data[i] == 1 and data[i + 1] == 1 and data[i + 2] == 1:
#         result += 7
#     if data[i] == 1 and data[i + 1] == 1 and data[i + 2] != 1:
#         result += 5
# print(data)
for i, numb in enumerate(data):
    if i == number - 2:
        break
    # print(data[i], data[i + 1], data[i + 2])
    if data[i] == 1 and data[i + 1] == 1 and data[i + 2] == 1:
        del data[i : i + 3]
        result += 7
    if data[i] == 1 and data[i + 1] == 1:
        del data[i : i + 2]
        result += 5
    # print(number)
    # result += number * 3
for numb in data:
    result = result + (numb * 3)
print(result)
