from sys import exit
with open(input()) as file:
    dress_colors = [color.split()[1] for color in file.readlines()]
with open(input()) as file2:
    coolItems = [c.split() for c in file2.readlines()]
print(coolItems)
colorName = input()
colorIndex = dress_colors.index(colorName)
res = []
for item in coolItems:
    for j in item:
        if int(j) > len(dress_colors) or len(item) == 0:
            with open('regards.txt', 'w') as file3:
                file3.writelines('Error')
                exit()
for i in coolItems[colorIndex]:
    res.append(dress_colors[int(i) - 1])
with open('regards.txt', 'w') as file3:
    file3.writelines('\n'.join(res).strip())

