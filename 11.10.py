
def menu_is_boring(meals):
     s=0
     for food in meals:
         if str(s)==str(food):
            t=[True]
            break
         else:
            t=[False]
         s=food
     return print(t[0])
meals1=["Redneck Ribs","Prawn Star","San Quentin Squid","Fist Full of Pizza","Honky Tonk Chicken"]
menu_is_boring(meals1)

