""" 1.defining functions is def keywords
    2.return statement
    3.default arguments in a function
    4.'In' keyword to check whether a value is present in a sequence
    5. kwargs
   """
import random

'''write a fibonacci series upto n '''
def fibo(n):
    a, b= 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fibo(5)

def f(a, L=None):
    """default parameter L"""
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

""" More on defalut parameter"""
# default arguments are called with fewer or no arguments while calling the function

name =['Aishwarya', 'Bindu', 'Chaya', 'Deepak']


def common_detail(name, city='Chennai', school= "SEC"):
    return (f'{name} is from {city} and he/she attended school in {school}')


for statement in range(4):

    # import ipdb; ipdb.set_trace()
    list1 = name.copy()
    l1 = random.choice(list1)
    statement = common_detail(l1)
    print(statement)


# default arguments are called with fewer or no arguments while calling the function
i = 5


def f(arg=i):
    print(arg)
# i = 6


f()


""" keyword arguments"""

def my_life(state, action="'eatsleepcoderepeat'", wants= "'worksatisfaction'"):
    print(f'My life is {state} and I {action} and I want {wants}')


""" ways of calling kwarg function"""
my_life('ongoing')
my_life('going-good', action='hog on sweets', wants='a sweet factory')
my_life(state='all about eating sweets', action='hog on sweets', wants='a sweet factory')
my_life('chilled', 'rock it everyday', 'peace')


""" *args and **kwargs"""
# *args - takes tuple
# **kwargs - takes dictionary

def beautysalon(haircut, *args, **kwargs):
    print("\nHaircut style:", haircut)
    print("Instructions:")
    for details in args:
        print(details, end='\n')
    print("-"*40)
    for customer_detail,values in kwargs.items():
        print(customer_detail, ":", values)


beautysalon("layer cuts", 'Don\'t make it too short', 'Blow dry properly', Name="Sandra", age="23", address="CA")


