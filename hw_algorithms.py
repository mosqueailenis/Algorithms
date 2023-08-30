# Level 1


def foo_bar(n: int):
    for i in range(1, 101):
        # Check if the number is divisible by both 3 and 7 and print 'FooBar'
        if i % 3 == 0 and i % 7 == 0:
            print("BinGo")
        # Check if the number is divisible by 3 and print 'Foo'
        elif i % 3 == 0:
            print("Bin")
        # Check if the number is divisible by 7 and print 'Bar'
        elif i % 7 == 0:
            print("Go")
        # If none of the above conditions are met, just print the number
        else:
            print(i)

# Call the function with the desired range (1 to 100 in this case)
foo_bar(50)


def sum_numbers(n: int):
    # Initialize the variable 'final_sum' and set it to 0 initially
    final_sum = 0

    # Use a loop to iterate over numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Convert the number to a string to iterate through its digits
        num_str = str(i)

        # Iterate through each digit in the string representation of the number
        for digit in num_str:
            # Convert the digit back to an integer and add it to 'final_sum'
            final_sum += int(digit)

    # Return the 'final_sum' as the result
    return final_sum


# Call the function with the desired value of n
n = 5
result = sum_numbers(n)
print("Result:", result)

 # level 2
 # 1 Find Max number

def find_max(a: int, b: int, c: int):
    # Compare 'a' with 'b' and 'c'
    if a > b and a > c:
        return a
    # Compare 'b' with 'a' and 'c'
    elif b > a and b > c:
        return b
    # If neither of the above conditions is met, 'c' is the largest
    else:
        return c


num1 = 127
num2 = 21
num3 = 32

# Call the function with the example values
max_num = find_max(num1, num2, num3)
print("Maximum number:", max_num)


# 2 Leap Year

def leap_year(year: int):
    # Check if the year is evenly divisible by 4
    if year % 4 == 0:
        # If it's a century year, check if it's divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        # If not a century year, it's a leap year
        else:
            return True
    # If not divisible by 4, it's not a leap year
    else:
        return False

# Test cases
years = [2000, 2020, 2024, 1900, 2100, 2022]
for year in years:
    if leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")



# Level 3
# Fibonacci

def generate_fibonacci_sequence(n: int):
    # Initialize the list with the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Use a for loop to generate the remaining Fibonacci numbers after the first two
    for i in range(2, n):
        new_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(new_number)
    # Calculate the next Fibonacci number using the formula fib_sequence[-1] + fib_sequence[-2]

    # Append the new Fibonacci number to the list using the append() function

    return fib_sequence
print(generate_fibonacci_sequence(10))

