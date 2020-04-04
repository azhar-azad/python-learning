# STRINGS

# Basics

my_string = "ABcdefgh";
print('hello');
print("hello");
print("I'm saying hello!!");
print(my_string);

# Indexing

print(my_string[0]);    # gives starting character
print(my_string[-1]);   # gives ending character

# Slicing

## full syntax = string_name[start_index : end_index (up to but not included) : step size (optional)] 
print(my_string[0:]);   # gives whole string
print(my_string[:4]);   # gives string from index 0 to index 3 (index after : will not be included) : ABcd
print(my_string[2:6]);  # gives string from index 0 to index 5 : cdef
print(my_string[::1]);  # gives whole string because step size is one (stop at each index and pick the value)
print(my_string[::2]);  # gives 'Aceg' (stop at every other index and pick the value)

# Basic Methods

print(my_string.upper());   # gives the string in upper case
print(my_string.lower());   # gives the string in lower case
print(my_string.capitalize());  #gives the string in first letter upper and rest lower
my_string = "hello world!!";
print(my_string.split());   # gives an array of words containing my_string (by default it splits on whitespace)
print(my_string.split('e'));   # gives an array of words split by the character passed as argument in the method
print(my_string.split('o'));    # gives ['hell', ' w', 'rld!!']

# Print Formatting

my_string = "Insert another string here: {}".format("INSERT ME!!");
print(my_string);   # Insert another string here: INSERT ME!!
my_string = "Item one: {}, two: {}".format("dog", "cat");
print(my_string);   # Item one: dog, two: cat
my_string = "Item one: {x}, two: {y}".format(x = "dog", y = "cat");
print(my_string); # Item one: dog, two: cat
