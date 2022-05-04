import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())

balls = list(map(int, input().split()))

array = [0] * 11
for weight in balls:
    array[weight] += 1
cnt = 0

for i in range(1, m + 1):
    n -= array[i]
    cnt += array[i] * n
print(cnt)

# 경우의 수 문제
# 각 무게별로 공의 갯수를 array에 입력
##->같은 무게를 고르는 경우의 수를 제거 하기 위함
# 특정 무개의 갯수 * 특정 무개의 갯수를 뺀 갯수
##-> 특정 무게의 개별 공이 갖을 수 있는 경우의 총 갯수
##-> 이 갯수를 cnt에 입력
