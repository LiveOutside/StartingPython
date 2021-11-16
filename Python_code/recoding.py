trans = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
         "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
         "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
         "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
         "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
         "б": "b", "ю": "ju", "ё": "jo"}


with open('cyrillic.txt', encoding='utf-8') as file:
    text = file.read()
res = ''
for i in text:
    if i.lower() in trans:
        if i.isupper():
            res += trans[i.lower()].capitalize()
        else:
            res += trans[i]
    else:
        res += i
with open('transliteration.txt', 'w', encoding='utf-8') as file1:
    file1.write(res)

