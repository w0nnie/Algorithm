# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 
# 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고,
#  계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.


a = int(input())
b = int(input())
c = int(input())
d = []
answer = list(map(int,str(a * b * c)))

for _ in range(10):
    d.append(0)

for i in answer:
    if(i == 0):
        d[0] += 1
    elif(i == 1):
        d[1] += 1
    elif(i == 2):
        d[2] += 1
    elif(i == 3):
        d[3] += 1
    elif(i == 4):
        d[4] += 1
    elif(i == 5):
        d[5] += 1    
    elif(i == 6):
        d[6] += 1
    elif(i == 7):
        d[7] += 1
    elif(i == 8):
        d[8] += 1
    elif(i == 9):
        d[9] += 1

for i in d:
    print(i)


# a = int(input())
# b = int(input())
# c = int(input())

# result = list(str(a * b * c))
# for i in range(10):
#     print(result.count(str(i)))