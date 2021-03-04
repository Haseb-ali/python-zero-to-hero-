'''
=======================
Python use dynamic typing don't know about dynamic typing 🤔 don't worry let me explain 
dynamic typing is basically a machanisim in which python assing data type to a variable on the base of assign data
to it
=======================
'''
first_name="Haseeb"
last_name="ali"
print(first_name,last_name)
'''
=======================
Hurry 🎉🎉, you have successfully declare variables in python and print them on screen make sure you
tried your own name in first and last name varaible now we see dynamic typing first we check type of 
these two variables by using type function in python.Let me create some more variable for making example 
easy to understandable
=======================
'''
'''
=======================
below print statement out put
<class 'str'> <class 'str'>
<class 'float'>
<class 'int'>
<class 'list'>
=======================
OMG , we did not assing any type to our variables in above and below code but python is enough smart 
it detect data type on the base of assing value
=======================
'''
PI=3.14444444444444444444444444444444
makrs=120
fruits=['apple','banna','orange']
print(type(first_name),type(last_name))
print(type(PI))
print(type(makrs))
print(type(fruits))
'''
=======================
Assign multiple values
=======================
'''
var1,var2,var3=1,2,3 #it will assing values on the base of order you assing  your  values
print(var1,var2,var3)#print these three variables
'''
=======================
Assign one value to multiple variables
=======================
'''
var1=var2=var3=1 #it will assing one value to all left side variables 
print(var1,var2,var3)#print these three variables
'''
=======================
function that is trying to change a golobal variable first_name without global keyword
without global keyword it will not change value because of scope of variable do you  
about variables scope ignore it if you don't know about it let me explain about scope
every programming provide to type of scope on is local scope second one is gloabl scope 
local scope limited to block level like funtons classes and any block you made in program
global scope is totally opposite of local scope it's not limited to any block or classes
so if you want to change a global variable value in python you need to use gloabl keyword to
target global variable that is i am doing in change_name_with_global_keyword function don't
be hasitate with function we will see in later
=======================
'''
def change_name_with_out_global_keyword():
    first_name='ali'
change_name_with_out_global_keyword()
print(first_name)
'''
=======================
function that is trying to change a golobal variable first_name using gloabl keyword
=======================
'''
def change_name_with_global_keyword():
    global first_name
    first_name='ali'
change_name_with_global_keyword()
print(first_name)


