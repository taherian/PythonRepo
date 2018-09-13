'''Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)'''
import random
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ranlen = random.randint(1,25)
a = list()
while (ranlen !=0):
    a.append(random.randint(1,99))
    ranlen -=1
print('List A = ',a)
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print('List B = ',b)
lengh = [len(a), len(b)]
clist = list()
for i  in range(0 , (lengh[0])):
    for j in range(0 , (lengh[1])):
        if a[i] == b[j]:
            clist.append(a[i])
if (len(clist)>0):
    print('\nList C comprised by common numbers between list A and B:', clist)
else:
    print('\nThere is no overlap between these two lists.')