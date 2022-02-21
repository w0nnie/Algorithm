a, r, n = map(int,input().split())
sum = a
for i in range(1,n):
    sum = sum * r
print(sum)    