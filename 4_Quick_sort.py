# # Quick sort

# def sum(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total

# print(sum([1,2,3,4]))

# def rec(arr):
#     if not arr:
#         return 0
#     else:
#         return 1 + rec(arr[1:])
    
# #------------recursion --------------------
# def sum_arr(arr):
#     if not arr:  # Если список пустой
#         return 0
#     else:
#         return arr[0] + sum_arr(arr[1:])  # Суммируем первый элемент с суммой оставшихся элементов

# # Пример использования
# my_list = [1, 2, 3, 4, 5]
# print("Сумма элементов списка:", sum_arr(my_list))

#----------Quick sort   ---------------------------

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = list(filter(lambda x: x < pivot, array))
        # less = [i for i in array[1:] if i <= pivot]
        # center = [i for i in array[1:] if i == pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([7, 8, 1, 10, 5, 2, 3]))



