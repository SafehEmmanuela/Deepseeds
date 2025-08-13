# # To calculate the bmi of a person
# def bmi_calculator(height=67,weight=80):
#     # weight= float(input("Enter the weight of th person: "))
#     # height= float(input("Enter the height of the person: "))
#     bmi_of_the_person= weight / height
#     print(f"The bmi is: {bmi_of_the_person}")

#     if bmi_of_the_person < 18:
#         print(f"Low weight")
#     elif bmi_of_the_person is range(8,25):
#         print(f"Normal weigth")
#     elif bmi_of_the_person is range(25,30):
#         print(f"Over weigth")
#     else:
#         bmi_of_the_person > 30
#         print(f"You're in danger")
# weight= float(input("Enter the weight of th person: "))
# height= float(input("Enter the height of the person: "))
# bmi_calculator(height, weight)


# # Why use functions

# def cal_circle_area(radius):
#     pi= 3.14
#     area = pi * radius* radius
#     return area

# area1= cal_circle_area(5)
# area2= cal_circle_area(10)
# area3= cal_circle_area(7)

# print(f"area of circle 1: {area1}")
# print(f"area of circle 2: {area2}")
# print(f"area of circle 3: {area3}")



# # functions with output
# def bmi(weight=234,height=34):
#     bmi=weight/height
#     return bmi

#     print(bmi)
# # bmi() anything yu put after the return function is not going to wrok



# Exercises 1 on function
def create_profile(name="Safeh Emmanuela", age=19, occupation="Generative AI student",city="Bamenda"):
    print(f"{name} is a {age}-years old girl, a {occupation}, in the city of {city}" )
    return create_profile
create_profile()

# Exercise 2(Grade calculator function)
def calculate_grade(score):
    if score >=90:
        print("A grade")
    elif score > 80:
        print("B grade")
    else:
        score >70
    return score
# calculate_grade()

# # Exercise 3(Shopping card total funtion)
# def calculate_total(price=29.99, quantity=3, tax_rate=0.08):
#     subtotal= price * quantity
#     tax_amount= subtotal * tax_rate
#     final_total=subtotal-tax_amount
#     print(f"Total Cost: {final_total}")
#     return final_total

# calculate_total()
