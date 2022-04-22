# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 
# 그 수를 한수라고 한다. 
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 
# 1보다 크거나 같고, 
# N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오


def solve():
    n = int(input()) 
    count = 0
    arr = []
    for i in range(1,n+1): # 1부터 n까지
        arr = []
        arr = list(map(int,str(i)))
        if i <100:  #각숫자를 다 쪼개서 등차수열인지 판별하기때문에 두자리는 모두 등차수열 판정 ex 97 9 7 
            count += 1
        elif arr[0] - arr[1] == arr[1] - arr[2]: #3자리 등차수열인지 판별
            count += 1
    print(count)

solve()