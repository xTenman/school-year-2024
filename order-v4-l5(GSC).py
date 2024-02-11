#program: lesson 5 week 5 GSC
#programmer: ethian
#date: 2/11/2024
#purpose: demonstrate programming logic and basic data validation using conditional coding
#
#variables
ctype=""
amt=0
yn=""

inum=0
it=0.0
ot=0.0

sc=0
tmc=0
tc=0
st=0.0
tmt=0.0
tt=0.0
#input/startup
name=input("What's your name sir/madam?: ")
print("Welcome to this output station of the Girl Scout Cookies enterprise holdings")
while True:
    yn=input("would you like to place an order (Y/N): ").lower()
    if yn!="y" and yn!="n":
        print("Error, invalid input")
    else:
        break
while yn=="y":
    #said yes so pick a cookie
    while True:
        ctype=input("Please choose a flavor:\n1.-Savannah ($3.50)\n2.-Thin Mints ($3.50)\n3.-Tagalogs ($5)\n>")
        match ctype:
            case "1":
                while True:
                    amt=int(input("How many would you like? (1-10): "))
                    if 0<amt<=10:
                        it=amt*3.50
                        sc=sc+amt
                        st=st+it
                        ot = ot+it
                        inum=inum+1
                        
                        print("current running total: ${}".format(ot))
                        print("Item  Flavor    Price Qty Total")
                        print("{}    Savannah $3.50 {}  ${}".format(inum,amt,it))
                        break
                    else:
                        print("error, invalid amount")
                #break out of the switch
                break
            case "2":
                amt=int(input("How many would you like? (1-10): "))
                if 0<amt<=10:
                    tmc=tmc+amt
                    it=amt*3.50
                    tmt=tmt+it
                    ot=ot+it
                    inum=inum+1
                    print("current running total: ${}".format(ot))
                    print("Item  Flavor    Price Qty Total")
                    print("{}    Thin Mint   $3.50 {}  ${}".format(inum,amt,it))
                    break
                else:
                    print("error, invalid amount")
                tm=tm+amt
                #break out of the switch
                break
            case "3":
                while True:
                    amt=int(input("How many would you like? (1-10): "))
                    if 0<amt<=10:
                        tc=tc+amt
                        it=amt*5
                        tt=tt+it
                        ot=ot+it
                        inum=inum+1
                        print("current running total: ${}".format(ot))
                        print("Item  Flavor    Price Qty Total")
                        print("{}    Tagalog    $5 {}  ${}".format(inum,amt,it))
                        break
                    else:
                        print("error, invalid amount")
                #break out of the switch
                break
            case _:
                #no break so while True still in effect
                print("Error, invalid input, choose 1-3")
    #still in the yn while
    while True:
        yn=input("Would you like to make another purchase? (Y/N): ").lower()
        if yn!="y" and yn!="n":
            print("Error, invalid input")
        else:
            break
#outside
if inum==0:
    print("{} has made no purchase".format(name))
else:
    print("Final receipt for {} which consisted of {} transactions consisted of:".format(name,inum))
    print("{} Savannah cookie(s) for: ${}".format(sc,st))
    print("{} Thin Mint cookie(s) for: ${}".format(tmc,tmt))
    print("{} Tagalog cookie(s) for: ${}".format(tc,tt))
    print("Overall total: ${}".format(ot))
