def palinPerm(string):
    result = {
        "found": True,
        "perms": []
    }
    str_lower = string.lower()
    str_letters_only = str_lower.replace(" ", "")

    alphabet = {}
    for i, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
        alphabet[char] = 0

    for w in str_letters_only:
        alphabet[w] += 1

    if (len(str_letters_only) % 2 == 0):
        for i in alphabet:
            if alphabet[i] % 2 != 0:
                result["found"] = False
                return result
    else:
        for i in alphabet:
            if alphabet[i] != 0:
                if alphabet[i] % 2 != 1:
                    result['found'] = False
                    return result

    return result


print(palinPerm('Tact coa')["found"])
print(palinPerm('adda')["found"])
