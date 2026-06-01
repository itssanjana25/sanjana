
## 1.Student Marks Management
##
##  Write a Python program to:
##    1) Create a list of marks for 5 students.
##    2) Display all marks.
##    3) Find the highest and lowest marks.
##    4) Calculate the average marks.


stud_marks = [85,92,80,60,83]

print("All student marks:", stud_marks)

highest_mark = max(stud_marks)
lowest_mark = min(stud_marks)
 
total_marks = sum(stud_marks)
no_of_stud = len(stud_marks)
average_mark = total_marks / no_of_stud

print("Highest Mark:", highest_mark)
print("Lowest Mark: " ,lowest_mark)
print("Average Mark:", average_mark)  

print()


## 2.Tuple Slicing Operations
##
##   Given: numbers = (10, 20, 30, 40, 50, 60, 70)
##   Write Python statements to:
##     1) Display first 3 elements.
##     2) Display last 2 elements.
##     3) Display elements from index 2 to 5.
##     4) Reverse the tuple using slicing.


numbers = (10, 20, 30, 40, 50, 60, 70)

print("Display Tuple:", numbers)

first_three = numbers[:3]
print("First 3 elements: ",first_three)

last_two = numbers[-2:]
print( "Last 2 elements: ",last_two)

index = numbers[2:6]
print("Elements from index 2-5:",index)

reversed_tuple = numbers[-1::-1]
print("Reversed tuple:",reversed_tuple)

print()


## 3.Create a set of even numbers from 1 to 20.

s = set(range(2, 21, 2))
print(s)
 
print() 


## 4.Find common elements between two lists using sets.

L1 = [10,20,30,40,50]
L2 = [20,30,60,70,90]

S1 = set(L1)
S2 = set(L2)

S3 = S1.intersection(S2)
print(S3)

print()


## 5.Student Enrollment Analysis

##     A school maintains two sets:
##       science = {"Amit", "Rahul", "Sneha", "Priya", "John"}
##       maths = {"Rahul", "John", "Kiran", "Priya", "Neha"}
##
##        Write a Python program to:
##         1) Find students enrolled in both subjects.
##	   2) Find students enrolled only in Science.
##	   3) Find students enrolled only in Maths.
##	   4) Find all students enrolled in at least one subject.
##	   5) Find students enrolled in exactly one subject.


science = {"Amit", "Rahul", "Sneha", "Priya", "John"}
maths = {"Rahul", "John", "Kiran", "Priya", "Neha"}

print("Science Students:",science)
print("Maths Students:",maths)

both_subjects = science.intersection(maths)
print("Enrolled in both subjects:",both_subjects)

only_science = science.difference(maths)
print(" Enrolled only in Science: ",only_science)

only_maths = maths.difference(science)
print(" Enrolled only in Maths: ",only_maths)

all_students = science.union(maths)
print(" Enrolled in at least one: ",all_students)

exactly_one = science.symmetric_difference(maths)
print(" Enrolled in exactly one subject:",exactly_one)

print()


## 6.Sports Club Membership
##      Two sports clubs maintain the following records:
##      cricket = {"Sam", "David", "Ali", "Rohan", "Karan"}
##      football = {"Ali", "Rohan", "John", "Mark"}
##
##       Perform the following operations:
##           1) Display members who play both games.
##	   2) Display members who play only cricket.
##	   3) Display members who play only football.
##	   4) Check whether all football players are cricket players. ( Hint : using issubset / issuperset )


cricket = {"Sam", "David", "Ali", "Rohan", "Karan"}
football = {"Ali", "Rohan", "John", "Mark"}

print("Cricket Club Members:",cricket)
print("Football Club Members:",football)

both_games = cricket.intersection(football)
print("Plays both games:",both_games)

only_cricket = cricket.difference(football)
print("Plays only cricket:",only_cricket)

only_football = football.difference(cricket)
print("Plays only football:",only_football)

all = cricket.issuperset(football)
print("All :",all)






