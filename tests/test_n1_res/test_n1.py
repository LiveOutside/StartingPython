with open(input()) as file:
    colors = [color.split()[1] for color in file.readlines()]
with open(input()) as file2:
    coolItems = [c.split() for c in file2.readlines()]
colorName = input()

colorIndex = colors.index(colorName)
res = []
for i in coolItems:
    for j in i:
        if int(j) > len(colors) or int(j) == 0 or int(j) < 0:
            with open('regards.txt', 'w') as file3:
                file3.writelines('Error')
                break
for i in coolItems[colorIndex]:
    if int(i) - 1 != colorIndex and colors[int(i) - 1] not in res:
        res.append(colors[int(i) - 1])
with open('regards.txt', 'w') as file3:
    file3.writelines('\n'.join(res).strip())
