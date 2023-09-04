#task 1
def find_two_lowest(arr: list):
    lowest = float('inf')
    second_lowest = float('inf')
    for num in arr:

        if num < lowest:
            second_lowest = lowest
            lowest = num
        elif num < second_lowest and num != lowest:
            second_lowest = num

    return lowest, second_lowest


arr = [310, 3, 1, 7, 11, 9, 6]
result = find_two_lowest(arr)
print(result)

#task2


def invert_list(arr: list):
    inverted = []

    for num in arr:
        inverted.append(-num)

    return inverted


input_list = [-1, 5, -2, 8]
output_list = invert_list(input_list)
print(output_list)

#task3


def max_diff(arr: list):
    if len(arr) == 0:
        return 0

    arr.sort()

    smallest = arr[0]
    largest = arr[-1]
    return largest - smallest


input_list = [3, 5, 7, 2]
output = max_diff(input_list)
print(output)


 #task4

def count_larger_neighbors(arr: list):
    count = 0

    for i in range(1, len(arr) - 1):

        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:

            count += 1

    return count


input_list = [2, 56, 7, 21, 22, 19, 26]
output = count_larger_neighbors(input_list)
print(output)

#task5


def subtract_min(arr: list):
    min_element = min(arr)

    for i in range(len(arr)):
        arr[i] -= min_element

    return arr


input_list = [9, 2, 5, 4, 7, 6, 1]
output = subtract_min(input_list)
print(output)
