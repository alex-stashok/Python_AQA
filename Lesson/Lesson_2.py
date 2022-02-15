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

x = 41
if x > 10:
    print ("Above ten,")
    if x > 20:
        print ("and also above 20!")
    else:
        print ("but not above 20.")

# while  Break

i = 1
while True:
    print (i)
    if i == 3:
        break
    i += 1

# while Continue

i = 0
while i < 6:
    i += 1
    if i == 3:
     continue
    print (i)

# while Continue

i = 0
while i < 6:
    i += 1
    if i in [3,5]:
     continue
    print (i)

# while Pass

i = 0
while i < 6:
    i += 1
    if i in [3,5]:
     pass
    print (i)

# while Continue

i = 0
my_list = [3, 5]
while i < 6:
    i += 1
    if i in my_list:
     continue
    print (i)

# while Continue

i = 0
my_limit = 6
my_list = [3, 5]
while i < my_limit:
    i += 1
    if i in my_list:
     continue
    print (i)

# For

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print (x)

# For

fruits = ["apple", "banana", "cherry"]
new_list =[]
for x in fruits [1]:
    new_list.append (x)
    print ("".join(new_list))

# For

fruits = ["apple", "banana", "cherry"]
new_list =[]
for x in range (0, 3, 1):
    print (fruits [x])

# Def

def my_function (a, b):
    c = a + b
    return c

first_val = 5
second_val = 7

result = my_function (first_val, second_val)

print (result)

# Def

def my_function (a, b=2):
    c = a + b
    return c

first_val = 5
second_val = 7

result = my_function (first_val, second_val)

print (result)

# Def

def my_function (a, b=2):
    c = a + b
    return c

first_val = 5
second_val = 7

result = my_function (first_val, second_val)

print (result)


