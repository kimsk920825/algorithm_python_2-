import sys

sys.stdin = open("input.txt", "r")

##방법1##

number, maximum = map(int, input().split())
weights = list((map(int, input().split())))
weights.sort()
cnt = 0

while True:
    # 만약 모든 승객이 다 탐습했다면 break
    if len(weights) == 0:
        break
    # 보트가 감당할 수 있는 몸무게가 넘어가면 리스트에서 버린다.
    if weights[-1] > maximum:
        impossible = weights.pop(len(weights) - 1)
    # 가장 무거운 사람을 뽑는다.
    heaviest = weights.pop(len(weights) - 1)
    print("heaviest--->", heaviest)
    # 추가 수용 무게 = 보트가 수용할 수 있는 무게 - 가장 무거운 사람
    available = maximum - heaviest
    print("available--->", available)
    # 추가 수용 가능 무게 추출
    available_list = list(filter(lambda x: x <= available, weights))
    # available_list에 값이 없다는 뜻은 남은 몸무게 리스트에 수용가능 몸무게보다 낮은 몸무게가 없으므로 cnt가 올라간다.
    if sum(available_list) == 0:
        cnt += 1
    # 무게를 누적시킬 total변수를 만든 후
    total = 0
    # 추가 가능 무게 하나씩을 돌면서

    # 만약 availabe을 추가 한다면 for문 끝냄

    # 해당 무게를 weights에서 제외시키고
    # cnt는 증가
    for weight in available_list:

        print("weight--->", weight)
        # total의 무게가 available보다 작은지 확인 후
        if total > available:
            break
        # 아니라면 total에 무게를 누적시키고,
        else:
            total += weight
            weights.remove(weight)
            cnt += 1
print(cnt)

##방법2##
