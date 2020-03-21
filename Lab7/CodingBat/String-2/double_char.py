def double_char(str):
    newstr = ""
    for i in str:
        for j in range(2):
            newstr = newstr + i

    return newstr