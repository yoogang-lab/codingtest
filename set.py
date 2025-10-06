empty_set = set()

fruits = {"apple", "banana", "cherry"}

number_of_fruits = len(fruits) #3

fruits.add("orange")

fruits.add("apple")

fruits.discard("banana") # apple, cherry, orange

removed_item = fruits.pop() # cherry, orange # removed_items = apple

list_example = [1, 2, 3, 2, 1]
set_from_list = set(list_example)

list_without_dup = list(set_from_list)

tuple_example = (1, 2, 3, 2, 1)
set_from_tuple = set(tuple_example)

string_example = "hello"
set_from_string = set(string_example)

pass