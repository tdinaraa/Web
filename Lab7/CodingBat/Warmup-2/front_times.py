def front_times(str, n):
    new_str = ""

    if len(str) < 3:
        for i in range(n):
            new_str = new_str + str
    else:
        temp = str[:3]

        for i in range(n):
            new_str = new_str + temp

    return new_str