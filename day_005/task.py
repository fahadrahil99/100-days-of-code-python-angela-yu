letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
e = nr_letters+nr_symbols+nr_numbers
import random

b = random.choice(letters)
for a in range(1,nr_letters) :
    b += random.choice(letters)
for a in range(1,nr_numbers+1) :
    b += random.choice(numbers)
for a in range(1,nr_symbols+1)  :
    b += random.choice(symbols)
c = list(b)
random.shuffle(c)

d = str(c.pop(1))
for a in c :
    d += a
print("You\'re Password is : ",d)






