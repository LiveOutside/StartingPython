numbers = input().split()
last_number = numbers[-1]
number_box = []
answer_is = []
for i in numbers:
    if int(i) not in number_box:
        number_box.append(int(i))
        if (int(i) <= 999) and (int(i) > int(last_number)):
            answer_is.append(int(i))
print(*answer_is, end=' ')
