# lists

my_list = [1, 2, 3];
print(my_list);

my_list = ["string", 1, 2, 3.4, [5, 6, 7]];
print(my_list);

print(len(my_list));

# Indexing and Slicing is just like strings (see strings.py)
# Unlike strings, lists are mutable. i.e. 
my_list[0] = 'list';
print(my_list);

## Methods

my_list.append("new item");     # appends new object to the end of the list
print(my_list);
another_list = [8, 9, 10];
my_list.append(another_list);   # another_list will be added to my_list as an item
print(my_list);
my_list.extend(another_list);   # another_list's items will be added to my_list as individual items
print(my_list);
item = my_list.pop();   # removes the last item by default
print(item);
print(my_list);
item = my_list.pop(2);  # removes the item by index that is passed on to the pop() function
print(item);
print(my_list);
my_list.reverse();  # reverse the list
print(my_list);
my_list = [3, 6, 8, 2, 0, 4];   
my_list.sort();     # sorts the list in ascending (not available if list contains different types)
print(my_list);

## Nested Lists

my_list = [1, 2, ['x', 'y', 'z']];
print(my_list[2]);      # returns ['x', 'y', 'z']
print(my_list[2][1]);   # returns y

## List Comprehension 

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
first_col = [row[0] for row in matrix];
print(first_col);   # prints [1, 4, 7]
