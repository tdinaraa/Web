import math

def leap(year):
	leap = False

	if year%4==0 and year%100 or year%400==0:
		leap = True

	return leap

year = int(input())
print(leap(year))