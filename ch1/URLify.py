def URLify(string, length):
    words = string.split()
    strArray = list(string)

    index = 0
    count = len(words)
    for word in words:
        for w in word:
            strArray[index] = w
            count += 1
            index += 1
        if count != length+1:
            strArray[index] = "%"
            index += 1
            strArray[index] = "2"
            index += 1
            strArray[index] = "0"
            index += 1

    separator = ''
    return separator.join(strArray)


print(URLify("Mr John Smith    ", 13))
