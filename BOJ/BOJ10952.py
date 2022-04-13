# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

while True:
    a,b = map(int,input().split())
    sum = a + b  
    if a==0 and b==0:
        break
    else:
        print(sum)
        
# 예제 출력 그래도 할필요가 없는건가 ? 
# 나의 답은 입력하면 print를 하고  0 0을 입력하기 전까지
# 또 입력받는다
# 1 1
# 2
# 2 3 이런식인데 예제 출력에는 합계만 쭉나와야하는거아닌가
# 흠 이게 왜 맞는거지 