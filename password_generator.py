import random
import string

print("Welcome to the Password Generator!")

length = int(input("Enter the total number of characters in the password :"))

num_letters = int(input("Enter the number of letters in the password :"))
num_number = int(input("Enter the number of numbers in the password :"))
num_symbols = int(input("Enter the number of symbols in the password :"))

if length != ( num_letters + num_number + num_symbols ) :
    print("Invalid input.\nThe sum of letters, numbers, and symbols doesn't match the password.")

else :
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    password_chars = ( 
         random.choices(letters, k=num_letters) +
         random.choices(numbers, k=num_number) +
         random.choices(symbols, k=num_symbols)
         )
    random.shuffle(password_chars)
    password = ''.join(password_chars)
    print("Generated Password :", password)
