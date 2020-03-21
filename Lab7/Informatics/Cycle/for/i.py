x = int(input())
d = 0

for i in range(1, int((x ** 0.5)) + 1):
    if x % i == 0 and i * i != x:
        d += 2
    elif i * i == x:
        d += 1

print(d)