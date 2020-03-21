import math

a = int(input())
cnt = 0

for i in range(a):
	k = int(input())
	if k == 0:
		cnt = cnt + 1

print(cnt)