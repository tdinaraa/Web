import math

x = int(input())
i = 0

while i<=x:
	if math.pow(2,i)>=x:
		print(i)
		break

	i = i + 1