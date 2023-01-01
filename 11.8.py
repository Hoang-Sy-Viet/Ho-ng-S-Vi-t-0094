def has_lucky_number(L):
    t=[]
    for ch in L:
         if ch%7==0:
             t=[True]
             break
         else:
             t=[False]
    return print(t[0])
L=[1,2,3,4,5,8]
print(has_lucky_number(L))
