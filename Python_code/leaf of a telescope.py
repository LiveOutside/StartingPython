import sys

words = []


def l_func(word, seek):
    global words
    word = list(word)
    for i in seek:
        if i not in word:
            return
        else:
            word.pop(word.index(i))
    words.append(seek)


words_list = [i.strip() for i in sys.stdin]
for i in words_list[1:]:
    l_func(words_list[0], i)
print(len(words))
print(i for i in words)