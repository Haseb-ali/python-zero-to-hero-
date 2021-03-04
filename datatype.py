'''
=======================
in this file we will cover python data types acctually data types are type of data you can 
store in a variable all programming language provide some basic data types like int,char,str
bool,complex python also provide these and some extra also included like list,tuple,set,dict,
bytes,bytearray,memoryview we cover all in depth.
=======================
'''
'''
=======================
List of provided data type
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview

=======================
'''

'''
=======================
Text Type: 	str
str use to store sring and charaters in python 
we use single,double,triple qoutes in python to 
assing a string data to a variables read below 
code you will get my point.
=======================
'''
#coding example for str/string data type
programming_language_name_s='Python' # used single quotes
programming_language_name_d="Python"# used double quotes
programming_language_name_t='''Python'''# used triple quotes
#all are vaild
#print all these variable in screen
print(programming_language_name_s)
print(programming_language_name_d)
print(programming_language_name_t)

'''
=======================
Numeric Types: 	int, float, complex
Numeric types are used to store number data in python 
int use to store interger values that are decimal free
float use to store floating point values 
complex use to store complex values into variables
don't worry we see detail cde example of all below
=======================
'''
#coding example for int,float,complex data type
PI=3.144444444444444444444444 # float use print(type(PT)) to check type of variable
laptop_bettry_percentage=90# int use print(type(laptop_bettry_percentage)) to check type of variable
complex_data_type=1j# complex data type use print(type(complex_data_type=)) to check type of variable
#print all these variable in screen
print(PI)
print(laptop_bettry_percentage)
print(complex_data_type)



'''
=======================
Sequence Types: list, tuple, range
Sequence types are used to store sequence of values into memory for example Sequence of fruits,brands
anything you can put into a Sequence this is not type specific you can mix different data typess into
one Sequence.
list use to store list of items into memory not depended on type of data
exmaple
fruits=['apple','banna','orange']
you can mix different types into single list
fruits=['apple','banna','orange',12,0.333,1j]
tuple use to store tuple of value into memory same as list but you can not change value of tuples 
range is used to create sequence 
like 1.......10
100.........1000 
like that
=======================
'''
#coding example for list,tuple,range data type
fruits=['apple','banna','orange'] # list use print(type(fruits)) to check type of variable
fruits_tuple=('apple','banna','orange')# int use print(type(fruits_tuple)) to check type of variable
dummpy_numbers=range(6)# complex data type use print(type(dummpy_numbers)) to check type of variable
#print all these variable in screen
print(fruits)
print(fruits_tuple)
print(dummpy_numbers)



