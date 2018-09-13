'''Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button) '''
import datetime
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
nowtime = str(datetime.datetime.now())
turn100 = int(nowtime[0:4]) + (100 - age)
if age < 100:
    print("Hello", name, "\nYou are", age , "years old.\nYou will turn 100 years old in {}.".format(turn100))
else:
    print("Hello", name, "\nYou are", age, "years old.\nYou turned 100 years old in {}.".format(turn100))
repeat = int(input("how many time do you want to see this message: "))
while repeat != 0:
    print("Hello", name, "\nYou are", age, "years old.\nYou will turn 100 years old in {}.\n".format(turn100))
    repeat -= 1
print("Hello", name, "\nYou are", age , "years old.\nYou will turn 100 years old in {}.".format(turn100))