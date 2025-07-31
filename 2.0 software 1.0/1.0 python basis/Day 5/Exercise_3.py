# CREATE A PYTHON RECORD BOOK
# Prompt: please let us know what you've learned today ?
# Enter your answer
# answer wil be stored in a file called: Record in a file caled: REcord.txt created by you

# format to store Data
# record book
# today;s date: Printed here


from datetime import datetime
datetime.now().strftime("%Y - %m - %d ")
# current_time=datetime.now().strftime("%Y - %m - %d %H:%M)
filename= "Record.txt"

print("Welcome to the Record book ")
print("Type 'exit' when you're done recording")

while True:
    response= input("Please let us know what you've learned today: /n> ")

    if response.lower()== "exit":
        print("Recording complete.")
        break
    
    current_time=datetime.now().strftime("%Y - %m - %d %H:%M")

    # with open("Record.txt", "txt","w") as file:
    with open(filename, "a") as file:
        file.write("\nWelcome to the Record book\n")
        file.write(f"Today's date: {current_time}\n")
        file.write(f"What you've learned today: {response}\n")
    print("Your answer has been record")