#Functions

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter the rate:")
r = float(rate)

def computepay(h,r):
 if h<40:
    pay = h*r
 elif h>40:
    pay = 40*r + (h-40)*1.5*r
 return pay


p= computepay(h,r)
print("Pay" , p)