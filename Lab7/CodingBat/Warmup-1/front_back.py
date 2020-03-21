def front_back(str):
    if len(str) <= 1:
        return str
    mid = str[1:-1]

    f = str[0]
    l = str[len(str) - 1]

    return l + mid + f