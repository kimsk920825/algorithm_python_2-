data = "1231423"
k = 4
tmp_data = []
answer = []
for i, number in enumerate(data):
    number = int(number)
    tmp_data.append((i, number))

while k > 0:
    tmp_max = 0
    tmp_max_i = 0
    # 가장 큰 수
    for i, n in tmp_data:
        if tmp_max < n:
            tmp_max = n
            tmp_max_i = i
    # tmp_max에는 가장 큰 수가 저장되어있음.
    if tmp_max_i + 1 > len(tmp_data) - k:  # <--이 부분이 문제
        tmp_data = tmp_data[:tmp_max_i]
        print(tmp_data)
    else:
        answer.append(tmp_max)
        tmp_data = tmp_data[tmp_max_i + 1 :]
    k -= 1  # < --이 부분이 문제.
print(answer)
