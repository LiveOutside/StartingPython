alphabet = input()
cross = int(input()) % len(alphabet)
print(alphabet[cross:] + alphabet[:cross])
print(alphabet)
print(alphabet[-cross:] + alphabet[:-cross])


