def close_far(a, b, c):
    diffAB = abs(a - b)
    diffAC = abs(a - c)
    diffBC = abs(b - c)

    return (
        (diffAB <= 1 and diffAC >= 2 and diffBC >= 2) !=
        (diffAC <= 1 and diffAB >= 2 and diffBC >= 2)
    )