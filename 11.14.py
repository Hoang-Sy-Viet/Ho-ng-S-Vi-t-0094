data = {}
while True:
    key = input("Nhập tên danh bạ: ")
    value = input("Nhập số điện thoại: ")
    if key == "" or value == "":
        break
    data[key] = value
search_name=input('Nhập tên cần tìm số điện thoại: ')
if search_name in data:
    print(search_name,':',data[search_name])
else:
    print(search_name,'không có số điện thoại')
print('-----Danh bạ-----')
for i in data:
    print(f"{i} : {data[i]}")