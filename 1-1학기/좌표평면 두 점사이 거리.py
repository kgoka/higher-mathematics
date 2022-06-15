import math

a1,b1 = input("a1의 x, y 좌표를 , 로 나누어서 입력하세요 ").split(',')
a2,b2 = input("a2의 x, y 좌표를 , 로 나누어서 입력하세요 ").split(',')
a1 = int(a1)
b1 = int(b1)
a2 = int(a2)
b2 = int(b2)

print(math.sqrt((a2-a1) ** 2)+math.sqrt((b2-b1) ** 2))

