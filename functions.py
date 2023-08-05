def mylist_items(lst):
    result = 1
    for items in lst:
        result =result* items
    return result

list1 = [2, 3, 6]
result = mylist_items(list1)
print("Result =", result)
#------------------------------------------------------------------------------------------------------------------------------Q1
def sort_list_by_element(tuple_list):
    return sorted(tuple_list, key=lambda x: x[-1])
shayma_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
dd = sort_list_by_element(shayma_list)
print("Sorted result:", dd)
#------------------------------------------------------------------------------------------------------------------------------Q2
def combine_dictionaries(d1, d2):
    combined_dict = {}

    for key in d1:
        combined_dict[key] = d1[key]

    for key in d2:
        if key in combined_dict:
            combined_dict[key] += d2[key]
        else:
            combined_dict[key] = d2[key]

    return combined_dict

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

r = combine_dictionaries(d1, d2)
print("Expected result:", r)
#----------------------------------------------------------------------------------------------------------------------------Q3
def generate_squared_dict(n):
    squared_dict = {i: i*i for i in range(1, n+1)}
    return squared_dict

# Get the input from the user
n = int(input("Enter an integral number: "))

t = generate_squared_dict(n)
print(t)
#-----------------------------------------------------------------------------------------------------------------------------Q4
def sort_tuple_by_float(lst):
    return sorted(lst, key=lambda x: float(x[1]), reverse=True)

input_list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
l = sort_tuple_by_float(input_list)
print("Expected result:", l)
#------------------------------------------------------------------------------------------------------------------------------Q5
example_set = {0, 1, 2, 3, 4}
print("Example set:", example_set)
for item in example_set:
    print(item)
#------------------------------------------------------------------------------------------------------------------------------
my_set = set()
my_set.add(10)
my_set.add(20)
my_set.add(30)
print("Set after adding members:", my_set)
my_set.remove(20)
print("Set after removing 20:", my_set)
my_set.discard(40)
print("Set after discarding 40:", my_set)
#----------------------------------------------------------------------------------------------------------------------------
