a = int(input())
list = [int(i) for i in input().split()]
i = len(list)-1

while i>=0:
	print(list[i], end = ' ')
	i = i -1
