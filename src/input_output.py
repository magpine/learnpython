import json
"""
1. f strings or formatted strings
2. The String format
3. str and repr
4. Manual string formatting
5. reading and writing files
"""

"""f string examples"""
name = "Magpine"
who = "coder"

print(f'{name} is a {who}')

"""str format requires more manual efforts"""
print('{0} is a {1}'.format(name, who))

"""str() and repr"""

name = "Joe"
print(str(name))  # prints human readable format

name = "Joeey"
print(repr(name))  # prints interpreter readable format. The argument to repr() may be any Python object

print(repr((('a, b', 'c'), (name,), (who,))))

""" spacing between strings can be done using fstring """

phn_dict = {'sam': 980, 'jack': 123, 'rob':234, 'julie': 645}

for k, y in phn_dict.items():
    print(f'{k:10} ==> {y:10d}')

# neatly spaced outputs
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# aligning the string towards the left, similar can be done with rjust and centre
for x in range(1,11):
    print(repr(x).ljust(2), repr(x*x).ljust(3), repr(x*x*x).ljust(4))


""" reading and writing files """
#with open('data_structures.py', 'a') as f:
#    f.write('written')

""" reading a file"""
with open('data_structures.py', 'r') as f:
    for line in f:
        print(line, end='')

"""reading and writing by using JSON"""

with open('read_write.py', 'w') as fwr:
    x =[1, 'cute', 'list']
    json.dump(x, fwr)

with open('read_write.py', 'r') as fr:
    reload_x = json.load(fr)
    print(reload_x)

