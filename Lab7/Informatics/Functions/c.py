def xor(x,y):
	if x == y and x==1  or x==y and x==0:
		return 0

	return 1

a,b  = input().split()

print(xor(int(a),int(b)))