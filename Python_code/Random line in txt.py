import random

with open('lines.txt', encoding='utf-8') as f:
    txt = f.readlines()

if txt:
    print(random.choice(txt))
