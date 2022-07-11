covert = input('u want to covert i Temperature type (t) or mesa (m): ')
if covert == 't':
    celsius_1 = float(input("Temperature value in degree Celsius: " ))  
    Fahrenheit_1 = (celsius_1 * 1.8) + 32  

    print(f'The {celsius_1} degree Celsius is equal to: {Fahrenheit_1} Fahrenheit')  
    celsius_2 = float (input("Temperature value in degree Celsius: " ))  
    Fahrenheit_2 = (celsius_2 * 9/5) + 32   
    print (f'The {celsius_2} degree Celsius is equal to: {Fahrenheit_2} Fahrenheit')  
if covert == 'm':
    numbers = float(input("type the number: "))
    inc = numbers/2.54
    cent = inc*2.54
    print("cent is {cent}, inch is {inc}....")