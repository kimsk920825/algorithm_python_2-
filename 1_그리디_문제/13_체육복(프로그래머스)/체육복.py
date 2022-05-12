import sys


sys.stdin = open("input.txt", "r")

# 체육복이 도난 당함.
# 체육복은 앞,뒤번호 학생에게만 빌려줄 수 있음.
# 최대한 많은 학생이 체육수업에 참가해야함.
# 전체 학생수 n
# 체육복을 도난당한 학생들의 번호가 담긴 배열 ㅣost
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reverse
# 최대값을 return

##제한사항
##전체 학생수는 2명 ~ 30명
##체육복을 도난당한 학생 수는 1명 이상 n명 이하
##여벌의 체육복을 가져온 학생의 수는 1명이상 n명 이하. 중복되는 번호는 없음
##여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정.
##남은 체육복이 하나이기에 다른 학생에게 빌려줄 수 없다.

# 만약 reverse값의 i-1이 lost에 있다면 lost에서 i-1 제거 그리고 continue
# 만약 reverse값의 i+1이 lost에 있다면 lostd에서 i+1 제거 그리고 continue
# 총 lost 길이를 n에서 뺀 값 return
n = 5
lost = [2, 4]
reverse = [3]


# def solution(n, lost, reverse):
#     for i in lost:
#         if i in reverse:
#             lost.remove(i)
#             reverse.remove(i)
#     for i in reverse:
#         if i - 1 in lost:
#             lost.remove(i - 1)
#             continue
#         if i + 1 in lost:
#             lost.remove(i + 1)
#             continue
#     answer = n - len(lost)
#     return answer


# def solution(n, lost, reserve):
#     reserve = set(reserve)  # reserve 를 집합으로 바꾼다.
#     for size in [0, 1, -2]:
#         lost = set(map(lambda x: x + size, lost))
#         reserve, lost = reserve - lost, lost - reserve
#     return n - len(lost)
def solution(n, lost, reserve):
    before_cloth_list = [1] * n
    after_cloth_list = [0] * n

    # 체육복을 가지고 있는지 없는지 확인하기
    for student in range(1, n + 1):
        if student in lost:
            before_cloth_list[student - 1] -= 1
        if student in reserve:
            before_cloth_list[student - 1] += 1
    for student, cloth in enumerate(before_cloth_list):
        # 옷이 없는 학생이라면 그대로 after cloth list에 0
        if cloth == 0:
            continue
        # 옷이 1개있는 학생이라면 after cloth list에 1
        if cloth == 1:
            after_cloth_list[student] = 1
            continue
        # 나머지는 모두 옷이 2개있는 항생
        after_cloth_list[student] = 1
        # 지금 학생이 첫 학생인지 아닌지 확인하고, 만약 아니라면 이전 학생의 옷이 0인지 확인하고 만약 0이라면 옷을 주자
        if student != 0:
            if after_cloth_list[student - 1] == 0:
                after_cloth_list[student - 1] = 1
            continue
        # 지금 학생이 마지막 학생이 아닌지 확인하고, 만약에 마지막 학생이 아니라면
        # 뒤의 학생은 앞의 학생을 점검 후 뒤를 점검하기때문에 아직 옷을 못받았을 경우를 생각하여 옷을 배분전 리스트를 사용한다
        if student != len(before_cloth_list) - 1:
            if before_cloth_list[student + 1] == 0:
                after_cloth_list[student + 1] = 1
                continue
    return after_cloth_list.count(1)


if __name__ == "__main__":
    a = solution(n, lost, reverse)
    print(a)


###가정1
###학생수 5명
###1,2번이 체육복을 안가져옴
###3,5번만 여유복이 있고 4번은 없음
###lost = [1,2], reverse=[3,5]
###1.lost안에 있는 값이 reverse에도 있다면 lost와 reverse모두에서 제외.
###2.lost 첫 번째 값 1 양 옆의 숫자 1+1 또는 1-1이 reverse에 있다면 lost에서 1 제외
###3.lost 두 번째 값 2 양 옆의 숫자 2+1, 2-1이 reverse에 있다면 lost에서 2 제외
###4.lost길이를 전체 학생숫자에서 뺀 값이 return값

###가정2
###학생수 5명
###2,4번이 체육복을 안가져옴
###1,3,5번은 여벌이 있음
###lost = [2,4], reverse = [1,3,5]
###만약 len(lost) < len(reverse)라면
###reverse에 있는 값 양옆을 확인
###reverse의 양 옆을 확인했을때 lost값이 둘 다 없을때마다 해당값 reverse에서 제외
###제외 후 len(reverse)값이 len(lost)와 같거나 크다면 n 모두 참석 가능
###제외 후 len(reverse)값이 len(lost)값보다 작다면 n-(len(lost)-len(reverse))

###만약 len(lost) > len(reverse)라면
###만약


###가정3
###만약 lost보다 reverse가 많다면 전원 참석 가능??
###1,2번이 체육복이 없고 5번만 여벌이 있다면 불가능

###가정4
###lost = [2,4]
###reverse = [3]
###n=5
### reverse의 i-1, i+1이 모두 lost에 있는데 reverse가 lost보다 작다면 return = n - (len(lost) - len(reverse))??
