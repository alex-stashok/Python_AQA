##Примеры
#
#x= 5
#print (type(x))
#
#x= "Hello World"
#print (type(x))
#
#x= 20.5
#print (type(x))
#
#x= ["apple", "banana", "cherry"]
#print (type(x))
#
#x= ("apple", "banana", "cherry")
#print (type(x))
#
#x= {"name" : "John", "age" : 36}
#print (type(x))
#
#x= True
#print(type(x))


# 5.0 <class 'float'>
x = 5
x = float(x)
print (x, type(x))

# 5 <class 'int'>
x = 5.0
x = int(x)
print (x, type(x))

# Воспользуйтесь методом len(), чтобы определить длину строки

x = "Hello World"
print (len(x))

# Выведете на консоль первый символ строки txt.

txt = "Hello World"
x = (txt [0])
print (x)

# Напишите программу, которая выводит на консоль символы фразы "Hello World" со второго по пятый включительно.

txt = "Hello World"
print (txt [1:5])

#Даны две строки "Hello World" и  " Hello World ". Используя переменные проверьте эти строки эквивалентны или нет.
#Если нет, преобразуйте вторую строку так, чтобы она была эквивалентна первой и убедитесь в этом.

a = "Hello World"
b = " Hello World "
if a == b:
    print ("The string are equael!")
else:
    print ("The string are not equael!")

print (b.strip()) # returns "Hello World"

# Преобразуйте строку  "Hello World" так, чтобы она выводилась на консоль строчными буквами

txt = "Hello World"
print (txt.lower())

# Преобразуйте строку  "Hello World" так, чтобы она выводилась на консоль заглавными буквами

txt = "Hello World"
print (txt.upper())

# Напишите программу, которая заменит в строке "Hello World" букву H на букву J.

txt = "Hello World"
print (txt.replace("H","J"))

# Напишите программу, которая преобразует строку "Hello World" в строку "Hello Word"

txt = "Hello World"
print (txt.replace("rld","rd"))

# У вас есть переменная my_age. Присвойте ей значение и напишите программу, которая выведет на консоль сообщение,
# в котором вместо многоточия будет значение переменной. Возраст может быть произвольным. ;-)

my_age = 31
print ("I am " + str(my_age) + " years old.")

#Напишите программу, которая выведет на консоль сообщение, в котором вместо многоточия будет случайное значение.
# Запустите программу не менее пяти раз, чтобы убедиться, что значение случайное.

import random

random_val = random.randint(1, 100)
print (f"I made this mistake {random_val} times.")












