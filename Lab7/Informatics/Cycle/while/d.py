import math

x = int(input())
isPowerOfTwo = False

for i in range(x):
	if math.pow(2,i) == x:
		isPowerOfTwo = True

if isPowerOfTwo:
	print("YES")
else:
	print("NO")