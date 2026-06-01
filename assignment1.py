# 1. Take a number as input and print its suare

num=int(input("Enter the number :"))
print("The square is :", num*num) #OR
print("The square is :", num**2)
print()


# 2. take two numbers and print their product

num1=int(input("enter the value1 :"))
num2=int(input("enter the value2 :"))
print("The product is :", num1*num2)
print()


# 3. Take a number and print its cube

num=int(input("Enter the number :"))
print("The cube is :", num**3)
print()


# 4. Input length and breadth, print perimeter of rectangle

length=float(input("Enter the value of length :"))
breadth=float(input("Enter the value of breadth :"))
perimeter = 2 * (length+breadth)
print("Perimeter of Rectangle is :", perimeter)
print()


# 5. Take a number and print half of it

num = int(input("Enter a number: "))
result = num / 2
print("Half of num is :", result)
print()


# 6. Input three numbers and print their average

a=int(input("enter the value1 :"))
b=int(input("enter the value2 :"))
c=int(input("enter the value3 :"))
avg = (a + b + c) / 3
print("The average is :", avg)
print()


# 7. Take total marks of 5 subjects and print the percentage

s1=int(input("enter marks of Marathi :"))
s2=int(input("enter marks of English :"))
s3=int(input("enter marks of Hindi :"))
s4=int(input("enter marks of History :"))
s5=int(input("enter marks of Science :"))
total = s1 + s2 + s3 + s4 + s5
percentage = (total/500) * 100
print( "Total marks :", total)
print( "Percentage is :", percentage, "%")
print()


# 8. Input a number and print its remainder when divided by 10

num = int(input("Enter a number: "))
remainder = num % 10
print("Remainder when divided by 10 :", remainder)
print()


# 9. Convert temperature from celcius to fahrenheit

celsius = int(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print("Temperature in farenheit :", fahrenheit)
print()


# 10. Input seconds and convert into minutes

total_sec = int(input("Enter the number of seconds: "))
min = total_sec // 60
rem_sec = total_sec % 60
print(total_sec, "seconds is :", min , "minit and", rem_sec, "seconds")
print()


# 11. Input price and quantity , print total cost

price = int(input("Enter the price of item: "))
quantity = int(input("Enter the quantity purchased: "))
total_cost = price * quantity
print("Price is :", price)
print("Quantity is :", quantity)
print("Total Cost is :", total_cost)
print()


# 12. Input base and height , print area of triangle

base = float(input("Enter the base of triangle: "))
height = float(input("Enter the height of triangle: "))
area = (base * height) / 2
print("The Area of Triangle is :", area)
print()


# 13. Input a number and print last digit

num = int(input("Enter a number: "))
last_digit = num % 10
print(f"The last digit is:" , last_digit)







