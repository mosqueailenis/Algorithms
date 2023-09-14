

#task 1

def sum_even_and_product_odd(arr: list):
    sum_even = 0
    product_odd = 1

    for num in arr:
        if num % 2 == 0:
            sum_even += num
        else:
            product_odd *= num

        return [sum_even, product_odd]


input_list = [6, 7, 8, 9]
result = sum_even_and_product_odd(input_list)
print(result)


#task 2

def sum_between_range(arr: list, min_val: int, max_val: int):
    sum_within_range = 0

    for num in arr:
        if min_val <= num <= max_val:
            sum_within_range += num

    return sum_within_range


arr = [5, 2, 1, 4, 10, 3, 7, 6, 9, 5]
min_val = 5
max_val = 10
result = sum_between_range(arr, min_val, max_val)
print(result)


#task 3

def buy_and_sell_stock(prices: list):
    maximum = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            maximum += prices[i + 1] - prices[i]
    return maximum


prices = [7, 1, 5, 3, 6, 4]
result = buy_and_sell_stock(prices)
print(result)


#task 4

def plus_one(arr: list):
    arr[-1] += 1

    for i in reversed(range(1, len(arr))):

        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1

    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)


input_list = [1, 2, 9]
plus_one(input_list)
print(input_list)
