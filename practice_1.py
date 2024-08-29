# Swap variables a and b

"""a = "x"

b = "y"

print(a,b)

c = a

a = b

b = c

print(a,b)

a = [1,2,3]

b = [3,2,1]

print(a,b)

x = list (b)

y = list (a)

a = x

b = y

print(a,b)"""

# Alice, Bob and Carol have agreed to pull their halloween candy and split it evenly among themselves. 
# Any candy left over will be smashed. How many candies they must smash for a given haul?

"""def halloween_candy (n):
    x = n % 3
    print(x)

halloween_candy(100)"""

# Round to two places (3.14159)

"""x = 3.14159
a = round(x,2)
print(a)"""

# There is a list to record people who attended our party and what order they arrived in. A guest is considered
# fashionably late if they arrived after at least half of the party's guest. However, they must not be the very last. 
# Make a function that takes a list of attendees and a person and tells us if that person is fashionably late

"""def fashionably_late(attendees,person):
    a = attendees.index(person)
    print("person is late") if a >= len(attendees)/2 and a != len(attendees)-1 else print ("person isnt late")

fashionably_late(attendees= ["Adela", "Fleda", "Owen", "May","Mona","Gilbert","Ford"],person="Mona")"""

# John has a list of monthly expenses from last year:
# monthly_spending = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120].
# He wants to know average expenses in each semester

"""def avgexp(a):
    b = []
    for x in a:
        if (a.index(x))<len(a)/2:
            b.append(x)
    print("Average expense in first semester:", sum(b) / len(b))

    c = []
    for x in a:
        if (a.index(x))>=len(a)/2:
            c.append(x)
    print("Average expense in second semester:", sum(c) / len(c))

avgexp([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])"""

# John and Sam kept their expenses list from last year and they want to know for how many months 
# John spent more than Sam.

"""def compare(a,b):
    x = []
    for index, (value_a, value_b) in enumerate (zip(a,b), start = 1):
        if value_a > value_b:
            x.append(index)
    print(x)

compare(a=[20,30,40],b=[10,20,60])"""


# For a list of strings create a function that does two things: filter out any words with three or fewer characters
# and sort the resulting list alphabetically.

"""def filtersort(a):
    filtered_list = [word for word in a if len(word)>3]
    filtered_list.sort()
    print(filtered_list)

filtersort(["apple", "banana", "car", "computer", "bed", "TV"])"""

#factorial problem

"""def factorial(num):
    if (num > 0):
        result = num*factorial(num-1)
    else: result = 1
    return (result)

print(factorial(5))"""


"""def factorial(num):
    x = 1
    a = b = num
    while x < b:
        num = num*(a-x)
        x = x+1
    return(num)

print(factorial(5))"""

"""def factorial(num):
    result = 1
    for x in range(1,(num+1)):
        y = (num+1)-x
        result = result*y
    return(result)

print(factorial(5))"""


# Symmetrical problem

def is_palindrome(string):
    newString = string.lower()

    print(newString[::1] == newString[::-1])
    
is_palindrome("Racecar")



"""def find(a):
    y = sorted(a,reverse=True)
    return y[1]
print(find([23,78,96,32]))"""


"""def reverse_string (a):
    b = list(a)
    c = []
    string = ""

    while (len(b)):
        c.append(b.pop())
    for x in c:
        string += str(x)
    print(string)
reverse_string("apple")    """

"""def count_vowels(string):
    b = []
    for char in string:
        if char in 'aeiou':
            b.append(char)
    print(len(b))


count_vowels('aaple')"""


    


    
    
    

    






      
    



