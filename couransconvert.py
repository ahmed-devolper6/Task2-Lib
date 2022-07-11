from currency_converter import CurrencyConverter
money = int(input("hoe mouch money?: "))
curren = input("the currency: ")
convert = input("the currency you want to convert: ")

c = CurrencyConverter(money,curren,convert)
print(c)