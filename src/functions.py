""" 1.defining functions is def keywords
    2.return statement
    3.default arguements in a function
    4.'In' keyword to check whether a value is present in a sequence
    5.
   """

'''write a fibonacci series upto n '''
def fibo(n):
    a, b= 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fibo(5)



def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
