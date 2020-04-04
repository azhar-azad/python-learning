###############
## Problem 1 ##
###############

# Given the string:
str = "django";

# Use indexing and slicing to print the following:
# d, o, djan, jan, go
print(str[0]);      # d
print(str[5]);      # o
print(str[:4]);     # djan
print(str[1:4]);    # jan
print(str[4:]);     # go

# Bonus: Use indexing to reverse the string
print(str[::-1]);   # ognajd [start(begin):end(last):step(-1) --> step = -1 means go one step backward]

###############
## Problem 2 ##
###############

# Given the nested list:
list = [3, 7, [1, 4, "hello"]];

# Reassign "hello" to be "goodbye"
list[2][2] = "goodbye";
print(list);        # [3, 7, [1, 4, 'goodbye']]

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the "hello" from the following dictionaries:
dict1 = {"simple_key": "hello"};
dict2 = {"k1": {"k2": "hello"}};
dict3 = {"k1": [{"nest_key": ["this is deep", ["hello"]]}]};

print(dict1["simple_key"]);
print(dict2["k1"]["k2"]);
print(dict3["k1"][0]["nest_key"][1][0]);
# for understanding:
print(dict3);                           # {"k1": [{"nest_key": ["this is deep", ["hello"]]}]}
print(dict3["k1"]);                     # [{'nest_key': ['this is deep', ['hello']]}]
print(dict3["k1"][0]);                  # {'nest_key': ['this is deep', ['hello']]}
print(dict3["k1"][0]["nest_key"]);      # ['this is deep', ['hello']]
print(dict3["k1"][0]["nest_key"][1]);   # ['hello']
print(dict3["k1"][0]["nest_key"][1][0]);    # hello

###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
my_list = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3];

print(set(my_list));    # {1, 2, 3}


###############
## Problem 5 ##
###############

# You are given two variables:
age = 4;
name = "Sammy";

# Use print formatting to print the following string:
# "Hello my dog's name is Sammy and he is 4 years old"
print("Hello my dog's name is {} and he is {} years old".format(name, age));
print("Hello my dog's name is {a} and he is {b} years old".format(a=name, b=age));
