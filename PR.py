#  Interactive personal Data Collector
print("Welcome to the Interactive Personal Data Collector!\n")
    # collect user inputs 
name = input("Please enter your name: ")
age =int(input("Please enter you age:"))
height =float(input("Please enter your height"))
favourite_number = int(input("Please enter your favourite numbe:"))

print("Thank you! Here is the infomation we collected:\n")
    #Display collected data with type and memory address 
print(f"Name: {name} (Type: {type(name)},")
print(f"Memory Address: {id(name)}\n")

print(f"Age: {age} (Type: {type(age)},")
print(f"Memory Address: {id(age)})")

print(f"Height: {height} (Type: {type(height)},")
print(f"Memory Address: {id(height)})")

print(f"Favourite Number: {favourite_number} (Type:{type(favourite_number)},")
print(f"Memory Address: {id(favourite_number)})")

# calculate approximate bith year
current_year = 2026
birth_year = current_year - age

print(f"\nYour birth year is approximately:")
print(f"{birth_year} (based on my age of {age})")

print("\nThank you for using the Personal Data Collector.Goodbye!")