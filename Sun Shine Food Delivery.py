# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 00:37:48 2020

@author: Partha
"""
import pickle as p
import random as r
import pymysql as sql

def verify():
    while True:
        st = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        a = ""
        for i in range(0, 6):
            ln = len(st)
            a = a+st[r.randint(0, ln-1)]
        print("Type the shown Captcha Code", a)
        x = input("Type Here")
        if x == a:
            return True
        else:
            print("Wrong Captcha Code entered")

def place():
    print("Select Your Location\n1.Kolkata\n2.Mumbai\n3.Delhi\n4.Chennai\n5.Bangalore\n6.Guwahati")
    location = int(input("Enter your choice -->"))
    while True:
        if location == 1:
            print("List of Available Restaurants in  Kolkata:\n",
                  "1.Abar Khabo\nAverage Cost per person --> Rs. 200\nRating --> 3.9/5\n\n",
                  "2.Bonnagor\nAverage Cost per person --> Rs. 150\nRating --> 4.2/5\n\n",
                  "3.Theque\nAverage Cost per person --> Rs. 200\nRating --> 3.0/5\n\n",
                  "4.Taste of Hill\nAverage Cost per person --> Rs. 250\nRating --> 4.4/5\n\n",
                  "5.Khatta Meetha\nAverage Cost per person --> Rs. 150\nRating --> 3.7/5\n\n")
            break
        elif location == 2:
            print("List of Available Restaurants in Mumbai:\n",
                  "1.Indiana\nAverage Cost per person --> Rs. 200\nRating --> 3.9/5\n\n",
                  "2.Mainland China\nAverage Cost per person --> Rs. 150\nRating --> 4.2/5\n\n",
                  "3.Mumma's Kitchen\nAverage Cost per person --> Rs. 200\nRating --> 3.0/5\n\n",
                  "4.Sizzling Grass\nAverage Cost per person --> Rs. 250\nRating --> 4.4/5\n\n",
                  "5.Fooodie's Area\nAverage Cost per person --> Rs. 150\nRating --> 3.7/5\n\n")
            break
        elif location == 3:
            print("List of Available Restaurants in Delhi:\n",
                  "1.So Tasty\nAverage Cost per person --> Rs. 200\nRating --> 3.9/5\n\n",
                  "2.Grassy Fussy\nAverage Cost per person --> Rs. 150\nRating --> 4.2/5\n\n",
                  "3.Delta Suites\nAverage Cost per person --> Rs. 200\nRating --> 3.0/5\n\n",
                  "4.Hotel Anand\nAverage Cost per person --> Rs. 250\nRating --> 4.4/5\n\n",
                  "5.Food Mart\nAverage Cost per person --> Rs. 150\nRating --> 3.7/5\n\n")
            break
        elif location == 4:
            print("List of Available Restaurants in Chennai:\n",
                  "1.Hot N Swwet\nAverage Cost per person --> Rs. 200\nRating --> 3.9/5\n\n",
                  "2.Sizzlicious\nAverage Cost per person --> Rs. 150\nRating --> 4.2/5\n\n",
                  "3.Theque\nAverage Cost per person --> Rs. 200\nRating --> 3.0/5\n\n",
                  "4.Taste of Hill\nAverage Cost per person --> Rs. 250\nRating --> 4.4/5\n\n",
                  "5.Parallax Restaurant\nAverage Cost per person --> Rs. 150\nRating --> 3.7/5\n\n")
            break
        elif location == 5:
            print("List of Available Restaurants in Bangalore:\n",
                  "1.Sky Dinner\nAverage Cost per person --> Rs. 200\nRating --> 3.9/5\n\n",
                  "2.Chez Panisse Cafe\nAverage Cost per person --> Rs. 150\nRating --> 4.2/5\n\n",
                  "3.Pine & Dine\nAverage Cost per person --> Rs. 200\nRating --> 3.0/5\n\n",
                  "4.The Glass Onion\nAverage Cost per person --> Rs. 250\nRating --> 4.4/5\n\n",
                  "5.Bakers Area\nAverage Cost per person --> Rs. 150\nRating --> 3.7/5\n\n")
            break
        elif location == 6:
            print("List of Available Restaurants in Guwahati:\n",
                  "1.Life of Pie\nAverage Cost per person --> Rs. 200\nRating --> 3.9/5\n\n",
                  "2.Meal Cage\nAverage Cost per person --> Rs. 150\nRating --> 4.2/5\n\n",
                  "3.Green Cafe\nAverage Cost per person --> Rs. 200\nRating --> 3.0/5\n\n",
                  "4.Havemore\nAverage Cost per person --> Rs. 250\nRating --> 4.4/5\n\n",
                  "5.Silver Platter\nAverage Cost per person --> Rs. 150\nRating --> 3.7/5\n\n")
            break
        else:
            print("Wrong Input!!!Please Try Again")
            continue
    rch = int(input("Enter your choice of restaurant(1/2/3/4/5)"))
    while True:
        if rch<=5:
            break
        else:
            print("Wrong Input!!!Please Try Again\n---------------------------------------------------------------------------------------\n")
            rch=int(input("Enter your choice of restaurant(1/2/3/4/5)"))
            continue
    return location, rch

loc=["Kolkata","Mumbai","Delhi","Chennai","Bangalore","Guwahati"]
kolkata=["Abar Khabo", "Bonnagor", "Theque", "Taste of Hill", "Khatta Meetha"]
mumbai=["Indiana", "Mainland China", "Mumma's Kitchen", "Sizzling Grass", "Fooodie's Area"]
delhi=["So Tasty", "Grassy Fussy", "Delta Suites", "Hotel Anand", "Food Mart"]
chennai=["Hot N Swwet", "Sizzlicious", "Theque", "Taste of Hill", "Parallax Restaurant"]
bangalore=["Sky Dinner", "Chez Panisse Cafe", "Pine & Dine", "The Glass Onion", "Bakers Area"]
guwahati=["Life of Pie", "Meal Cage", "Green Cafe", "Havemore", "Silver Platter"]
allres=[kolkata,mumbai,delhi,chennai,bangalore,guwahati]

menu_dic={1:{'name': "Crispy Chilli Babycorn", 'price': 175, 'type': "starter"},
          2:{'name': "Chilli Chicken", 'price': 150, 'type': "starter"},
          3:{'name': "Dragon Chicken", 'price': 200, 'type': "starter"},
          4:{'name': "Chikka Tikka(8 pcs.)", 'price': 275, 'type': "Main Course"},
          5:{'name': "Chicken Moghlai", 'price': 135, 'type': "Main Course"},
          6:{'name': "Chicken Dopiaza(8 pcs.)", 'price': 250, 'type': "Main Course"},
          7:{'name': "Paneer Makhani", 'price': 150, 'type': "Main Course"},
          8:{'name': "Dal Tadka/Dal Fry", 'price': 100, 'type': "Main Course"},
          9:{'name': "Paneer Lawab Dal", 'price': 120, 'type': "Main Course"},
          10:{'name': "Chicken Manchurian", 'price': 175, 'type': "Main Course"},
          11:{'name': "Veg Manchurian", 'price': 150, 'type': "Main Course"},
          12:{'name': "Paneer Dopiaza", 'price': 170, 'type': "Main Course"},
          13:{'name': "Egg Butter Curry", 'price': 145, 'type': "Main Course"},
          14:{'name': "Butter Nun", 'price': 35, 'type': "Roti"},
          15:{'name': "Tandoori Roti", 'price': 30, 'type': "Roti"},
          16:{'name': "Masala Kulcha", 'price': 45, 'type': "Roti"},
          17:{'name': "Lachcha Paratha", 'price': 45, 'type': "Roti"},
          18:{'name': "Momo(Schezwan/Pan-Fried/Steam)(8 pcs.)", 'price': 120, 'type': "Snacks"},
          19:{'name': "Pastry", 'price': 45, 'type': "Snacks"},
          20:{'name': "French Fries", 'price': 90, 'type': "Snacks"},
          21:{'name': "Masala Vada Paw", 'price': 50, 'type': "Snacks"},
          22:{'name': "Cold Drink(Coke/Pepsi/Mirinda)(250 ml)", 'price': 40, 'type': "Beverages"},
          23:{'name': "Gulab Jamun(4 pcs.)", 'price': 25, 'type': "Beverages"},
          24:{'name': "Ice Cream(Chocolate Cone)", 'price': 30, 'type': "Beverages"}}

deln=["Akash Roy","Vikash Kumar","Dehej Prajapti","Amit Dodeja","Ashish Aurora","Kapil Sharma","Rajesh Aggarawal","Mukesh Kumar","Anil Sarkar"]

def Menu(l,c):
        print(f"\n\n                Welcome to {allres[l-1][c-1]},{loc[l-1]}")
        print("""            <<---------------  Menu  -------------->>""")
        print("\n\nName  --------->   Price")
        print("\nSTARTER LIST\n")
        for i in range(1,25):
            if menu_dic[i]['type'] == "starter":
                print(i, f"{menu_dic[i]['name']}  -------> Rs. {menu_dic[i]['price']}")
            if i==4:
                print("\nMAIN COURSE LIST\n")
            if menu_dic[i]['type']=="Main Course":
                print(i, f"{menu_dic[i]['name']}  -------> Rs. {menu_dic[i]['price']}")
            if i==14:
                print("\nROTI LIST\n")
            if menu_dic[i]['type']=="Roti":
                print(i, f"{menu_dic[i]['name']}  -------> Rs. {menu_dic[i]['price']}")
            if i==18:
                print("\nSNACKS LIST\n")
            if menu_dic[i]['type']=="Snacks":
                print(i, f"{menu_dic[i]['name']}  -------> Rs. {menu_dic[i]['price']}")
            if i==22:
                print("\nBEVERAGES LIST\n")
            if menu_dic[i]['type']=="Beverages":
                print(i, f"{menu_dic[i]['name']}  -------> Rs. {menu_dic[i]['price']}")
            if i==25:
                print("\n\nChoose from the list and Enter the number of the SL. NO. of the item and their quantity\n")


        return True

def userselect(a):
    i = 1
    total=0
    f1 = open("Current Bill.txt", "w")
    f1.write(f"                        Bill of {a.get('name')}\n\n\n")
    f1.write("Food Name                                              Unit price   Quantity   Total\n\n")
    while True:
        s=""
        if i == 1:
            food = int(input("Enter serial Number of food you want to order"))
            while True:
                if food<=24 and food>0:
                    break
                else:
                    print("Wrong Input!!!Please Try Again")
                    food = int(input("Re-Enter serial Number of food you want to order"))
                    continue
            qty = int(input("Enter no. of items of order you placed"))
            total = total + (menu_dic[food]['price'])*qty
            s=s+f"{menu_dic[food]['name']}"
            while len(s)<59:
                s=s+" "
            s=s+f"{menu_dic[food]['price']}"
            while len(s)<66:
                s=s+" "
            s = s + "*"
            while len(s)<71:
                s=s+" "
            s=s+f"{qty}     =  {(menu_dic[food]['price'])*qty}\n"
            f1.write(s)
            ch1 = input("Do you want to order anything else(y/n)")
            if ch1=="y":
                i=1
            elif ch1=="n":
                final=""
                final=final+"GRAND TOTAL"
                while len(final) < 80:
                    final = final + " "
                final= final+f"{total}\n\n"
                f1.write("\n")
                f1.write(final)
                i=2
        elif i==2:
            print("Thank You for placing your order with us.")
            print("Please Bear with us till your order is being processed.\n\n-------------------------------------------------------------------------------------\n\n")
            break
    f1.close()
    return total

def userselect_np(t):
    f1 = open("Current Bill.txt", "a")
    f1.write("((ITEMS ADDED LATER))\n\n")
    total=0
    i=1
    while True:
        s=""
        if i == 1:
            food = int(input("Enter serial Number of food you want to order"))
            qty = int(input("Enter no. of items of order you placed"))
            total = total + (menu_dic[food]['price'])*qty
            s=s+f"{menu_dic[food]['name']}"
            while len(s)<59:
                s=s+" "
            s=s+f"{menu_dic[food]['price']}"
            while len(s)<66:
                s=s+" "
            s = s + "*"
            while len(s)<71:
                s=s+" "
            s=s+f"{qty}     =  {(menu_dic[food]['price'])*qty}\n"
            f1.write(s)
            ch1 = input("Do you want to order anything else(y/n)")
            if ch1=="y":
                i=1
            elif ch1=="n":
                final=""
                final=final+"GRAND TOTAL(Changed/New)"
                while len(final) < 80:
                    final = final + " "
                final= final+f"{total+t}\n\n"
                f1.write("\n")
                f1.write(final)
                i=2
        elif i==2:
            print("Thank You for making changes to your order.")
            print("Please bear with us till your order is being processed.")
            break
    f1.close()
    chg_tot=total+t

    return chg_tot

def sqlentry(a,totamt):
    con=sql.connect(user='Partha',
                    password='partha1234',
                    host='127.0.0.1',
                    database='CustomerInfo')
    cr1=con.cursor()

    sqlTablecreate1 = """create table if not exists Basic_Information(Name char(50), Mobile char(20), Address char(100), Username char(25), Total_Amount float(12,2))"""
    cr1.execute(sqlTablecreate1)
    con.commit()

    sqlTablecreate2 = """create table if not exists Payment_Information(Username char(25), Type char(50), CC_Number char(25), CC_ExpDate char(15), CC_Name char(50), DC_Number char(25), DC_ExpDate char(15), DC_Name char(50), NB_Acc_NumNB_Acc_Num char(30), NB_IFSC_Code char(30), Paytm_Mob_Num char(15))"""
    cr1.execute(sqlTablecreate2)
    con.commit()

    cnm=a.get('name')
    cmob=a.get('mobile')
    cad=a.get('address')
    cun=a.get('username')
    camt=totamt

    sqlInsert1=f"""insert into Basic_Information(Name,Mobile,Address,Username,Total_Amount) values(%s,%s,%s,%s,%s)"""
    cr1.execute(sqlInsert1,(cnm,cmob,cad,cun,camt))
    con.commit()

    ch3 = int(input("Enter your mode of payment(1/2/3/4/5\n1.Credit Card\n2.Debit Card\n3.Net Banking\n4.Cash\n5.Paytm"))
    while True:
        if ch3 == 1:
            ty = "Credit Card"
            cc_num=input("Enter your Credit Card Number")
            cc_ed=input("Enter expiry date(mm/yy)")
            cc_n=input("Enter Name on Credit Card")
            sqlInsert2 = f"""insert into Payment_Information(Username,Type,CC_Number,CC_ExpDate,CC_Name) values(%s,%s,%s,%s,%s)"""
            cr1.execute(sqlInsert2, (cnm, ty, cc_num, cc_ed, cc_n))
            con.commit()
            break
        elif ch3 == 2:
            ty = "Debit Card"
            dc_num=input("Enter your Debit Card Number")
            dc_ed=input("Enter expiry date(mm/yy)")
            dc_n=input("Enter Name on Debit Card")
            sqlInsert3 = f"""insert into Payment_Information(Username,Type,DC_Number,DC_ExpDate,DC_Name) values(%s,%s,%s,%s,%s)"""
            cr1.execute(sqlInsert3, (cnm, ty, dc_num, dc_ed, dc_n))
            con.commit()
            break
        elif ch3 == 3:
            ty = "Net Banking"
            acc_num=input("Enter your Account Number")
            acc_cd=input("Enter IFSC code")
            sqlInsert4 = f"""insert into Payment_Information(Username,Type,NB_Acc_Num,NB_IFSC_Code) values(%s,%s,%s,%s)"""
            cr1.execute(sqlInsert4, (cnm, ty, acc_num, acc_cd))
            con.commit()
            break
        elif ch3 == 4:
            ty = "Cash"
            sqlInsert5 = f"""insert into Payment_Information(Username,Type) values(%s,%s)"""
            cr1.execute(sqlInsert5, (cnm, ty))
            con.commit()
            break
        elif ch3 == 5:
            ty = "Paytm"
            pt_num=input("Enter your Credit Card Number")
            sqlInsert6 = f"""insert into Payment_Information(Username,Type,Paytm_Mob_Num) values(%s,%s)"""
            cr1.execute(sqlInsert6, (cnm, ty, pt_num))
            con.commit()
            break
        else:
            print("Wrong Input!!Try Again")
            continue

    print("Complete the captcha verification to prove that you are not a bot")
    verify()
    print("Payment Done Successfully!!!")
    return True

def deliveryboy():
    ln=len(deln)
    dc=r.randint(0,(ln-1))
    d=deln[dc]
    nm=""
    for i in range(0,10):
        nm=nm+str((r.randint(0,9)))
    print("Your Order will be delivered within 45 mins by Sunshine Delivery Boy")
    print("\n\nDELIVERY BOY DETAILS\n\n")
    print(f"Name --> {d}\nMobile Number --> {nm}")
    return True

def feedback():
    fdbk=float(input("Enter your rating feeding from 0 - 5.0"))
    fdbk_cmmt=input("Enter any feedback comment if you want to")
    return fdbk,fdbk_cmmt

# main
print("1.Sign Up\n2.Login\n----------------------------------------------------------------------------------\n")
mch = int(input("Enter Your Choice-->"))
flag1=False
while True:
    if mch == 1:
        uname = input("Enter a new username")
        f = open("Details.dat", "rb")
        while True:
            try:
                x = p.load(f)
                if x.get('username') == uname:
                    print("This username already exists\n-------------------------------------------------------------------------------------------\n\n")
                    flag1=False
                    mch=1
                    break
                else:
                    continue
            except EOFError:
                flag1=True
                break

        while flag1==True:
            f.close()
            pw = input("Enter your new Password (min. 8 characters and max. 16 characters)")
            while True:
                if (len(pw) >= 8) and (len(pw) <= 16):
                    break
                else:
                    print("Password is not fulfilling criteria")
                    pw = input("Renter Your Password")
            print("Enter Your Details Below")
            name = input("Enter your name")
            mob = input("Enter your mobile number")
            add = input("Enter your FULL Address")
            secq = input("Enter Security Question")
            seca = input("Enter Answer of Security Question (CASE SENSATIVE)")
            verify()
            f5= open("Details.dat", "ab")
            det = {'username': uname, 'password': pw, 'name': name, 'mobile': mob, 'address': add, 'secques': secq,
                   'secans': seca}
            p.dump(det, f5)
            f5.close()
            print("Sign Up Successful!!\nNow login using your username and password.\n--------------------------------------------------------------------------------------\n\n")
            mch = 2
            break

    elif mch == 2:
        uname = input("Enter username")
        f = open("Details.dat", "rb")
        while True:
            try:
                x = p.load(f)
                if x.get('username') == uname:
                    pw = input("Enter your Password")
                    if x.get('password') == pw:
                        print("Login Successful")
                        print(f"\n\nWelcome {x.get('name')}")
                        location, rch = place()
                        Menu(location, rch)
                        tot = userselect(x)
                        while True:
                            p=open("Current Bill.txt","r")
                            bill=p.read()
                            print("\n\n"+bill)
                            print("\n\nYou can check your bill above")
                            p.close()
                            ch2=input("Proceed To payment?(y/n)")
                            if ch2=="y":
                                f2 = open("All Bills.txt", "a")
                                f1 = open("Current Bill.txt", "r")
                                txt = f1.read()
                                f2.write(txt)
                                f2.write("\n\n\n")
                                f2.close()
                                f1.close()
                                sqlentry(x,tot)
                                print("Order has been placed succesfully.")
                                deliveryboy()
                                feedback()
                                break
                            elif ch2=="n":
                                tot_final=userselect_np(tot)
                                tot=tot_final

                        break

                    else:
                        print("Wrong Password")
                        pass_ch = input("Did you forget your password?(y/n)")
                        if pass_ch=="y":
                                print(f"Answer the security question\n{x.get('secques')}")
                                ans=input("Type your answer here(CASE SENSATIVE)")
                                if ans==x.get('secans'):
                                    print(f"Here is your Password-->{x.get('password')}")
                        break
            except EOFError:
                print("Username does not exist")
                break
        f.close()
    else:
        print("Wrong Choice!!!Please Try Again")
        continue















#         else:
#         print("Wrong Password")
#         pass_ch = input("Did you forget your password?(y/n)")
#         if pass_ch == "y":
#             print(f"Answer the security question\n{x.get('secques')}")
#             ans = input("Type your answer here(CASE SENSATIVE)")
#             if ans == x.get('secans'):
#                 print(f"Here is your Password-->{x.get('password')}")
#         break
# except EOFError:
# print("Username does not exist")
# break
# f.close()
# else:
# print("Wrong Choice!!!Please Try Again")
# continue
#         else:
#         print("Wrong Password")
#         pass_ch = input("Did you forget your password?(y/n)")
#         if pass_ch == "y":
#             print(f"Answer the security question\n{x.get('secques')}")
#             ans = input("Type your answer here(CASE SENSATIVE)")
#             if ans == x.get('secans'):
#                 print(f"Here is your Password-->{x.get('password')}")
#         break
# except EOFError:
# print("Username does not exist")
# break
# f.close()
# else:
# print("Wrong Choice!!!Please Try Again")
# continue
#         else:
#         print("Wrong Password")
#         pass_ch = input("Did you forget your password?(y/n)")
#         if pass_ch == "y":
#             print(f"Answer the security question\n{x.get('secques')}")
#             ans = input("Type your answer here(CASE SENSATIVE)")
#             if ans == x.get('secans'):
#                 print(f"Here is your Password-->{x.get('password')}")
#         break
# except EOFError:
# print("Username does not exist")
# break
# f.close()
# else:
# print("Wrong Choice!!!Please Try Again")
# continue
#         else:
#         print("Wrong Password")
#         pass_ch = input("Did you forget your password?(y/n)")
#         if pass_ch == "y":
#             print(f"Answer the security question\n{x.get('secques')}")
#             ans = input("Type your answer here(CASE SENSATIVE)")
#             if ans == x.get('secans'):
#                 print(f"Here is your Password-->{x.get('password')}")
#         break
# except EOFError:
# print("Username does not exist")
# break
# f.close()
# else:
# print("Wrong Choice!!!Please Try Again")
# continue
#

        
        






