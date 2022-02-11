this_list = ["apple", 2, "cherry"]
another_list = [1, 2, 3.3]
print (len(another_list))
print (this_list.index ("cherry"))
this_list.append ("orange")
this_list.insert(3, "kiwi")
print(this_list)


old_list = [1, 2, 3]

# copy list using =
new_list = old_list.copy()

# add an element to list
new_list.append ("a")

print ("New List:", new_list)
print ("Old List:", old_list)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict["brand"])


dict_1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

dict_2 = {
    "brand": "Chevi",
    "model": "Malibu",
    "year": 2020
}

my_list = [dict_1, dict_2]
print (my_list[1]["model"])