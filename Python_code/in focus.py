from PIL import Image
image = Image.open('image.png')
pixels = image.load()
x, y = image.size
(min_x, min_y), (max_x, max_y) = (x - 1, y -1), (0, 0)
for i in range(x):
    for j in range(y):
        if pixels[i, j] != pixels[0, 0]:
            if i < min_x:
                min_x = i
            if i > max_x:
                max_x = i
            if j < min_y:
                min_y = j
            if j > max_y:
                max_y = j
image.crop((min_x, min_y), (max_x + 1, max_y + 1)).save('res.png')
