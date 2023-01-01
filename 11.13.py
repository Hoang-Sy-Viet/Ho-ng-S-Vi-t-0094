set1=set()
set2=set()

#Nhập set1
while True :
    a=int(input("Nhập giá trị cho element trong set 1:"))
    set1.add(a)
    b=int(input('Bạn có tiếp tục nhập set 1? 1: có, khác 1: không   '))
    if b != 1:
        break
    else:
        continue
#Nhập set2
while True:
    a=int(input("Nhập giá trị cho element trong set 2:"))
    set2.add(a)
    b=int(input('Bạn có tiếp tục nhập set 2? 1: có, khác 1: không   '))
    if b != 1:
        break
    else:
        continue
#In set1, set2
print('Set 1 =',set1)
print('Set 2 =',set2)
#Tính số phần tử có trong set và tổng giá trị các phần tử có trong set
print("Chiều dài của Set 1:", len(set1))
print("Chiều dài của Set 2", len(set2))
#Tổng giá trị các phần tử trong set 1
print('Tổng Set 1',sum(set1))
#Tổng giá trị các phần tử trong set 2
print('Tổng Set 2',sum(set2))
#Min max mỗi set
print('Max Set 1:', max(set1))
print('Min Set 1:', min(set1))
print('Max Set 2', max(set2))
print('Min Set 2', min(set2))
set3=set1 | set2
print('Set 1 union Set 2',set3)
set4=set1.intersection(set2)
print('Set 1 intersection Set 2',set4)
set5=set1.difference(set2)
print('Set 1 difference set 2',set5)
set7=set1^set2
print('Set 1, Set 2 symmetric differnce',set7)
#Sắp xếp set 1 tăng dần và set 2 giảm dần
print('Sorted set 1:',sorted(set1))
print('Sorted reversed set 2:',sorted(set2,reverse=True))