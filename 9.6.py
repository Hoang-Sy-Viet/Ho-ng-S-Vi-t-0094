# Kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(x):
    a=True
    if (x<2):
        a=False
        print(a)
        return
    for i in range(2,x):
        if (x%1==0):
            a=False
            break
    print(a)
    return
x=int(input("Nhập x="))
kiem_tra_so_nguyen_to(x)