class Car:
    def __init__(self, brand, color):
        self.brand=brand
        self.color=color

    def drive(self):
        return f"I am driving a car from {self.brand} and the color is {self.color}"
    def calculate_speed(self):
        pass

# created an object of the class car
car1= Car("Toyota", "red")
car2= Car("Benz", "Black")
car3= Car("Tesla", "white")

print(car1.brand)
print(car1.color)
# how to acces the methods
print(car1.drive())
# drive is the name of the method