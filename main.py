# Day-5: Project: Password-Generator (Easy Version)

### Instructions: ###
# The program will ask:
# How many letters would you like in your password?
# How many symbols would you like?
# How many numbers would you like?

# The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

### Easy Version: ###
# Generate the password in sequence. If the user wants:
    # 4 letters
    # 2 symbols and
    # 3 numbers

# then the password might look like this: fgdx$*924

#Password Generator Project (Easy Version)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

# For random characters
for char in range(1, nr_letters+1):
  random_char = random.choice(letters)
  password += random_char

# For random symbols
for symbol in range(1, nr_symbols+1):
  random_symbol = random.choice(symbols)
  password += random_symbol

# For random numbers
for number in range(1, nr_numbers+1):
  random_number = random.choice(numbers)
  password += random_number

print(f"Your password is: \n{password}")