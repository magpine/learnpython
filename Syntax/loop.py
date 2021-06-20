# TODO:Need to revise these loops and write loop for set datatype

# mylist1 = ["dog", "cat", "mantu", 1, 14, 27, 1.0]
#
# for values in mylist1:
#
#      if ( values == "dog"):
#          newlist = [values]
#          print(newlist)
#
#
#
#
#
# list_comprehension = ["yes" for val in mylist1 if val == "dog" or val == "cat"]
# print(list_comprehension)

#for loop for tuple
tuple1 = ("dog", "cat", "mantu", 1, 14, 27, 1.0)
for val in tuple1:
    # print(val)

    if (val == "dog"):
        newtuple = (val)
        print(newtuple)

list_comprehension = [val for val in tuple1 if val == "dog" or val == "cat"]
print(list_comprehension)

# Dictionary

thisdict = {
    "like": "orange",
    "dislike": "blackcurrent",
    "dress": "mini",
    "top":"jumpsuit"

}

# for x in thisdict:
#     print(x)
#
# for x in thisdict:
#  print(thisdict[x])
#
# for x in thisdict.values():
#     print(x)
#
# print(thisdict.items())
#
# for x, y in thisdict.items():
#     print(x, y)
#
# print(thisdict.get("like"))


# thisdict["year"]= 1993
# thisdict["status"]="False"




# if "like" in thisdict:
#     print("yes")
#
# thisdict.update({"year": 2001})
#
# for x, y in thisdict.items():
#      print(x, y)

newset = {"runningsuit", "trouser", "bellbottomjeans", "belt"}

#iterate the set

