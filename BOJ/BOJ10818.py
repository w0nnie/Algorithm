# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

a = int(input())
x = list(map(int,input().split()))
max = x[0]
min = x[0]
for i in x:
    if i < min:
        min = i
    elif i > max:
        max = i
print(min,max)


# import sys

# input = sys.stdin.readline
# N = int(input()) #정수의 개수

# numArr = []
# numArr = list(map(int,input().split()))

# print(min(numArr),max(numArr))

# min , max 함수의 존재를 몰랐다...