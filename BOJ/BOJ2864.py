a,b =input().split()
min = int(a.replace('6','5')) + int(b.replace('6','5'))
max = int(a.replace('5','6')) + int(b.replace('5','6'))
print(min,max)

# 간단하게 replace 함수를 이용하여 푼다... 는데 나 잘모르겠다 
# replace 함수는 문자열에서 어떠한 값을 찾아 바꿔주는 역할
# min == 6-> 5 max == 5-> 6 
# 이런생각을 어떻게하는걸까.. 