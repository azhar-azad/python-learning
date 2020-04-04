# Comparison Operators

## Greater than:    >
## Less than:       <
## Greater than or Equal to:   >=
## Less than or Equal to:      <=
## Equality:        ==
### 1 == 1 -> True, 1 == '1' -> False i.e. no type conversion in Python
## Inquality:       !=

# Logical Operators

## AND:     and
## OR:      or

# if-elif-else

## NOTES:
###     1. No () or {}, intendation is the way to define code blocks

if 1 < 2:
    print("First if Block");
    if 20 < 3:
        print("Second if Block");

if 1 < 2:
    print("if Block");
elif 2 > 3:
    print("elif Block");
else:
    print("else Block");

# loops

## range function:
print(list(range(5)));      # [0, 1, 2, 3, 4]
print(list(range(0, 5)));   # [0, 1, 2, 3, 4]
print(list(range(1, 5)));   # [1, 2, 3, 4]
print(list(range(1, 10, 2)));   # [1, 3, 5, 7, 9]
print(list(range(0, 10, 2)));   # [0, 2, 4, 6, 8]

## for loops

list = [1, 2, 3, 4, 5, 6];   # a list

for item in list:
    print(item);


dict = {"Sam": 1, "Frank": 2, "Dan": 3};

for key in dict:
    print(key);         # print the key
    print(dict[key]);   # print the value

for item in dict.keys():
    print(item);        # print keys

for item in dict.values():
    print(item);        # print values


my_pairs = [(1, 2), (3, 4), (5, 6)];

for item in my_pairs:
    print(item);        # prints the tuples one by one

for tup1, tup2 in my_pairs:
    print(tup1);        # print the first item of a tuple
    print(tup2);        # print the second item of a tuple


## while loops

index = 1;
while index <= 5:
    print("index is {}".format(index));
    index = index + 1;


# list comprehension

list = [1, 2, 3, 4];

## without list-comprehension
sqr_list = [];
for item in list:
    sqr_list.append(item**2);
print(sqr_list);

## with list-comprehension
sqr_list = [item**2 for item in list];
print(sqr_list);
