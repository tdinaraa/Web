def diff21(n):
    difference = 0
    if n > 21:
        difference = (21 - n) * 2

    else:
        difference = (21 - n)

    return abs(difference)