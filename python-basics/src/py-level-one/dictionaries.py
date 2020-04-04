# Dictionaries

## NOTES:
##   1. Dictionaries do not retain any sort of order.
##   2. Can't add methods as item in dictionary unlike javascript

my_dic = {"key1": "value1", "key2": "value2"};
print(my_dic["key1"]);
my_dic = {"key1": 123, "key2": "value2", "key3": {'123': [1, 2, "grab me"]}};
print(my_dic);
print(my_dic["key3"]["123"][2]);    # access a value: "grab me"

my_dic = {"lunch": "pizza", "bfast": "eggs"};
print(my_dic);
my_dic["lunch"] = "burger"
print(my_dic);

my_dic["dinner"] = "pasta";     # add a new item(key-value pair), it's really that easy
print(my_dic);
