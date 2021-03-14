#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(',')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_len = nr_letters + nr_symbols + nr_numbers
password = []

for i in range(0, nr_letters):
  random_letters = random.randint(0,len(letters) - 1)
  password.append(letters[random_letters])
for x in range(0, nr_symbols):
  random_symbols = random.randint(0,len(symbols) - 1 )
  password.append(symbols[random_symbols])
for z in range (0, nr_numbers):
  random_numbers = random.randint(0,len(numbers) - 1)
  password.append(numbers[random_numbers])

final_password = ""
for x in range(len(password)): 
    final_password += password[x]

print(f"Easy Level: \nYour Password len is: {total_len}\nAnd your Safe Password is: {final_password}\n")

hard_password = random.sample(password, len(password))

final_hard_password = ""
for x in range(len(hard_password)): 
    final_hard_password += hard_password[x]

print(f"Hard Level: \nYour Password len is: {total_len}\nAnd your Safe Password is: {final_hard_password}\n")

