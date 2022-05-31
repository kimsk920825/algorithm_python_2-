# def solution(people, limit):
#     answer = 0
#     #보트에 탈 사람이 있는 경우에만 while 반복
#     while people:
#         #무리에서 한명의 무게 추출
#         for weight in people:
#             #배 1대가 태울 수 있는 사람 무게 제한과 한 사람의 무게 차이
#             temp = limit - weight
#             #태운 사람 무게는 무리에서 제거
#             people.remove(weight)
#             #남은 무게에서 1명 더 태울 수 있는 여유 무게와 같거나 작은 무게 추출 *주의사항: 없을 수 있음.
#             temp2 = list(filter(lambda x: x <= temp, people))
#             #만약 1명 더 태울 수 있는 무게보다 더 적은 몸무게를 갖은 사람들이 있다면
#             if temp2:
#                 #그 중 가장 큰 몸무게를 추출하고
#                 max_data = max(temp2)
#                 #해당 몸무게를 제외
#                 people.remove(max_data)
#             #보트 1대 추가
#             answer += 1
#             #1명 또는 2명을 제외한 상태에서 다시 for문.
#             break

#     return answer
def solution(people, limit):
    answer = 0
    # 보트에 탈 사람이 있는 경우에만 while 반복
    while people:
        # 무리에서 한명을 뽑아라
        temp = people.pop()
        # 배에 temp를 태우고 남는 무게를 구하여라
        temp_spare = limit - temp
        # 남는 여유 무게보다 작은 숫자들을 가려내라
        temp2 = list(filter(lambda x: x <= temp_spare, people))
        # 만약 남는 여유 무게보다 작은 숫자들이 있다면
        if temp2:
            # 그 중 가장 큰 수를 뽑고
            max_data = max(temp2)
            # 해당 무게를 peopled에서 지워라
            people.remove(max_data)
        answer += 1

    return answer


if __name__ == "__main__":
    a = solution([1, 1, 4, 98], 100)
    print(a)
