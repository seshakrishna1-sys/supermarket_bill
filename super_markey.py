from datetime import datetime
name=input("enter your name:")
lists=''' 
rice        rs 20/kg
sugar       rs 30/kg
salt        rs 20/kg
oil         rs 80/liter
paneer      rs 110/kg
maggi       rs 50/kg
boost       rs 90/kg
colgate     rs 85/kg

'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
plist=[]
qlist=[]
#rates for items
items={'rice':20,'sugar':30,'salt':20,'oil':80,'paneer':110,'maggi':50,'boost':90,'colgate':85}
option=int(input("for list of items enter 1 :"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input(" if u want 2 buy press 1 or 2 for exit"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter your quantity:"))
        if item in  items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry item entered by u is not available")
    else:
        print("u entered wrong number")
    inp=input("can i print the items: yes/no")
    if inp=="yes":
        pass
        if finalamount!=0:
            print(25*"=","sesha supermarket",25*"=")
            print(28*" ","bhimavaram")
            print("name:",name,30*" ","date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ","quantity",3*" ","price")
            for i in range(len(pricelist)):
                print(i,8*' ',4*' ',ilist[i],4*' ',3*' ',qlist[i],6*" " ,plist[i])
            print(75*"-")
            print(50*" ",'totalamount:',"rs",totalprice)
            print('gstamount:',40*" ","rs",gst)
            print(75*"-")
            print(50*" ","finalamount:","rs",finalamount)
            print(75*"-")
            print(20*" ","thanks for visisting")
            print(75*"-")



                     

