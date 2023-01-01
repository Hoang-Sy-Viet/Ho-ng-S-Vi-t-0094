a = float(input("cạnh thứ nhất ="))
b = float(input("cạnh thứ hai ="))
c = float(input("cạnh thứ ba ="))
#p là nửa chu vi
p =(a+b+c)/2
# s là diện tích tam giác 
import math
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
print ("diện tích tam giác là :",s,           " :))")

