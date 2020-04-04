# Booleans

## NOTES:
##     1. Values: True, False, 0, 1
if True:
    print(True);
else :
    print(False);

# Tuples

## NOTES: 
##     1. Difference with Lists is Tuples are immutable. Can't do this: my_tuples[0] = 5;
##     2. Indexing and Slicing are same as Lists

my_tuples = (1, 2, 3);
print(my_tuples);
my_tuples = ('a', True, 123);
print(my_tuples);
print(my_tuples[1]);

# Sets

## NOTES:
##     1. Sets contain only unique items
##     2. Sets are unordered

my_sets = set();
my_sets.add(3);
my_sets.add(2);
my_sets.add(3);
print(my_sets);