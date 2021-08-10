""" 1. List
    2. List as stack and queues(using collections.deque )
    3. List Comprehension
    4. del statement
    6. tuple and sequences
    7. sets
    8. dictionaries
    9. enumerate, zip and reversed function
    """


""" list functions
    -> count, index, reverse, append, sort, pop 
    -> can search more functions using dir(list)
"""

women_clothes = ['halter', 'spaghetti', 'sleeveless', 'peplum', 'mandarin-collar', 'bay-sleeve', 'body-con']
print(women_clothes.count('spaghetti')) #return nummber of times values is present
print(women_clothes.index('peplum'))

women_clothes.reverse()
print(women_clothes)

print(women_clothes.append('full-sleeve'))
print(women_clothes)

women_clothes.sort()
print(women_clothes)

print(women_clothes.pop(len(women_clothes)-1))
print(women_clothes)


"""list used as stack """

stack = [3, 5, 7, 9, 11] # LIFO model

stack.pop()   # pops 11 from stack
print(stack)
stack.append(13)  # pushes 13 in stack
print(stack)

""" list as queues"""

from collections import deque

queue= deque(['Rob', "James", 'Gilly', "Elva", "Samuel"])
queue.append("Sa'Mora")
queue.append("Brain")

queue.popleft()   # removes Rob
queue.popleft()   # removes James

print(queue)  # prints without Rob and James



""" List comprehensions """
# concise way of creating list
#import ipdb; ipdb.set_trace()
list_num = [x for x in range(3, 10) if x % 3 == 0 or x % 5 == 0]
print(list_num)

list_num2= [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x == y]
print(list_num2)


""" using women_clother list to demo del"""
print(women_clothes)

del women_clothes[0] # deleted value from 0th index

print(women_clothes)

# delete full list
# del women_clothes         # keeping uncommted to avoid code error

""" tuples """

tuple_1 = ('2345', 'red', '10', 'rto')
# accessing tuple

print(len(tuple_1))

print(tuple_1[3])

# tuple is immutable hence, not assignable, below line with throw error ''tuple' object does not support item assignment'

# tuple_1[0] = 0

# tuple can contain mutable object, like list, which we can modify
tuple_1 = ([1, 4, 5], [4, 6, 7], [5, 8, 3])
tuple_1[0].insert(2, 9)
print(tuple_1)

# when creating a tuple with one value leave a trailing comma

tuple_1 = ('Hey',)
print(tuple_1)


""" Sets in python- unordered collection with non-duplicate values"""
# empty set are created as below

a = set()
print(type(a))

# set with values
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(type(basket))

# Fast membership testing
print('orange' in basket)  # returns True

# on set you can perform a lot of arithmetic operations like, intersection, union, difference etc.

set1 = set('blabber')
set2 = set('hungers')

print(set1 - set2)          #letters in set1 but not in set2
print(set2 | set1)          #letters in set2 or set2 or both
print(set1 & set2)          #letters in set1 and set2
print(set1 ^ set2)          #letters in set1 or set2 but not both


""" Dictionaries - key value pair data type with unique key"""

# create a dictionary

myPersonalDictionary = {'wake-up': 'early', 'wakeup-time': '8', 'eat': 'clean', 'learn': 'Py&Jap', 'AvoidJunk': 'Yes'}

# printing dictionary
print("Print dictionary:\n", myPersonalDictionary)

print(myPersonalDictionary['wake-up'])

# get value of a key in dict
print("Value of particular key:\n", myPersonalDictionary.get('wake-up'))

# get all keys of a dict
print("Keys:\n", myPersonalDictionary.keys())

# get all values of a dict
print("Values:\n", myPersonalDictionary.values())

# update dictionary
myPersonalDictionary['dress'] = 'purple'
print(myPersonalDictionary)

# fast membership in testing
print('dress' in myPersonalDictionary)
print('dress' not in myPersonalDictionary)

# dictionary comprehension

new_dict= {x: x/2 for x in (19, 20, 21)}
print(new_dict)

# list of keys

print(list(myPersonalDictionary))

# sort dictionary
print(sorted(myPersonalDictionary))

""" enumerate function is used to print the values with indexes"""

for i, v in enumerate(['trippy', 'tip', 'tap', 'toe']):
    print(i, v)


"""  zip function """
questions = ['name', 'school', 'section']
answers = ['Charlie', 'Globus High', 'X-C']
for q, a in zip(questions, answers):
    print(f'What is your {q}?  It is {a}')

marriage =['Venue', 'food', 'groom']
answers = ['laurel_wood way', 'Cakes & pastries', 'Richard']

for q, a in zip(marriage, answers):
    print(f'{q}: {a}')


""" reversed fucntion is used to loop over a sequence in reverse order"""
for i in reversed(answers):
    print(i)
