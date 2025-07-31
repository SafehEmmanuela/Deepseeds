# def style():
#     print("_"*40)

# def number_error():
#     try:
#         style()
#         user_input=int(input("Please enter your number: "))
#         print(f"User input is: {user_input}")
#     except ValueError:
#         print("Error: Please make sure your number is in digits")

# def division_error():
#     try:
#         style()
#         first_number= int(input("Enter your first number: "))
#         second_number= int(input("Enter your second number: "))
#         print(first_number/second_number)
#     except ZeroDivisionError:
#         print("Enter a number that is different from Zero")

# number_error()
# division_error()


def dictionary_error(data):
    try:
        color=data["color"]
        print(color)
        return(data)

    except KeyError:
        print("What you're looking for is not available")
data={
        "name": "Safeh Emmanuela",
        "age": 19,
        "favourite meal": "Coki"
    }

dictionary_error(data)
