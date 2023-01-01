h=1
t=0
k=[]
while h == 1 :
    t=int(input("nhap phan tu trong list "))
    h=int(input("tiep tuc nhap gia tri co = 1,khong = 0 "))
    m=[t]
    k=k+m
print(k)
print("tong cua chuoi vua nhap",sum(k))
x=int(input("nhap so x "))
ktr=(x)in k
if ktr == True:
    print(x,"xuat hien",k.count(x),"lan")
else:
    print("khong co ",x)
to=max(k)
if x>=to:
    print(x,"la so lon nhat trong chuoi vua nhap")
else:
     y=[]
     for so in k:
         if so > x:
             lonhonx=[so]
             y=y+lonhonx
     print("so lon hon",x,"trong chuoi la",y)
    