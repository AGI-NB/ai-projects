A = 1
A += 1
A -= 1
A *= 1
A /= 1
A //= 1
A %= 1
A **= 1
print(A)
A = 10
G = 5
I = 2
print(A - G ** I * I) #优先级：** >（ * ， / ， % ，// ）> （+ ，-）
NB = int(input("请输入一个整数："))
print(NB % 2 == 0) #判断是否为偶数
print(NB % 2 != 0) #判断是否为奇数
print(10 <= NB <= 20) #判断是否在10到20之间
print(NB < 10 and NB > 20) #判断是否小于10且大于20
print(NB < 10 or NB > 20) #判断是否小于10或大于20
print(not (NB < 10 or NB > 20)) #判断是否不在10到20之间