#proj04
#Asks the user for a string and prints out whether or not the string is a palindrome.

print 'A palindrome is a word or phrase that is the same forwards and backwards. Type something to see if its a palindrome!'
print ' '
uword = str(raw_input('Enter a word or phrase '))
length = len(uword)

#shortcuts for me
no = ' is not a palindrome :('
yes = ' is indeed a palindrome! :D'

#for making stuff reverse
rword = uword[::-1]

#for making stuff lowercase
rwordn = rword.lower()

uwordn = uword.lower()

#removing spaces
uwordf = uwordn.replace(" ","")
rwordf = rwordn.replace(" ","")

#palindrome or nah?
if rwordf == uwordf:
    print uword + yes
elif rwordf != uwordf:
    print uword + no
