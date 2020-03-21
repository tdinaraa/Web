def find_min(a, b, c, d):
    return min(a, min(b, min( c, d)))

numbers = list(map(int, input().split()))

n1 = numbers[0]
n2 = numbers[1]
n3 = numbers[2]
n4 = numbers[3]
print(find_min(n1, n2, n3, n4))