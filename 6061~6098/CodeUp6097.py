h, w = map(int,input().split())

a =[]
for i in range(h+1):
  a.append([])
  for j in range(w+1):
    a[i].append(0)
    
n = int(input())
for i in range(n):
  l,d,x,y = map(int,input().split())
  if d==0:
    for j in range(l):
      a[x-1][y-1+j] =1
  else:
    for j in range(l):
      a[x-1+j][y-1] =1

for i in range(h) :
  for j in range(w) : 
    print(a[i][j], end=' ')
  print()  
