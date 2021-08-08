"""Practise on topics like if statement, for, pass , break continue, range"""

''' 1. if statement
    2. for loop
    3. range funtion
    4. break, continue and else statements
    
    '''

y = int(input('''Please enter the following to execute:
                    if statements= 1
                    for loop = 2
                    range func= 3
                    break, continue = 4
              '''))
if y == 1:
    ''' if statement implementation'''
    x = int(input("Please enter one number"))
    if x < 0:
        x =0
        print('Negative changed to zero')
    elif x ==0:
        print('Zero')
    elif x==1:
        print('Single')
    else:
        print('More')

elif y == 2:
    fruits = ['dragonfruit', 'peaches', 'avacardo', 'kiwi']
    for fruit in fruits:
        print(fruit, len(fruit))

# range function - It gives arithmetic progression
elif y == 3:
    for i in range(50):
        if i % 10 ==0:
            print(i)

# 'Step' In range function
# you can write step in range function to modify the length and frequency of arithmetic progress in
# step. You can also mention negative number

    for num in range(0, 20, 4):
        print(num)

    for negnumber in range(-1, -20, -4):
        print(negnumber)

# calculating sum of a number starting from 0
    num =9
    print(sum(range(num)))


# break and continue and else statements

elif y == 4:
    print("executing break and continue and else example")
    for n in range(2, 10):
        for x in range(2, n):
    #import ipdb;
    #ipdb.set_trace()
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break

    else:
     # loop fell through without finding a factor
        print(n, 'is a prime number')

# continue statement
    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
            print("Found an odd number", num)

# pass statement
    for num in range(2, 10):
        if num % 2 == 0:
            pass
        else:
            print("Found an odd number", num)
            continue

else:
    print('incorrect option entered, TRY AGAIN!!')
