from datetime import date
print('''
i well take form you i two dayes
and i well count the dayes betwen us
''')
while True:
    palyer = input("if u want paly type x if u want exit type n:  ")
    if palyer == 'n':
        break
    if palyer == 'x':
        year0 = int(input("type the year of date one: "))
        mounth0 = int(input("type the mounth of date one: "))
        day0 = int(input("type the day of date one: "))
        date0 = date(year0,mounth0,day0)
        year1 = int(input("type the year of date two : "))
        mounth1 = int(input("type the mounth of date two: "))
        day1 = int(input("type the day of date two: "))
        date1 = date(year1,mounth1,day1)
        counter = (date0 - date1) 
        print(f"the count is {counter}")
    else:
        print("enter x or y...")