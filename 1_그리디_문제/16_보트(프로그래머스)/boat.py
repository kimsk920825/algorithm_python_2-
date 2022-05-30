def solution(people, limit):
    answer = 0
    people.sort()
    boat = 0
    for weight in people:
        # 현재 보트에 타있는 사람 무게 + 앞으로 들어올 사람의 무게가 한계보다 크다면
        if boat + weight > limit:
            # print(boat + weight)
            answer += 1  # 기존 보트는 떠나고
            boat = 0  # 새로운 보트를 추가시켜라
        # 보트에 사람을 태워라
        boat += weight
        # print("boat", boat)
    # 만약 보트에 사람이 있다면 해당 보트도 갯수에 추가시켜라.
    if boat:
        answer += 1

    return answer


if __name__ == "__main__":
    a = solution([70, 50, 80, 50], 100)
    print(a)
