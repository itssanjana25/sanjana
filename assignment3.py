

# 1. Largest of two numbers

num1=int(input(" Enter number1 :"))
num2=int(input(" Enter number2 :"))

if num1 > num2 :
    print("The", num1,  "is Greater.")
    
elif num1 < num2 :
    print("The", num2, "is Greater.")

else :
    print("Both numbers are equal")

print()


#2. Largest of three numbers
    
num1=int(input(" Enter number1 :"))
num2=int(input(" Enter number2 :"))
num3=int(input(" Enter number3 :"))

if (num1 >= num2) and (num1 >= num3):
    print(num1,"is largest")
    
elif (num2 >= num1) and (num2 >= num3):
    print(num2,"is largest")
    
else:
    print(num3,"is largest")

print()


# 3. profit or loss

costp = int(input("Enter the Cost Price: "))
sellp = int(input("Enter the Selling Price: "))

if sellp > costp:                                
    profit = sellp - costp
    print(" Your profit is :",profit,"%")

elif costp > sellp:
    loss = costp - sellp
    print(" Your loss is :", loss,"%")

else:
    print("No Profit, No Loss.")

print()


# 4. number in range

num = int(input("Enter a number: "))

if 10 <= num <= 50:
    print("Yes,", num,"lies between 10 and 50.")
    
else:
    print(f"No,", num , "is outside the range.")
print()


# 5. leap year

year = int(input("Enter a year: "))
if year % 4 == 0 :
    print(year, "is a leap year")
else:
    print(year, "is not a leap year.")
print()


# 6. three digit number

num = int(input("Enter a number: "))
if 100 <= num <= 999:
    print(num, "is a three-digit number.")
else:
    print(num, "is not a three-digit number.")
print()


# 7. divisible by both 3 and 5

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(num, "is divisible by both 3 and 5.")
    
else:
    print(num, "is not divisible by both 3 and 5.")
print()

a=int(input("Enter angle1 :"))
b=int(input("Enter angle2 :"))
c=int(input("Enter angle3 :"))

if a + b + c == 180 :
    print("Valid triangle ")
else:
    print("Not valid")

