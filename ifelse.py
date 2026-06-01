
'''  ***  Conditional Satement  ***  '''

#if else statement
# syntax :
##       if condition :
##           // code
##       elif condition:
##           // code



    
# 1. check whether the candidate is eligible for vote

age = int(input("Enter your age :"))
if age>= 18:
    print("Eligible for vote")

elif age< 18:
    print("Not eligible to vote")
print()

 
# 2. Grading according to given marks 

marks=int(input("Enter your marks :"))

if marks >= 85 :
    print("Grade - A")

elif marks >= 75 :
    print("Grade - B")

elif marks >= 40 :
    print("Grade - C")

elif marks < 40:
    print("Grade - F")
print()


# 3. Quadtrants 


x=int(input("Enter x :"))
y=int(input("Enter y :"))

if x > 0 and y > 0 :
      print("I-Quadrant.")

elif x < 0 and y > 0 :
      print("II-Quadrant.")

elif x < 0 and y < 0 :
      print("III-Quadrant.")

elif x > 0 and y < 0 :
      print("IV-Quadrant.")

elif x == 0 :
    print("X-axis.")

else :
    print("Y-axis.")
