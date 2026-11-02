#PASSWORD GENERATOR
import random
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!','#','$','%','&','(',')','*','+']
print("Welcome to the PyPassword Generator!")
nr_letters=int(input("how many letters  would you like in your password\n"))
nr_symbols=int(input("how many symbols would you like in your password\n"))
nr_numbers=int(input("how many numbers do you want in your password\n"))
password_list=[]
d_letter=[]
for letter in range(1,nr_letters+1):
    d_letter.append(random.choice(letters))
print(d_letter)
d_symbol=[]
for symbol in range (1,nr_letters+1):
    d_symbol.append(random.choice(symbols))
print(d_symbol)
d_number=[]
for number in range (1,nr_numbers+1):
    d_number.append(random.choice(numbers))
print(d_number)
password_list=d_letter+d_symbol+d_number
print(password_list)
random.shuffle(password_list)
password=''.join(password_list)
print(password)

