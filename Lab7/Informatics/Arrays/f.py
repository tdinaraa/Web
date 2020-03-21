a = int(input())
list = [int(i) for i in input().split()]

cnt = 0
for i in range(len(list)):
	if i+1<len(list) and i-1>=0:
		if list[i]>list[i+1] and list[i]>list[i-1]:
			cnt = cnt+1

print(cnt)