import math
x=int(input("Nhập x:"))
n=int(input("Nhập n:"))
A=math.pow((math.pow(x,2)+x+1),n)+math.pow((math.pow(x,2)-x+1),n)
print(A)