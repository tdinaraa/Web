def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    round = num % 10;

    if round >= 5:
        return num + 10 - round;

    return num - round;