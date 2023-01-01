# Xác định khách đến dự tiệc muộn hay không
def party_late(arrivals, name):
    return name in arrivals
arrivals=['Adela','Fleda','Owen','May','Mora','Gilbert','Ford']
print(party_late(arrivals,name='Gilbert'))
print(party_late(arrivals,name='Tony'))
print(party_late(arrivals,name='Mora'))