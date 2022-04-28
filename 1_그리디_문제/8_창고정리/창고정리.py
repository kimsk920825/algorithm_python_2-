import sys

sys.stdin = open("input.txt", "r")
# M회를 돈다
# 매회를 돌때마다
## 숫자를 작은숫자부터 나열한다.
# 가장 높은 숫자에서 -1
# 가장 낮은 숫자게엇 +1
n = int(input())
box_height = list(map(int, input().split()))
cnt = int(input())
box_height.sort()
for _ in range(cnt):
    box_height[0] = box_height[0] + 1
    box_height[-1] = box_height[-1] - 1
    box_height.sort()


print(box_height[-1], box_height[0])
