import sys

sys.stdin = open("input.txt", "r")
# 0. 인덱스로 분리해야하기 때문에 int가 아닌 문자열로 인풋을 받아온다.
n = input()
########
# 방법 1#
########
# 1. 지금 수와 지금 이전 수를 가르키는 인덱스와 답을 출력할 수 있는 result를 만든다.
# index = 2
# result = 0
# first = int(n[0])
# second = int(n[1])
# 2. index가 len(n)과 같아지면 stop할 때까지 while문
# while True:
#     if index == len(n):
#         break
#     if index == 2:
#         # n[0] 또는 n[1]이 0 이라면, 두 수를 더한 후 result에 저장
#         # 처음 이후 아래 코드는 실행 안됨
#         if first == 0 or first == 1 or second == 0 or second == 1:
#             result = first + second

#         else:
#             result = first * second
#     # 세번째 인덱스 숫자부터
#     # 0과 1이 아니라면 result값에 누적 곱
#     if int(n[index]) != 0 or int(n[index]) != 1:
#         result = result * int(n[index])
#     # 0과 1이라면 result에 누적 합
#     else:
#         result = result + int(n[index])

#     index += 1
# print(result)

########
# 방법 2#
########
# 숫자가 1이하라면 더하기 2이상이면 곱하기
result = int(n[0])
for i in range(1, len(n)):
    num = int(n[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
