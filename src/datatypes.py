""" Here is the list data types in python and examples how to work with it"""

''' Lists 
    1. creating list
    2. append()
    3. concatenation of lists
    4. len()
    5. list indexing and slicing
    6. change element at a position
    7. clearing list by slicing
    8. nested listed 
    '''

# 1.creating list

fruits = ['Apple', 'Mango', 'Banana', 'Jackfruit']

# 2.use append() function in the list

fruits.append('Guava')
print(fruits)

# 3. concatenation of list
print(['chocolate', 'cake', 'cookies'] + fruits)

# 4. len() funtion to print the length of the string
print(len(fruits))

#5. list indexing and slicing

''' indexing'''
print(fruits[1])

''' slicing, first 2 fruits'''
print(fruits[0:2])

'''slicing, 2nd last fruit'''
print(fruits[-2:-1])

# 6. updating a particular element

''' replacing Mango with orange using index() of list'''
i = fruits.index('Mango')
fruits[i] = 'orange'
print(fruits)

''' now replacing values from 2nd element to 3rd element'''
fruits[1:3] = ['berry', 'Papaya']
print(fruits)

'''
7. deleting list by slicing
'''
fruits[ : ] = []
print(fruits)

'''
nested list, lists within a list
'''
nestlist = [[2, 4, 6, 8], ["sugar", "flour", "salt"], ['x', 'y', 'z']]
print(nestlist[0])
print(nestlist[1][1])
print(nestlist[2][1])

