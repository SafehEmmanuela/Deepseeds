# # if age is more than 18 - can vote
# # Else, can't vote
# age=input("Please enter your age")
# if age >18:
#     print("Welcome, You can vote")
# else:
#     print("Please wait for next election")

# Exercie: take a person's age, check if they are more than 16, if yes, they can play in the basketball team

# age=int(input("Please enter your age"))
# if age >16:
#     print("You can play in the basketball team")
# else:
#     print("Sorry youcannot  play in the basketball team")


# command= input("Enter 'exit' to the program and 'continue' to keep it going" )
# if command=="exit":
#     print("Exiting command")
# elif command=="continue":
#     print("continue enjoying...")
# else:
#     print("Wrong command")

# #if_else_elif chain
# # exercise
# print("___"*50)
# marks= float(input("Input your grade here:"))
# if marks>= 80:
#     print("You have a A❤️ Grade")
# elif marks>=70:
#     print("You have a B+🦸‍♂️ grade")
# elif marks>=60:
#     print("You have a C😂 grade")
# else:
#     marks=50
#     print(" You have a D😒 grade")


# # simple calculator
# first_number= float(input("Enter first number: "))
# second_number=float(input("Enter second number: "))
# operator= input("Enter operator")
# result=0

# if operator=="+":
#     result=first_number+second_number
# elif operator=="-":
#     result=first_number-second_number
# elif operator=="*":
#     result=first_number*second_number
# elif operator=="/":
#     if second_number!= 0:
#         result=first_number/second_number
#         print(result)
#     else:
#         print("Cannot be divided by zero")
# else:
#     print("Error") 


# Leap year excercise
# to check if a year is a leap year or not

year=int(input("Enter the year here:"))
if year %4!=0:
    if year%100!=0:
        if year%400!=0:
            print(f"It is not a leap  year")
else:
    print(f"It is a leap year")    