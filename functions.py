def mylist_items(lst):
    result = 1
    for items in lst:
        result =result* items
    return result

list1 = [2, 3, 6]
result = mylist_items(list1)
print("Result =", result)
#------------------------------------------------------------------------------------------------------------------------------
def sort_list_by_element(tuple_list):
    return sorted(tuple_list, key=lambda x: x[-1])
shayma_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
dd = sort_list_by_element(shayma_list)
print("Sorted result:", dd)