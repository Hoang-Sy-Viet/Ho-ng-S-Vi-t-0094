def elementwise_greater_than(L,thresh):
    y=[]
    f=[False]
    t=[True]
    for ch in L:
         if ch<=thresh:
             y=y+f
         else:
             y=y+t
    return print(y)
L=[1,2,3,4,5]
print(elementwise_greater_than(L,2))