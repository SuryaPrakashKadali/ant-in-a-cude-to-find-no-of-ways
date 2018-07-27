#no of way a ant can go from one conner to  other in a cube of(l=b=h=n) of n
from math import factorial
n = int(input())
m = int(factorial(3*n)/(n**3))
print("no of ways is :",m)
