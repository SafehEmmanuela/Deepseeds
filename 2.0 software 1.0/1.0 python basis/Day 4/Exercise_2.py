# Write a function that takes in an array in target and
# calculate the average of numbers in the array and also 
# look through the array to check if target is in the array. 
# If yes, return “seen” else “unseen” 
# Your function should return the average and whether the target is seen or not
def average_target (array, target):
    total=0
    length=0
    average=total/len(array)
    found= False

    for number in array:
        total = total +number
        length= length +1
    found== False
    for number in array:
        if number == target:
            found=True
            break
    if found== True:
        print("Seen")
    else:
        print("Unseen")

    average= total/length
    return average 
   
numbers = [2,5,4,6]
target=10
result=average_target(numbers,target)
print(f"Average =  {result}")