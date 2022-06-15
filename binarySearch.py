#it is best to use when list are sorted
# def binary_search(list, target):
#     first = list[0]
#     last = len(list) - 1
   

#     while first <= last:
#         midpoint = (first + last) // 2
#         if list[midpoint] == target:
#             return midpoint
#         elif list[midpoint] < target:
#             first = midpoint + 1
#         else:
#             last = midpoint - 1
#     return None

# def verify(index):
#     if index is not None:
#         print("target founnd at index :", index)
#     else:
#         print("Target not found in list")


# numbers = [1,2,3,4,5,6,7,8,9,10]   
# result = binary_search(numbers,9)
# verify(result)
 


def binary_search(list, target):
    first = list[0]
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint

        elif target > list[midpoint]:
            first = list[midpoint] + 1
        else:
            last = list[midpoint] - 1
    return None


def verify(index):
    try:
        if index is not None:
            print ("this is the index", index)
    except:
        print("target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]   
result = binary_search(numbers,9)
verify(result)