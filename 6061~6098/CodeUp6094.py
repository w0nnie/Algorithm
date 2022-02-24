n = int(input())
a = list(map(int,input().split()))
ans = a[0]
for i in range(n):
    if ans >a[i]:
        ans = a[i]
    
print(ans)

