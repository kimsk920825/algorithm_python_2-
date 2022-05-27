data = "1231423"
k = 4
tmp_data = []
answer = []
f_index = 0
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
    # print(tmp_max, tmp_max_i)
    # tmp_max에는 가장 큰 수가 저장되어있음.
    if tmp_max_i >= len(data) - k:  # <--이 부분이 문제
        for i, number in enumerate(data[:tmp_max_i]):
            number = int(number)
            tmp_data = []
            tmp_data.append((i, number))
        # print("tmp_max_i초과", tmp_data)
    else:
        answer.append(tmp_max)
        for i, number in enumerate(data[tmp_max_i + 1 :]):
            number = int(number)
            tmp_data = []
            tmp_data.append((i, number))
        # print("tmp_max_i미만", tmp_data)
    k -= 1  # < --이 부분이 문제.
print(answer)
