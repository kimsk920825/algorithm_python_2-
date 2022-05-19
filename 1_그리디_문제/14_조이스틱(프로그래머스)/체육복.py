# name = "AACAAB"


# def solution(name):
#     # 1. 변수선언
#     r_result = 0
#     l_result = 0
#     answer = 0
#     number = 0
#     forward = []
#     backward = []
#     move_to_right = 1
#     reverse_name = ""
#     check_rA = []
#     check_lA = []
#     # 2. 정방향 알파벳별 변호, 반대방향 알파벳별 번호 각 각 매기고 리스트
#     for f in range(66, 91):
#         forward.append((f - 65, chr(f)))
#     for b in range(90, 65, -1):
#         backward.append(((b - 91) * -1, chr(b)))
#     # 3. 오른쪽 방향
#     for name_i in name:
#         if name_i == "A":
#             r_result += 0
#         else:
#             for i in range(0, 25):
#                 if name_i == forward[i][1]:
#                     check_0 = forward[i][0]
#             for i in range(0, 25):
#                 if name_i == backward[i][1]:
#                     check_1 = backward[i][0]
#             r_result += min(check_0, check_1)
#     r_result += len(name) - 1
#     if name[-1] == "A":
#         reverse_chr = "".join(reversed(name))
#         for i in reverse_chr:
#             if i == "A":
#                 check_rA.append(i)
#             else:
#                 break

#     r_result -= len(check_rA)

#     # 4. 왼쪽방향
#     if name[0] == "A":
#         l_result += 0
#     else:
#         for i in range(0, 25):
#             if name[0] == forward[i][1]:
#                 check_0 = forward[i][0]
#         for i in range(0, 25):
#             if name[0] == backward[i][1]:
#                 check_1 = backward[i][0]
#         l_result += min(check_0, check_1)
#     l_result += 1

#     reverse_name = "".join(reversed(name))
#     reverse_name = reverse_name[:-1]

#     for name_i in reverse_name:
#         if name_i == "A":
#             l_result += 0
#         else:
#             for i in range(0, 25):
#                 if name_i == forward[i][1]:
#                     check_0 = forward[i][0]
#             for i in range(0, 25):
#                 if name_i == backward[i][1]:
#                     check_1 = backward[i][0]
#             l_result += min(check_0, check_1)

#     l_result += len(reverse_name) - 1
#     if reverse_name[-1] == "A":
#         reverse_chr = "".join(reversed(reverse_name))
#         for i in reverse_chr:
#             if i == "A":
#                 check_lA.append(i)
#             else:
#                 break

#     l_result -= len(check_lA)
#     answer = min(r_result, l_result)

#     return answer


# if __name__ == "__main__":
#     a = solution(name)
#     print(a)

name = "BBAAC"
# print(len(name))


def solution(name):
    # 조이스틱 조작 횟수
    answer = 0
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_value = len(name) - 1
    for i, letter in enumerate(name):
        answer += min(ord(letter) - ord("A"), ord("Z") - ord(letter) + 1)

        next = i + 1
        while next < len(name) and name[next] == "A":
            next += 1
        print(i, letter, next)
        min_value = min(
            [min_value, 2 * i + len(name) - next, i + 2 * (len(name) - next)]
        )

    answer += min_value
    return answer


if __name__ == "__main__":
    solution(name)
