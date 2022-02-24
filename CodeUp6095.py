d = []                  #list를 만들어주고
for i in range(20):     #19*19 바둑판 에 i,j 열에 0을 다 채워줌
    d.append([])
    for j in range(20):
        d[i].append(0)
        
n = int(input())        #입력받을 횟수를 입력받음
for i in range(n):      #n번만큼 x축 , y축을 입력받고 그값에 1을 넣어줌
    x,y = map(int,input().split())
    d[x][y] = 1
    
for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end=' ') #공백을 주고 한줄로 출력 후 줄바꿈
    print()
    
    