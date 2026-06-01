# 1.Take a number n (user input) and print numbers from 1 to n.

num = int(input("Enter a number: "))
for i in range(1, num + 1):
    print(i)
print()


# 2. Print numbers from 1 to 50 that are divisible by 3

for i in range(1, 51):
    if i % 3 == 0:
        print(i)
print()


# 3. Print all numbers between 1 and 100 that are divisible by both 3 and 5

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
print()


# 4.Print numbers from 1 to 20, but Skip multiples of 4

for i in range(1, 20):
    if i % 4 == 0:
        continue
    print(i)
print()


# 5.Ask the user to input numbers 5 times.Stop early if the user enters a zero (break).

for i in range(1,6) :
    num = int(input("Enter number :"))
    if num == 0:
        break
    print(i)
print()


# 6.Print characters of a string, but stop when you find the first vowel (break).

for i in "Hello!" :
    vowels = "aeiou"
    if i in vowels:
        break
    print(i)
print()


# 7.Print all characters except spaces (continue).

char = input("Enter a string: ")
for i in char:
    if i == " ":
        continue  
    print(i)


    
