import time
t = time.localtime()
time = time.strftime(f"|{'Date : %d-%m-%y ,  %H:%M'}|" , t)
print(time)
product = ["Aloo Parantha","Aloo Pyaz Parantha","Aloo Gobhi Parantha"]
price = [100,140,90]
user = []
pricel = []
qntl = []


print("WELCOME TO MAMA'S PARANTHA".center(100))
i = 0
while i<1:
    
    pro = int(input("1)Aloo Parantha\n2)Aloo Pyaz Parantha\n3)Aloo gobhi Parantha : "))
    qnt = int(input("ENTER QUANTITY: "))

    print(f"you choose {product[pro-1]}")
    user.append(product[pro-1])
#     pricel.append(price[pro-1])
    qntl.append(qnt)

    print(f"Quantity : {qnt}")
    pri = qnt* price[pro-1]
    pricel.append(pri)
    print(f"total price {pri}")

    print("Would you like to add somethink?")
    add = int(input("press 1 for yes \npress 2 for no"))
    if add == 2:
        i+=1
        
    elif add == 1:
        print("sure")
    

print("Generating bil......")


print("-"*100)
print(f"|{'Ratail Invoice':^98}|")
print(f"|{'WELCOME TO MAMAS PARANTHA':^98}|")

print(f"|{'(A Unit Of Saisha foods Pvt Ltd)':^98}|")
print(f"|{'Add:- Shop No, 10, Swarn Path, Mansarovar Sector 3,':^98}|")
print(f"|{'Sector 32, Mansarovar, Jaipur, Rajasthan':^98}|")
print(f"|{'302020':^98}|")
print(f"|{'GSTIN:- 08ABDCS0210P1ZC':^98}|")
print("="*100)
import time
name_time = time.localtime()
time = time.strftime(f"|{' Date: %d-%m-%Y, %H:%M':^96}|", name_time)
print(time)
print(f"|{' Pick up ':<98}|")
print(f"|{' Cashier  : biller':<98}|")

print(f"|{' Bill No. : 59055':<98}|")

print(f"|{' Token No.: 279':<98}|")
print("="*100)
print(f"|{'Product':<40}|{' qty':<28}|{'price':<28}|")
v = 0
while v<len(user):
    print(f"|{user[v]:<40}|{qntl[v]:<28}|{pricel[v]:<28}|")
    v+=1
    
print("="*100)
print(f"|{'total amount':<68}| {sum(pricel):<28}|")

print("="*100)
print(f"|{'FSSAI No. 12220027000066':^98}|")
print(f"|{' Hope You Liked Our Food? ':^98}|")
print(f"|{' Please review us on Google ':^98}|")
print("-"*100)



