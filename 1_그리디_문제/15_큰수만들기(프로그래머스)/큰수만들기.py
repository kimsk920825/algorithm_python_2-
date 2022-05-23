given_number = "1231234"
k = 3
q = len(given_number) - k
big_number = []

result = 0
result2 = 0
temp = given_number[0:-k]

for i in temp:
    i = int(i)
    if result < i:
        result = i
result = str(result)
big_number = big_number.append(result)
k -= 1
index = given_number.find(result)
while k > 0:
    temp2 = given_number[index + 1, -k]
    for i in temp2:
        i = int(i)
        if result2 < i:
            result2 = i
    index = given_number.find(result2)
    result2 = str(result2)
    big_number = big_number.append(result2)
    k -= 1
print(big_number)

# 제일큰수를 제외한 나머지 숫자 + given_number[-k+1]


# while k > 0:
#     result = 0
#     temp = given_number[0:-k] #<--문제

#     # print("temp", temp)
#     for i in given_number[0:-k]:
#         i = int(i)
#         if result < i:
#             result = i
#     result = str(result)
#     index = given_number.find(result)
#     # given_number = given_number[index + 1 : -k + 1] #<--문제
#     print("수정", given_number)
#     temp2.append(result)
#     k -= 1
# # print(temp2)
# answer = "".join(temp2)
# print(answer)
