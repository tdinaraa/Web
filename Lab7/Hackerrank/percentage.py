import math
from decimal import Decimal

n = int(input())

dictionary = {}
for i in range(n):
    list = input().split()

    name = list[0]
    values = list[1:]

    dictionary[name] = values

findName = input()

avg = 0
sum = 0
common = len(dictionary.get(findName))
for value in dictionary.get(findName):
    sum = sum + Decimal(value)

avg = sum / common

print("%.2f" % avg)