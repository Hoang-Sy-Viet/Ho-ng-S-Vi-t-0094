
# Tính năm âm lịch từ năm dương lịch
def tinh_can(nam):
    if nam % 10 ==0:
        return "Canh"
    elif nam%10 ==1:
        return "Tân"
    elif nam%10 ==2:
        return "Nhâm"
    elif nam%10 ==3:
        return "Quý"
    elif nam%10 ==4:
        return "Giáp"
    elif nam%10 ==5:
        return "Ất"
    elif nam%10 ==6:
        return "Bính"
    elif nam%10 ==7:
        return "Đinh"
    elif nam%10 ==8:
        return "Mậu"
    else:
        return "Kỷ"
#_______________________________
def tinh_chi(nam):
    if nam % 12 ==0:
        return "Thân"
    elif nam%12 ==1:
        return "Dậu"
    elif nam%12 ==2:
        return "Tuất"
    elif nam%12 ==3:
        return "Hợi"
    elif nam%12 ==4:
        return "Tý"
    elif nam%12 ==5:
        return "Sửu"
    elif nam%12 ==6:
        return "Dần"
    elif nam%12 ==7:
        return "Mão"
    elif nam%12 ==8:
        return "Thìn"
    elif nam%12 ==9:
        return "Tỵ"
    elif nam%12 ==10:    
        return "Ngọ"
    else:
        return "Mùi"
#__________________________________
n=int(input("Nhập vào năm sinh dương lịch: "))
print("Năm sinh theo âm lich của bạn là: ", tinh_can(n),tinh_chi(n))