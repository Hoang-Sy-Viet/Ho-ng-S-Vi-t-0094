s=" a b c d e duck "
s_sub="d"
s_find="duck"
s_replace="dog"
# In chuỗi s
print(s)
# Loại bỏ khoảng trắng ở đầu và ở cuối chuỗi
s1=s.strip()
print(s1)
# In chuỗi với ký tự đầu viết hoa
print(s1.capitalize())
# Đếm và in ra số lần s_sub xuất hiện trong chuỗi s
print(s.count(s_sub,0,14))
''' Tìm kiếm s_find trong s và thay thế s_replace 
in chuỗi sau khí tìm kiếm và thay thế'''
print(s.find(s_find))
print(s.replace("duck",s_replace))
