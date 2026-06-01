

## 1. WAP that takes  a students marks (0-100) and
##       prints the grade based on:
##       90-100   -  A
##       75-89    -  B
##       50-74    -  C
##       35-49    -  D
##       below 35 -  Fail

# Solution:
    
marks = int(input("Enter your marks :"))

if marks >= 90 :
    print("Your Grade is : A")

elif marks >= 75 :
    print("Your Grade is : B")

elif marks >= 50 :
    print("Your Grade is : C")

elif marks >= 35:
    print(" Your Grade is : D")

else :
    print("You are Fail")



## 2. Categorize temperature
##   < 10 - cod
##   10-25 - normal
##   25 - hot

# Solution:

temp = int(input(" Enter the temperature :"))
if temp < 10 :
    print(" The Temperature is Cold")

elif temp <= 25 :
    print(" The Temperature is Normal")

else :
    print(" The Temperature is Hot")



