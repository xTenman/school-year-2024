#program: lesson 3 week 3
#programmer: ethian
#date: 1/24/2024
#purpose: demonstrate Python’s ability to use dynamic data entry.
#
#define variables
in1=str("")
in2=str("")
in3=str("")
iq1=int(0)
iq2=int(0)
iq3=int(0)
ip1=float(0.0)
ip2=float(0.0)
ip3=float(0.0)

it1=float(0.0)
it2=float(0.0)
it3=float(0.0)
order_total = float(0.0)

#input
name=input("what's your name sir/madam?: ")
print("Welcome to XYZ general store {:>}\nPlease scan (name) your item now:".format(name))
in1=input()
iq1=int(input("How many {} are you buying?: ".format(in1)))
ip1=float(input("How much does {} cost?: ".format(in1)))
print("Please scan (name) your second item now: ")
in2=input()
iq2=int(input("How many {} are you buying?: ".format(in2)))
ip2=float(input("How much does {} cost?: ".format(in2)))
print("Please scan (name) your third item: ")
in3=input()
iq3=int(input("How many {} are you buying?: ".format(in3)))
ip3=float(input("How much does {} cost?: ".format(in3)))

#process
it1=iq1*ip1
it2=iq2*ip2
it3=iq3*ip3
order_total=it1+it2+it3

#output
print("\nReciept for: {:>}".format(name))
print()
print("item# name price amount total")
print("1.- {}           ${:<}   {:>}          ${:>}".format(in1,ip1,iq1,it1))
print("2.- {}           ${:<}   {:>}          ${:>}".format(in2,ip2,iq2,it2))
print("3.- {}           ${:<}   {:>}          ${:>}".format(in3,ip3,iq3,it3))
print("your overall total is: ${:d>}".format(order_total))
