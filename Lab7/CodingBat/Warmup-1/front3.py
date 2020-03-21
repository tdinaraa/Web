def front3(str):
    if len(str) < 3:
        return str + str + str

    temp = str[:3]

    return temp + temp + temp