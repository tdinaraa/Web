x = int(input())

if x%4==0 and x%100 or x%400==0:
	print("YES")

else:
	print("NO")