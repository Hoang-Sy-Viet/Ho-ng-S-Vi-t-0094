def party_late(customers,name):
     s=[]
     d=len(customers)
     for ch in customers:
         x=[ch]
         s+=x
         if (str(ch) == name[0])and(len(s)>((d//2)+1)) :
            t=[True]
            break
         else:
            t=[False]
     return print(t[0])
L=["son","hiep","hoang","duong","minh","manh","quang"]
name=["minh"]
party_late(L,name)