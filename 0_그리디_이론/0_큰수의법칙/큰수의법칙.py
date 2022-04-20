import sys

sys.stdin = open("input.txt", "r")

# N은 배열의 크기, M은 숫자가 더해지는 횟수, K는 한 인덱스에 있는 수가 더해질 수 있는 최대 횟수.
N, M, K = map(int, input().split())
array = list(map(int, input().split()))
############
# 첫 번째 풀이 #
############
# # 1.숫자를 큰 수부터 정렬한다.
# array = sorted(array, reverse=True)
# # 2.가장 큰 수와 두 번쨰로 큰 수를 변수에 입력
# first = array[0]
# second = array[1]
# # 2. K미만일때까지 높은 인덱스 누적
# result = 0
# print(N, M, K, array, first, second, result)
# while True:
#     for _ in range(K):
#         if M == 0:
#             break
#         result += first
#         M -= 1
#     if M == 0:
#         break
#     result += second
#     M -= 1
# print(result)

############
# 두 번째 풀이 #
############

# 1. M횟수에 K+1이 몇 번 들어갈 수 있는지 계산 후 K를 곱하라
count = int(M / (K + 1)) * K
# 2. 나머지 또한 횟수에 추가
count += M % (K + 1)
# 3. 가장 큰 값, 두 번째로 큰 값
array.sort(reverse=True)
first = array[0]
second = array[1]
# 4. 가장 큰 값 계산
result2 = first * count
# 5. 두 번째 큰값 계산 결과값에 대임
result2 += second * (M - count)

print(result2)
