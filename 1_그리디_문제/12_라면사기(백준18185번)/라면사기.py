import sys


sys.stdin = open("input.txt", "r")
number = int(input())
data = list(map(int, input().split()))
## 1회차 시도
# result = 0

# for i, numb in enumerate(data):
#     if i == number - 2:
#         break
#     # print(data[i], data[i + 1], data[i + 2])
#     if data[i] == 1 and data[i + 1] == 1 and data[i + 2] == 1:
#         del data[i : i + 3]
#         result += 7
#     if data[i] == 1 and data[i + 1] == 1:
#         del data[i : i + 2]
#         result += 5
#     # print(number)
#     # result += number * 3
# for numb in data:
#     result = result + (numb * 3)
# print(result)
# 2회차 시도

# (i+1)번 공장의 라면 > (i+2)번 공장의 라면
result = 0
for i in range(number - 2):
    # 만약 i+1아 i+2보다 크다면
    if data[i + 1] > data[i + 2]:
        # data[i]와 data[i+1] - data[i+2] 두 값중 가장 낮은 값을 추출한다.
        m = min(data[i], data[i + 1] - data[i + 2])
        # m 횟수만큼 data[i], data[i+1] 값 제외 후 5원 누적
        result += m * 5
        data[i] -= m
        data[i + 1] -= m
    # 만약 data[i]와 data[i+1] 그리고 data[i+2]이 모두 양수라면
    if data[i] > 0 and data[i + 1]:
        m = min(data[i], data[i + 1])
        result += m * 7
        data[i] -= m
        data[i + 1] -= m
        data[i + 2] -= m
