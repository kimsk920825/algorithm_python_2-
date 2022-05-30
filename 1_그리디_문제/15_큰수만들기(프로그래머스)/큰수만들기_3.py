def solution(n, k):
    answer = []
    for i in n:

        if not answer:
            answer.append(i)
            continue
        if k > 0:
            while answer[-1] < i:
                answer.pop()
                k -= 1
                if not answer or k <= 0:
                    break
        answer.append(i)

    answer = answer[:-k] if k > 0 else answer
    return "".join(answer)


if __name__ == "__main__":
    a = solution("1924", 2)
    print(a)
