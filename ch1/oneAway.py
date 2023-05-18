def oneAway(str1, str2):
    # if same word
    if (str1 == str2):
        return True

    # if difference is len is greater than 1
    diff = len(str1) - len(str2)
    if (diff > 1 or diff < -1):
        return False

    for i in range(len(str1)):
        new_str1 = str1[:i] + str1[i+1:]
        if (str2.find(new_str1) != -1):
            return True
    return False


print(oneAway('pale', 'pale'))
print(oneAway('pale', 'pa'))
print(oneAway('pale', 'ple'))
print(oneAway('pales', 'pale'))
print(oneAway('pale', 'bale'))
print(oneAway('pale', 'bake'))
