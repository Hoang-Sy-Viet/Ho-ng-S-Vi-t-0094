h=1
t=0
k=[]
while h == 1 :
    t=int(input("nhap phan tu trong list "))
    h=int(input("tiep tuc nhap gia tri co = 1,khong = cac so khac "))
    m=[t]
    k=k+m
print(k)
y=[]
b=2
for so in k:
         snt=[so]
         while (so>=b):
             if (so == 1 ) :
                 y=y+snt
                 b=2
             else:
                 if(so==b):
                     y=y+snt
                     b=2
                     break
                 if (so%b==0):
                     b=2
                     break    
             b+=1 
print("cac so nguyen to trong chuoi la",y)
soam=[]
tbcam=[]
for am in k:
    if am <0:
        soam=[am]
        tbcam+=soam
print("trung binh cong cac so am trong chuoi =",sum(tbcam)/(len(tbcam)))
soduong=[]
tbcduong=[]
for duong in k:
    if duong >0:
        soduong=[duong]
        tbcduong+=soduong
print("trung binh cong cac so duong trong chuoi =",sum(tbcduong)/(len(tbcduong)))
print("gia tri max trong chuoi",max(k))
print("gia tri min trong chuoi",min(k))
print("gia tri chuoi tang",sorted(k))
