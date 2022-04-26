import sys
import heapq

sys.stdin = open("input.txt", "r")

food_times = list(map(int, input().split()))
k = int(input())
print(food_times)
print(k)
# food times에서 data 추출
# 추출된 데이터에서 -1 차감
# 만약 추출된 데이터가 0이 된다면 continue
# cnt 1씩 증가
# 만약 cnt가 k와 같다면 같을때의 food_times 인덱스값 추출
# 만약 리스트 합이 1보다 작을 때 그리고 cnt가 k보다 작다면 -1 return.

if sum(food_times) <= k:
    print(-1)

# q리스트를 최소힙으로 만드는 과정
q = []
for i in range(len(food_times)):
    # 음식 시간, 음식 번호로 입력
    heapq.heappush(q, (food_times[i], i + 1))
print(q)

# 먹는데 걸리는 시간
sum_value = 0
# 이전에 먹었던 시간
previous = 0
# 총 음식의 갯수
length = len(food_times)

while sum_value + ((q[0][0] - previous) * length) < k:
    now = heapq.heappop(q)[0]
    sum_value += (now - previous) * length
    length -= 1
    previous = now

result = sorted(q, key=lambda x: x[1])
print(result[(k - sum_value) % length][1])
