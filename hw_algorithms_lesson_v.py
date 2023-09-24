#1
def selection_sort_descending(arr: list):
    n = len(arr)
    for i in range(n - 1):
        max_index = i

        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        arr[i], arr[max_index] = arr[max_index], arr[i]


my_list = [64, 24, 12, 22, 10]
selection_sort_descending(my_list)
print("selection array in descending order:")
print(my_list)


#2
def bubble_sort_descending(arr: list):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


my_list = [60, 24, 12, 22, 10]
bubble_sort_descending(my_list)
print("bubble array in descending order:")
print(my_list)


#3
def insertion_sort_descending(arr: list):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


my_list = [65, 24, 12, 22, 11]
insertion_sort_descending(my_list)
print("insertion array in descending order:")
print(my_list)
