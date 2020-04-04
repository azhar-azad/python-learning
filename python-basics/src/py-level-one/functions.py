def my_func(param1 = "default"):
    """
    This is a DOCSTRING
    :param param1:
    :return:
    """
    print("A python function with param value {}".format(param1));

my_func();
my_func("parameter_value");


def hello():
    return "hello";

print(hello());


def add1(value1, value2):
    return value1 + value2;

print(add1(2, 3));           # 5
print(add1("2", "3"));       # 23
print(type(add1(2, 3)));     # <class 'int'>
print(type(add1("2", "3"))); # <class 'str'>

def add2(value1, value2):
    if type(value1) == type(value2) == type(0):
        return value1 + value2;
    else:
        return "Sorry, this function needs Integers";

print(add2(2, 3));      # 5
print(add2("2", "3"));  # Sorry, this function needs Integers


## Lambda Expression

my_list = [1, 2, 3, 4, 5, 6, 7, 8];

### normal version
def even_bool(num):
    return num % 2 == 0;

even_nums = filter(even_bool, my_list);
print(list(even_nums)); # [2, 4, 6, 8]

### Lambda version
even_nums = filter(lambda num: num % 2 == 0, my_list);
print(list(even_nums)); # [2, 4, 6, 8]


## split() method on string

str = "Go Barca!! #morethanaclub";
result = str.split("#");
print(result);          # ['Go Barca!! ', 'morethanaclub']
result = str.split("#")[1];
print(result);          # morethanaclub


## in operator
print('x' in [1, 2, 3]); # False
print('x' in [1, 2, 3, 'x']); # True