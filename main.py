#COMMENTS
# this is a one line comment

import csv
import math
"""
this is
a multi
line commnet
"""

#GETTING INPUT FROM THE USER
print("Enter a number:")
num=input()#num is a variable
# what type is num?
print(type(num))
print("The number doubled is:",2*num)



#we need to convert num from a string
# to a  integer
num_int=int(num)
print("The number doubled is:",2*num_int)

#CONDITIONALS (IF STATEMENTS)
#if some condition is true
#then execute some code
x = 10
if x == 5:
    print("x is 5")
elif x== 7:
    print("x is 7")
else:
    print("x is not 5 and x is not 7")

#LOOPS
# use a loop when you want to repeat code
#we have for loops and while loops in python
#for item in sequence:
# body of for loop (code you want repeated)
for character in "python":
    print(character)

#we can also make our own sequences
#with range(start,stop,step)
for i in range(0, 5, 1):
    print(i)
for i in range(5):
    print(i)
for i in range(0, 5):
    print(i)

#task:write a for loop to print
#the first 20 even numbers
#2,4,...,38,40
for i in range(2,42,2):
    print(i,end=" ")
print()


#while loops
#while condition is true:
#body of loop (code to be repeated)
#progress towards the condition
#being false
#let's re-write our for loop
#with a while loop

i=2
while i <=40:
    print(i,end=" ")
    i +=2#progress

#note that conditionals and loops
#can be nested inside each other
#just pay attention to the indentation

#FUNCTIONS
#a named sequence of statements
#we have been using pre-denfined
#functions
#now,we define our own functions
#def function_name(parameter list):
#body of funciton (code to run
# when function is "called")
#funtions don't run until they are
#called

#example #1
#function with no inputs and no
#return
def say_hello():
    print("hello")
    
#we nedd to call the function
 # for it to run
for i in range(10):
    say_hello()#call
    
#example #2
#function with one input and no
#retrun
def say(message):
    print(message)

say("hi!!")
say("how are you")
say("goodbye...")

#example #3
#function with one input 
#and one return (output)
def compute_circle_area(radius):
    area =3.14 * radius ** 2
    return area #send back to
    #calling code


result = compute_circle_area(5)
print("result:",result)

#List
#a list a sequence of items
#-3右边往左数，1从左边往右数
list_ints=[10,4,-2,9]
print(list_ints)
print(list_ints[1],list_ints[-3])

#lists are mutable
#they can be changed
list_ints[0]=4000
print(list_ints)

#items in a list can have mixed type
list_ints[-1]="hello"
print(list_ints)


#use len() function can have mixed
#how many items are in a list
print(len(list_ints))
#add another item
list_ints.append(42)#add to end
print(len(list_ints))

empty_list=[]
print(len(empty_list))

#we can have a list of lists
#called a nested  list
nested_list=[[0,1],[2,3],[],[8]]
print (nested_list)
print(nested_list[1])
print(nested_list[1][1])

#looping through list items
cities=["hangzhou","beijing","shanghai"]
for city in cities:
    print(city)

#task:try writing the above for loop
#using a while loop

i = 0
while i < len(cities):
    print("i:",i,"cities[i]:",cities[i])
    i += 1

#common list operators
print(cities)
#list concatentaion
#adding 2 lists together
cities += ["shenzhen","chongqing"]
print(cities)

#list repetition
#repeating items in a list
repeated_list=3 *["guangzhou","tianjin"]
print(repeated_list)

#list slicing
#get some items from a list
print(cities)
print(cities[1:3])

#start index:stop index
#start index is included
#stop index is not included
print(cities[:2])
print(cities[2:])

cities_copy=cities[:]
print("copy:",cities_copy)
cities_copy[0]="CHONGQING"


print("copy:",cities_copy)
print("original:",cities)

cities.append("new york city")
print(cities)

#remove() delete item based on value
cities.remove("chongqing")
print(cities)

#pop() delete item based on index
cities.pop(-1)
print(cities)

string_list=["da","jia","hao"]

one_string="****".join(string_list)
print(one_string)

comma_separated_value_String="da,jia,hao"


sl2=comma_separated_value_String.split(",")
print(sl2)


star_separated_value_string="da***jia***hao"
sl3=star_separated_value_string.split("***")
print(sl3)


#data.csv must
filename="data.csv"

#1.open file
infile=open(filename,"r")

#2.read from file
reader= csv.reader(infile)
table=[]

for row in reader:
    print(row)
    table.append(row)
    
#3.close the file
infile.close()

print("after closing file,table:")
print(table)


table.pop(0)



