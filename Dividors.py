'''Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)'''

usrno = int(input('Please enter a number: '))
dividors = usrno
divlist = list()
while dividors > 0:
    if usrno % dividors == 0:
        divlist.append(dividors)
    dividors -=1
print(divlist)