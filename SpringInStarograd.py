n = int(input())
for i in range(n):
    first = set(input().split())
    second = set(input().split())
    print(' '.join(first.difference(second)))