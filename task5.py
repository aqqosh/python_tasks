def recursive(list1, list2, result):
    a = list1[0]
    b = list2[0]
    
    if len(list1) == 1:
        return [min([a, b]), max([a, b])]
    
    result = [min([a, b]), max([a, b])]
    return result + recursive(list1[1:], list2[1:], result)

list1 = [1, 2, 4, 7, 9, 10]
list2 = [1, 3, 4, 5, 8]

result = []
result = recursive(list1, list2, result)
result