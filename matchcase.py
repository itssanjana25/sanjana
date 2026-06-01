 # 1. *** Even or Odd ***

a = int(input(" Enter a Number :"))
if a % 2 == 0 :
    print("The number is EVEN")
else :
    print("The number is ODD")
print()


# 2. *** Menu ***

num = int(input("Enetr 1. Add ,2. Sub , 3.Multiply, 4.Div :\n"))

match num :
    case 1:
        a=int(input("Enter number1 :"))
        b=int(input("Enter number2 :"))
        print("Addition is :", a+b)

    case 2:
        a=int(input("Enter number1 :"))
        b=int(input("Enter number2 :"))
        print("Subtraction is :", a-b)

    case 3:
        a=int(input("Enter number1 :"))
        b=int(input("Enter number2 :"))
        print("Multiplication is :", a*b)

    case 4:
        a=int(input("Enter number1 :"))
        b=int(input("Enter number2 :"))
        print("Division is :", a/b)

    case _:
        
        print("Invalid input")
print()


# 3. ***  Day of week ***

day = int(input("Enter 1.Monday, 2.Tuesday, 3.Wednesday, 4.Thursday, 5.Friday, 6.Saturday, 7.Sunday :\n"))
match day:
    case 1:
        print(" Monday.")
        
    case 2:
        print(" Tuesday.")
        
    case 3:
        print(" Wednesday.")
        
    case 4:
        print(" Thursday.")
        
    case 5:
        print(" Friday.")

    case 6:
        print(" Saturday.")

    case 7:
        print(" Sunday.")

    case _:
        print(" Invalid input.")
print()


# 4. *** chatbot ***

chat = int(input("Enetr 1.hi, 2.bye, 3.thanks :\n"))

match chat:
    case 1:
        print("Hello! How are you?\n How can I help you?")

    case 2:
        print("Goodbye! Have a great day!\n Take care.")

    case 3:
        print("You are Welcome!\n My pleasure!")

    case _:
        print("Invalid input")

    





