n = int(input())
s = list(map(int, input().split(" ")))
cnt = 0

for i in range(n):
    if i - 1 < 0:
        continue
    if s[i] > s[i-1]:
        cnt += 1
print(cnt)