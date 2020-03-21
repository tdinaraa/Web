def string_match(a, b):
    cnt = 0

    for i in range(min(len(a), len(b)) - 1):
        subA = a[i:i + 2]
        subB = b[i:i + 2]

        if subA == subB:
            cnt = cnt + 1

    return cnt