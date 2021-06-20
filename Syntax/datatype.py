# TODO:Need to revise these concepts and update this file


# list
# tuple
# dictionary
# set

# LIST
myTodo_List = ["Nihongo", 200000, True, 1.0002, "tusk" , "tody", -1]
imp_task = myTodo_List[0]
print(imp_task)

myTodo_List[0] = "Python"
myTodo_List.append('learning')

print(myTodo_List)
print(dir(myTodo_List))


# TUPLE


new_tuple = ("python", "learn")
new_tuple2 = ("nihongo", "jap_Class")
final_tuple = (new_tuple2, new_tuple)
print(final_tuple)


# SETS

name_set = {"riya", "dhruva", "aanchu"}
print(name_set)
print(type(name_set))


# DICTIONARIES

new_dict = {'anurag': 'fat', 'neha': 'slim', 'chotu': 'bad', 'motu': 'good'}
print(new_dict['chotu'])
print(new_dict.values(), new_dict.keys(), new_dict.items());

new_dict['chotu']= 'average'
print(new_dict)

new_dict.update({'anurag': 'slimtoo'})
print(new_dict)

new_dict.update({'ruby': 'stone'})

print(new_dict)

del new_dict['ruby']
print(new_dict)

# dir-keyword

dir(new_dict)

