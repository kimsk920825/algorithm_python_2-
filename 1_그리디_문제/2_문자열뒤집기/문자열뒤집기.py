import sys

sys.stdin = open("input.txt", "r")
# 0. 인덱스로 분리해야하기 때문에 int가 아닌 문자열로 인풋을 받아온다.
n = input()

count0 = 0  # 다음 숫자를 0으로 바꿀 때
count1 = 0  # 다음 숫자를 1로 바꿀 때

if n[0] == "1":
    count0 += 1
    print("count0", count0)
else:
    count1 += 1
    print("count1", count1)
cnt = 0
for i in range(len(n) - 1):
    if n[i] != n[i + 1]:
        # print(cnt, ":", n[i], n[i + 1])
        cnt += 1
        if n[i + 1] == "1":
            count0 += 1
            # print("다음 수가 1일때", n[i + 1])
            # print(count0)
        else:
            count1 += 1
            # print("다음 수가 0일때", n[i + 1])
            # print(count1)
# print("미니멈값:", min(count0, count1))
# print(count0, count1)
