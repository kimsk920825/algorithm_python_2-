import sys

sys.stdin = open("input.txt", "r")
# for문을 돌려하기 떄문에 문자열로 받아옴
data = input()
change_to_zero = 0
change_to_one = 0
for i in range(len(data) - 1):
    if int(data[i]) == 0 and int(data[i + 1]) == 1:
        change_to_one += 1
    if int(data[i]) == 1 and int(data[i + 1]) == 0:
        change_to_zero += 1
if int(data[-1]) == 1:
    change_to_zero += 1
if int(data[-1]) == 0:
    change_to_one += 1

print(change_to_zero, change_to_one)
