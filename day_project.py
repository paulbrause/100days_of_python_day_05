import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = ""
pw_list = []

for num in range(1, num_letters + 1):
    pw_list.append(random.choice(letters))
    
for num in range(1, num_symbols + 1):
    pw_list.append(random.choice(symbols))
    
for num in range(1, num_numbers + 1):
    pw_list.append(random.choice(numbers))
    
    
random.shuffle(pw_list)
password += ''.join(pw_list)

print(f"Here is your password: {password}")