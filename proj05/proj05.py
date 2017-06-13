# # proj05: functions and lists
#
# # Part I
#
def divisors(num):

#        Takes a number and returns all divisors of the number, ordered least to greatest
#     :param num: int
#    :return: list (int)

    ans_list = []
    for n in range(1,num+1):
        #print "num =", num, "n =", n
        if num % n == 0:
            #print "is divisor"
            ans_list.append(n)
            #print ans_list , 'is ans list'
    return ans_list


def prime(num):
#     """
#   #  Takes a number and returns True if the number is prime, otherwise False
#     :param num: int
#     :return: bool

    divisors_list = divisors(num)
    if len(divisors_list)>2:
        return False
    else:
        return True
#
# # Part II
#

newlist = []

def intersection(lst1, lst2):
    newlist = []
    #lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    #lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for number in lst1:
        if number in lst2 and number not in newlist:
            newlist.append(number)
    return newlist


# # Part III

def find_ab(side1, side2, side3):
    if side1>side2 and side1>side3:
        return side2 , side3
    if side2>side1 and side2>side3:
        return side1 , side3
    if side3>side1 and side3>side2:
        return side1 , side2

    """
    """
    return [0, 0]

def find_c(side1, side2, side3):
    if side1>side2 and side1>side3:
        return side1
    if side2>side1 and side2>side3:
        return side2
    if side3>side1 and side3>side2:
        return side3

    """
    """
    return 0

def square(side1, side2, side3):
    return side1**2 , side2**2 , side3**2

#     """
#  Takes a side length and returns the side length squared
#  :param side: int or float
# :return: int or float
#     """

def pythagorean(a,b,c):

    if a**2 + b**2 == c**2:
        print "is a right triangle"
        return True
    else:
        print "is not a right triangle"
        return False

pythagorean(3,4,5)



    # """
    # Takes three side lengths and returns true if a^2 + b^2 = c^2, otherwise false
    # :param a: int or float
    # :param b: int or float
    # :param c: int or float
    # :return: bool
    # """
    #return False

def is_right(side1, side2, side3):
   



    # Takes three side lengths and returns true if triangle is right
    # :param side1: int or float
    # :param side2: int or float
    # :param side3: int or float
    # :return: bool




# TESTS
# Feel free to add your own tests as needed!

print ("Divisors Tests")
# Test 1
if divisors(1) == [1]:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

# Test 2
if divisors(8) == [1,2,4,8]:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")

# Test 3
if divisors(9) == [1,3,9]:
    print("Test 3: PASS\n")
else:
    print("Test 3: FAIL\n")

print("Prime Tests")
# Test 4
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

# Test 5
if prime(7):
    print("Test 5: PASS\n")
else:
    print("Test 5: FAIL\n")

L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]

print("Intersection Tests")
# Test 6
if intersection(L1, L2) == []:
    print("Test 6: PASS")
else:
    print("Test 6: FAIL")

# Test 7
if intersection(L2, L3) == [3]:
    print("Test 7: PASS")
else:
    print("Test 7: FAIL")

# Test 8
if intersection(L2, L4) == []:
    print("Test 8: PASS")
else:
    print("Test 8: FAIL")

# Test 9
if intersection(L3, L4) == ["a"]:
    print("Test 9: PASS")
else:
    print("Test 9: FAIL")

# Test 10
if intersection(L4, L5) == [5, 7]:
    print("Test 10: PASS\n")
else:
    print("Test 10: FAIL\n")

print("Is_Right Tests")
# Test 11
if is_right(5, 3, 4):
    print("Test 11: PASS")
else:
    print("Test 11: FAIL")

# Test 12
if is_right(9, 3, 4):
    print("Test 12: FAIL")
else:
    print("Test 12: PASS")

