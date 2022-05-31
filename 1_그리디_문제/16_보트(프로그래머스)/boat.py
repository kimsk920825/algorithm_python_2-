def solution(people, limit):
    answer = 0
    while people:
        for weight in people:
            temp = limit - weight
            people.remove(weight)
            temp2 = list(filter(lambda x: x <= temp, people))
            if temp2:
                max_data = max(temp2)
                people.remove(max_data)
            answer += 1
            break

    return answer


if __name__ == "__main__":
    a = solution([70, 50, 80, 50], 100)
    print(a)
