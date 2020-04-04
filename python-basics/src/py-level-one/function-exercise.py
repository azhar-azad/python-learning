#################
## Problem - 1 ##
#################
#
# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.
#
# For example:
#
# array_check([1, 1, 2, 3, 1]) -> True
# array_check([1, 1, 2, 4, 1]) -> False
# array_check([1, 1, 2, 1, 2, 3]) -> True

print("PROBLEM 1");

def array_check(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True;
    return False;

print(array_check([1, 1, 2, 3, 1]));
print(array_check([1, 1, 2, 4, 1]));
print(array_check([1, 1, 2, 1, 2, 3]));
print("#################");

#################
## Problem - 2 ##
#################
#
# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yelds "Hlo".
#
# For example:
#
# string_bits("Hello") -> "Hlo"
# string_bits("Hi") -> "H"
# string_bits("Heeololeo") -> "Hello"

print("PROBLEM 2");

## simple way using slicing
# def string_bits(str):
#     return str[::2];

# standard way
def string_bits(mystring):
    result = "";
    for i in range(len(mystring)):
        if i % 2 == 0:
            result = result + mystring[i];
    return result;

print(string_bits("Hello"));
print(string_bits("Hi"));
print(string_bits("Heeololeo"));
print("#################");

#################
## Problem - 3 ##
#################
#
# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be 'case sensitive').
#
# Examples:
#
# end_other("Hiabc", "abc") -> True
# end_other("AbC", "HiaBc") -> True
# end_other("abc", "abXabc") -> True

print("PROBLEM 3");

# simple way using endswith() method
# def end_other(str1, str2):
#     str1 = str1.lower();
#     str2 = str2.lower();
#
#     return str1.endswith(str2) or str2.endswith(str1);

# algorithmic way
def end_other(str1, str2):
    str1 = str1.lower();
    str2 = str2.lower();

    return str1[-len(str2):] == str2 or str2[-len(str1):] == str1;

print(end_other("abc", "Hiabc"));
print(end_other("AbC", "HiaBc"));
print(end_other("abc", "abXabc"));
print(end_other("ab", "abXabc"));

print("#################");

#################
## Problem - 4 ##
#################
#
# Given a string, return a string where for every character in the original,
# there are two characters.
#
# double_char("The") -> "TThhee"
# double_char("AAbb") -> "AAAAbbbb"
# double_char("Hi-There") -> "HHii--TThheerree"

print("PROBLEM 4");

def double_char(mystring):
    double_str = "";
    for char in mystring:
        double_str += char * 2;
    return double_str;

print(double_char("The"));
print(double_char("AAbb"));
print(double_char("Hi-There"));

print("#################");

#################
## Problem - 5 ##
#################
#
# Given 3 int values, a b c, return their sum. However, if any of the value is a
# teen - in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teen. Write a separate helper "def fix_teen(n)" that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) -> 6
# no_teen_sum(2, 13, 1) -> 3
# no_teen_sum(2, 1, 14) -> 3

print("PROBLEM 5");

def fix_teen(n):
    if n in [13, 14, 17, 18, 19]:
        return 0;
    else:
        return n;

def no_teen_sum(n1, n2, n3):
    return fix_teen(n1) + fix_teen(n2) + fix_teen(n3);

print(no_teen_sum(1, 2, 3));
print(no_teen_sum(2, 13, 1));
print(no_teen_sum(2, 1, 14));
print("#################");

#################
## Problem - 6 ##
#################
#
# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) -> 3
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0

print("PROBLEM 6");

def count_evens(num_list):
    even_nums = filter(lambda n: n % 2 == 0, num_list);
    return len(list(even_nums));

print(count_evens([2, 1, 2, 3, 4]));
print(count_evens([2, 2, 0]));
print(count_evens([1, 3, 5]));