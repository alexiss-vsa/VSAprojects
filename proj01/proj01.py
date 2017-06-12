# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name = raw_input("Enter your first name ")
age = raw_input("Enter your age ")
bday = raw_input("Have you had a birthday this year? Enter y or n ")
if bday=='y':
    aged = 100 - int(age)
    year = int(aged) + 2017
    print ' '
    print str(name) + ' will turn 100 in the year ' + str(year)
elif bday == 'n':
    aged2 = 99 - int(age)
    year2 = int(aged2) + 2017
    print ' '
    print str(name) + 'will turn 100 in the year ' + str(year2)
if int(age)<13:
    print 'You can see movies rated G and PG'
elif int(age)>12 and int(age)<18:
    print 'You can see movies rated G, PG, and PG13'
elif int(age)>17:
    print 'You can see movies rated G, PG, PG13, and R-rated movies'




