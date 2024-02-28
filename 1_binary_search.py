#Бинарный поиск

def binary_search(list, item, count):
    low = 0
    high = len(list)-1 
    while low <= high :
        count += 1
        mid_index = (low + high) // 2
        guess = list[mid_index]
        if guess == item :
            return mid_index, count
        if guess > item:
            high = mid_index - 1
        else:
            low = mid_index + 1
    return None, count

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
my_list = list(range(1, 101))

print(binary_search(my_list, 68, 0))
print(binary_search(my_list, 33, 0))
print('Hi Git')
