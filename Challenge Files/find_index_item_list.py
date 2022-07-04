import functools
import operator

# def compatible(x):
#     try:
#         return list(x)
#     except TypeError:
#         return [int(x) for a in str(x)]
#
# def find_index_in_list(input, value):
#     flatten = (functools.reduce(operator.add, list(map(compatible, input))))
#     number = flatten.count(value)
#     print(number)
#     count = 0
#     result = []
#     for element in input:
#         print(traverse(element, input, value, result, index_trace=[]))
#     return result
#
# def traverse(element, input, value, result, index_trace):
#     if element == value:
#         return index_trace.append(input.index(element))
#     elif type(element) is list:
#         for el in element:
#             traverse(el, element, value, index_trace, result)
#     else:
#         return

# Giving up as it is taking too long (out of timebox)

"""
GIVEN SOLUTION
"""


def index_all(search_list, item):
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif type(search_list[i]) is list:
            for index in index_all(search_list[i], item):
                indices.append([i] + index)
    return indices


# print(find_index_in_list([[[3, 4], 2], 2, [3, 2]], 2))
print(index_all([[[3, 4], 2], 2, [2, 3, 2]], 2))

### REFLECTION
## Along the right lines, try next time to just do it in one function,
# don't expect it to be split up,
