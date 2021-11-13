import sys

n = 0
for i in sys.stdin:
    s = 0
    w = i.split()
    for j in w:
        if s == 1:
            continue
        if j.lower().startswith('далек'):
            n += 1
            s += 1
print(n)
