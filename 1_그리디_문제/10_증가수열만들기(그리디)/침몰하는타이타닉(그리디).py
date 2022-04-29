from collections import deque
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

number = int(input())
data = list(map(int, input().split()))


tmp = []
result = []
result_letter = []


# # 시도1 실패#
# while data:
#     # 데이터가 2개 이상일때만
#     if len(data) >= 2:
#         if data[0] < data[-1]:
#             if data[0] > tmp[-1]:
#                 left = data.popleft()
#                 tmp.append(left)
#                 result.append("L")
#             else:
#                 right = data.pop()
#                 tmp.append(right)
#                 result.append("R")
#         else:
#             if data[-1] > tmp[-1]:
#                 right = data.pop()
#                 tmp.append(right)
#                 result.append("R")
#             else:
#                 left = data.popleft()
#                 tmp.append(left)
#                 result.append("R")
#         print(result)
#     if len(data) == 1:
#         data.pop()
#         result.append("L")
# print(result)

# 시도2 실패#
# 데이터가 존재할때까지 반복문을 하라
# while data:
#     #데이터가 2개 이상일때만
#     if len(data) >= 2:
#         #왼쪽과 오른쪽을 뽑아라
#         left = data.popleft()
#         right = data.pop()
#         #두 숫자중 작은 숫자를 출력하라
#         #tmp = min(left, right)
#         if left
#         if tmp == left:
#             result.append(("L",tmp))
#             data.append(right)
#         else:
#             result.append("R")
#             data.appendleft(left)
#         print(result)
#     if len(data) == 1:
#         data.pop()
#         result.append("L")
# # print(result)

# 시도3 성공 #
while data:
    # 데이터가 2개 이상일때만
    if len(data) >= 2:
        # 왼쪽과 오른쪽을 뽑아라
        tmp = [data[0], data[-1]]
        min_value = min(tmp)
        if min_value == data[0]:
            result_letter.append("L")
        else:
            result_letter.append("R")
        # 결과값에 작은값을 추가하고
        result.append(min_value)

        # result에 입력된 값 삭제
        data.remove(min_value)
        # data에 result에 입력된 값보다 작은게 있으면 삭제
        data = list(filter(lambda x: x > min_value, data))

    if len(data) == 1:
        result.append(data[-1])
        result_letter.append("L")
        break
print(result)

for i in result_letter:
    print(i.rstrip("%"), end="")
