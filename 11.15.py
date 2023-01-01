data={"hello": "xin chào", "goodbye": "tạm biệt", "dog": "chó", "cat": "mèo"}
while True:
    a=int(input('Bạn muốn làm gì? 1:Xem từ điển; 2:Tra từ; 3:Thêm từ; 4: Xóa từ     '))
    if a==1:
        print('-----Từ điển Anh-Việt-----')
        key_max_length = max(len(key) for key in data)
        value_max_length = max(len(value) for value in data.values())
        print(f"{'Từ Anh':<{key_max_length}}         {'Nghĩa Việt':<{value_max_length}}")
        for key, value in data.items():
            print(f"{key:<{key_max_length}}          {value:<{value_max_length}}")
    if a==2:
        b=input('Nhập từ cần tra:')
        if b in data:
            print(b,':',data[b])
        else:
            print(b,'không có trong từ điển')
    if a==3:
        key = input("Nhập từ Anh: ")
        value = input("Nhập nghĩa Việt: ")
        data[key]=value
    if a==4:
        b=input('Nhập từ cần xóa: ')
        del data[b]
        print(f'Đã xóa từ {b} trong từ điển')      
    b=int(input('Tiếp tục lựa chọn? 1: Có, 0: Không   '))
    if b==0:
        break
    else:
        continue