"""
FizzBuzz Validator
Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.

In a valid FizzBuzz sequence:

Multiples of 3 are replaced with "Fizz".
Multiples of 5 are replaced with "Buzz".
Multiples of both 3 and 5 are replaced with "FizzBuzz".
All other numbers remain as integers.
Tests:
Waiting:1. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"]) should return True.
Waiting:2. is_fizz_buzz([13, 14, "FizzBuzz", 16, 17]) should return True.
Waiting:3. is_fizz_buzz([1, 2, "Fizz", 4, 5]) should return False.
Waiting:4. is_fizz_buzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]) should return True.
Waiting:5. is_fizz_buzz([1, 2, "Fizz", "Buzz", 5]) should return False.
Waiting:6. is_fizz_buzz([97, 98, "Buzz", "Fizz", 101, "Fizz", 103]) should return False.
Waiting:7. is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"]) should return True.
"""


def is_fizz_buzz(arr):
    expected_arr = 0
    for index, elem in enumerate(arr):
        if isinstance(elem, int) and expected_arr == 0:
            expected_arr = 1
            exp = expected(index, elem, len(arr))
    for index, i in enumerate(exp):
        if i % 3 == 0 and i % 5 == 0:
            exp[index] = "FizzBuzz"
        elif i % 3 == 0:
            exp[index] = "Fizz"
        elif i % 5 == 0:
            exp[index] = "Buzz"
    return arr == exp


def expected(index, elem, size):
    arr = [None for i in range(size)]
    arr[index] = elem
    if index == 0:
        arr = [i for i in range(elem, elem + size)]
        return arr
    else:
        arr = []
        pre = [i for i in range(elem - index, elem)]
        post = [i for i in range(elem, elem + size - index)]
        pre.extend(post)
        arr.extend(pre)

        return arr

print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"]))
print(is_fizz_buzz([13, 14, "FizzBuzz", 16, 17]))
print(is_fizz_buzz([1, 2, "Fizz", 4, 5]))
print(is_fizz_buzz([13, 14, "FizzBuzz", 16, 17]))
print(is_fizz_buzz([1, 2, "Fizz", "Buzz", 5]))
print(is_fizz_buzz([97, 98, "Buzz", "Fizz", 101, "Fizz", 103]))
print(is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"]))