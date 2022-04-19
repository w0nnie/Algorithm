# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.

def solve():
  c = int(input())
  for _ in range(c):
    avg = 0
    count = 0
    answer = 0
    jumsu = list(map(int,input().split()))
    avg = (sum(jumsu) - jumsu[0]) / jumsu[0]
    for i in jumsu[1:]:
      if i > avg:
        count += 1
        answer = count / jumsu[0] * 100
    print("{:.3f}%".format(answer))

solve()