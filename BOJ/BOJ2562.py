# 9개의 서로 다른 자연수가 주어질 때, 
# 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

n = 9
x = []
count = 0
for i in range(n):
    a = int(input())
    x.append(a)

for i in x:
    count += 1
    if i >= max(x):
        break

print(max(x))
print(count)
 