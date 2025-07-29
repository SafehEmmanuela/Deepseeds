# # FizzBuzz game
# # Fizz if number is divisible by 3
# # FizzBuzz if number is divisible by both 3 and 5
# # Buzz if number is divisible by 5

# while True:
#     user_input= input("\n continue or 'exit': ")
    
#     number = int(input("Enter the number:"))
# if number % 3==0 and number % 5==0:
#     print("FessBuzz")
#     count+= +1
# elif number %3 == 0:
#     print("Fess")
# else:
#     number %5 == 0
#     print("Buzz")



# # A code to swap 2 contents a and b
# a=int(input("Enter your first value: "))
# b=int(input("ENter your second value:"))
# c=a
# a=b
# b=c
# print(f"Value of a={a} and value of b={b}")

# computer will generate a random number between 1 and 20
# Guess the answer
# if answer is below the target, print(Answer is below the target)
# elif answee less than target, print(Answer is higher than target)

correct_number= 20
for attempt in range(3):
    guess = int(input("Guess the number: "))

    if guess < correct_number:
        print("Answer lower than the correct answer ")
    elif guess > correct_number:
        print("Answer is greater than the correct answer")
    else:
        print(f"{guess} is the correct asnwer")
        break
else:
    print("Sorry you've used all your chances")
    