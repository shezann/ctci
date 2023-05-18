def isUnique(word):
    index = 1
    for w in word:
        for num in range(index, len(word)):
            if w == word[num]:
                return False
        index += 1
    return True


print(isUnique('word'))
print(isUnique('wordd'))
print(isUnique('wwordd'))
print(isUnique('false'))
print(isUnique('treu'))
