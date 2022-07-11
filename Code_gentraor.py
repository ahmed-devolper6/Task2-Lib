'''''
create 2 functions 
the frist one take text
encoded he text messg
the secned on decode
the organal message
'''
from dataclasses import replace
import string
def encoded():
    global my_name
    my_name = input("Type ur name:")
    return my_name

def decoded():
    global new_name
    new_name = input(f" {my_name} :Enter i new name:")
    return my_name.replace(my_name,new_name)
name = input("Enter ur name:")
start = encoded()
if my_name == name:
    df = decoded()
    print(f"ur name {name} is repalce by {df}ahm")