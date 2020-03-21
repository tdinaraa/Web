n = int(input())
a = list(map(int, input().split()))
f='NO'

for i in range (1,n):
    if (a[i]*a[i-1])>0:
        f='YES'
print(f)