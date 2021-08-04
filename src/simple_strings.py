""" working with string literals and their manipulation"""


# Topic
# 1. usage of \' to escape the single quote. or use double quote instead
# 2. Raw strings
# 3. doc strings """..."""" or '''...''' inside print()
# 4. String concatenation with + or *
# 5. Automatic concatenation of string(string and string only.Doesn't work with variable and string)
# 6.Indexed string and string slicing
# 7. String are immutable
# 8. Inbuilt function len

''' how to escape quote in a string if using single quotes'''

my_string = '\"Yes\", I said'
print(my_string)
# OR
my_string1= "'Yes', I said"
print(my_string)


'''raw string is used when you dont want the word prefixed with \ to be interpreted as a special character'''
# Before
new_string = 'C:\folder\read'
print(new_string)

# After raw string
new_string_again = r'C:\folder\read'
print(new_string_again)


""" using doc string inside print() function- it does not print the first empty line if you prefix '\' """

print("""\
Learn Python: 
    1. practise             step 1
    2. update repository    step 2
    3. share                step 3
    4. repeat step 1, 2, 3
""")


""" string concatenation"""
var= 2 * ' yum ' + 'yummy'
print(var)


""" Auto concatenation"""
print('This is my learning python practise repo.' ' I am enjoying it very much')

""" string indices and string slicing """

str= "Mango and Ice-cream"
# to print char I
print(str[10])

# To print "Man"
print(str[0:3])

# similarly to print 'cream'
print(str[-5:])

""" string immutability means you can't change the an existing string variable value"""
# from above example of str

# str[10] = 'G'
# print(str)
print("""\
You will get error if above statements were not commented
     ++++++++++++++++IGNORE THIS WARNING+++++++++
Traceback (most recent call last):
  File "simple_strings.py", line 67, in <module>
    str[10] = 'G'
TypeError: 'str' object does not support item assignment
    +++++++++++++++++++++++++++++++++++++++++++++
""")

""" append a character in front of the word Ice-cream and make it Gcream """
print('G'+ str[-4:])

""" Usage of len() function to find the length of the string """

s = "Inheritentawesomenessquoitent"
print(len(s))

