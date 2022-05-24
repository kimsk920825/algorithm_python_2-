# )주어지는 정보
n = "1231234"
k = 3
# 1) n의 개별 숫자와 해당 인덱스를 묶어 data리스트에 저장
data = []
index = 0
for i in n:
    data.append((index, i))
    index += 1
# 2) 변수지정
# 2-1)처음에는 데이터의 첫 인덱스, 두 번째 부터는 큰 수 인덱스 + 1
f_index = 0
# 2-2)큰 수를 뽑을 범위를 지정해주는 컨트롤 인덱스. 매번 1씩 증가
b_index = 0
# 2-3)정해진 범위에서 가장 큰 수
mx = 0
# 2-4)정해진 범위에서 가장 큰 수의 인덱스
mx_i = 0
# 2-5)답을 저장할 리스트
answer = []
while True:
    # 3)만약 len(data[f_index:]) == len(data) - (-1*(-k+b_index)) answer에 data[f_index:]의 데이터값 저장
    if len(data[f_index:]) == len(data) - (
        -1 * (-k + b_index)
    ):  # <-- 5월 24일 화요일: 논리가 맞는지 확인하기.
        for i, number in data[f_index:]:
            answer.append(number)
        break
    # 4)만약 f_index == len(n) -1 이라면, answer.append(data[-1][1]) <-- data[-1][1]데이터 타입은 문자형
    # 그리고 break
    if f_index == len(n) - 1:
        answer.append(data[-1][1])
        break
    # 5)큰 수를 만들 범위
    temp = data[f_index : -k + b_index]
    # 6)범위안에서 인덱스와 숫자 나눠 반복문 실행
    for i, number in temp:
        # 6-1)숫자 정수형으로 변환
        number = int(number)
        # 6-2)만약 현 숫자가 mx보다 크다면
        if mx < number:
            # 6-3)mx에 현 숫자 저장
            mx = number
            # 6-4)mx_i에 현 숫자의 인덱스 저장
            mx_i = i
    # 7)mx의 데이터 타입을 문자형으로 변환
    mx = str(mx)
    # 8)answer에 인덱스와 숫자 저장
    answer.append((mx_i, mx))  # <-- mx_i데이터 타입 int, mx데이터 타입 str
    # 9)f_index는 가장 큰 수 인덱스 앞 인덱스로 지정
    f_index = mx_i + 1
    # 9)b_index는 하나씩 증가
    b_index = b_index + 1
print(answer)
