# for loop
# 1. Starting point
# 2. Condition
# 3. increment or decrement

# names=["Emma", "Leo","Kate", "Kelly", "SafehMbom", "PeggyMbom", "TracyMbom"]
# # database of people
# print(names[0])
# print(names[1])
# print(names[2])
# # or
# for name in names:
#     print(name)
#     if name.endswith("Mbom"):
#         print(f"We dan catch you: {name}")
#     else:
#         print(f"Welcome to the party: {name}")

# count =1
# for name in names:
#     print(f"{count} {name}")
#     count +=1



# # RANGE METHOD in looping
# for i in range(5):
#     print(i)
# for i in range(2,7):
#     print(i)



# # printing even numbers
# for i in range(0, 10, 2):
#     print(i)  


# # countdown
# for i in range(10, 0, -1):
#     print(f"Countdown: {i}")


# # Baisc while loop
# count=1
# while count <=5:
#     print(f"Count is: {count}")
#     count+=1

# # user input loop
# user_input= ""
# while user_input!= "quit":
#     user_input = input("Enter 'quit' to exit: ")
#     if user_input != "quit":
#         print(f"You entered: {user_input}")
# print("Goodbye!")


# # Break - exit the loop completely
# print("Finding the first even number")
# for number in range (1,10):
#     if number %2==0:
#         print(f"Found even number: {number}")
#         break
#     print(f"{number} is odd")


# print("Printing only odd numbers: ")
# for number in range(1,10):
#     if number %2 == 0:
#         continue 
#     print(f"Odd number: {number}")


# Multiplication table
for i in range(1,4):
    for j in range(1,4):
        result= i*j
        print(f"{i} * {j} = {result}")
