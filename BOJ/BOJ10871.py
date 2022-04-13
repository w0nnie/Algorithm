# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

n,min = map(int,input().split())
x = list(map(int,input().split()))
for i in x:
    if i < min:
        print(i,end=" ")

# for 문에 in range와 혼동했다 for i in x 는 x까지 for문을 돌리는건 맞지만 x의 i번째의 값을 나타낸다
# x[i]로 생각하는게 맞을거같다 i번쨰 값을 다 비교하여 min보다 작은값들만 print한다