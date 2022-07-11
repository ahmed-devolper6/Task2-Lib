from ntpath import join
import random
import string
letters = string.ascii_letters
while True:
    length = int(input("Type i length for password: "))
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    if length >= 7:
        print(f"Random string of length length, is: {result_str}")
    else:
        print("the password is weak")