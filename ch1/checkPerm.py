def checkPerm(str1, str2):
    # find the smaller word
    smallStr = ""
    bigStr = ""
    if (len(str2) < len(str1)):
        smallStr = str2
        bigStr = str1

        for w in smallStr:
            if w not in bigStr:
                return False

    elif (len(str2) == len(str1)):
        smallStr = str2
        bigStr = str1

        for w in smallStr:
            if w not in bigStr:
                return False

        for w in bigStr:
            if w not in smallStr:
                return False

    return True


print(checkPerm('abcd', 'abcc'))
