import sys
import heapq

sys.stdin = open("input.txt", "r")

food_times = list(map(int, input().split()))
k = int(input())

if sum(food_times) <= k:
    print(-1)
# 해석
# : 음식을 섭취하는데 총 걸리는 시간이 네트워크와 단전되는 시간과 같거나 작다면,
# k초 후에 섭취하는 음식이 없기때문에 -1
q = []
for i in range(len(food_times)):
    heapq.heappush(q, (food_times[i], i + 1))
sum_value = 0
previous = 0
length = len(food_times)

while sum_value + ((q[0][0] - previous) * length) < k:
    # 먹는데 걸리는 전체 시간 + ((남은 음식을 먹기 위해 걸리는 시간 - 이전 음식을 먹기위해 걸리는 시간) * 길이) < 네트워크가 단절되는 시간
    now = heapq.heappop(q)[0]
    # 리스트 첫 번째 음식을 먹는데 걸리는 시간
    sum_value += (now - previous) * length
    # 리스트 첫 번째 음식을 먹는데 걸리는 시간 - 지난 음식을 먹는데 걸리는 시간 * 길이 = 한 음식을 다 먹기위해선 1바퀴를 음식초만큼 돌아야한다. 즉 첫 번째 음식을 다 먹기 위해서 2초가 걸린다면 그리고 길이가 3이라면 첫 음식을 다 먹기 위해선 6초가 걸린다. 그 다음 음식을 먹는데 걸리는 시간은 다음 음식을 먹는데 걸리는 시간에서 전 음식을 먹는데 걸리는 시간을 빼줘야 한다. 왜냐하면 전 음식을 다 먹기위해서 1바퀴를 돌때마다 다음 음식도 먹었기 때문이다.
    length -= 1
    # 한 음식을 다 먹었다면 전체 길이를 뺴줘라
    previous = now
    # 지금 음식은 이제 전 음식이 된다.

# while문을 빠져나왔다는 것은 음식을 1번 더 회전해서 먹는 시간이 네트워크가 단절되는 시간을 초과했다는 뜻.
result = sorted(q, key=lambda x: x[1])
# 음식 번호를 기준으로 정렬
print(result[(k - sum_value) % length][1])
# 다음에 해석
