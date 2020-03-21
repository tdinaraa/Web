a = int(input())
list = [int(i) for i in input().split()]
cnt = 0

for i in range(len(list)):
	if list[i]>0:
		cnt = cnt+1

print (cnt)
