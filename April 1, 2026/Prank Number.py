"""
Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't follow the pattern fixed.

The pattern will be one of:

The numbers increase from one to the next by a fixed amount (addition).
The numbers decrease from one to the next by a fixed amount (subtraction).
For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].
"""


def fix_prank_number(arr):
    fixed = arr[0]
    diff = [arr[index + 1] - arr[index] for index in range(len(arr) - 1)]
    print(diff)

    common_diff = max(set(diff), key=diff.count)
    print(common_diff)
    fixed = [arr[0] + i * common_diff for i in range(len(arr))]

    if fixed[0] != arr[0]:
        fixed = [arr[1] - common_diff + i * common_diff for i in range(len(arr))]

    return fixed


print(fix_prank_number([2, 4, 7, 8, 10]))  # [2, 4, 6, 8, 10]
print(fix_prank_number([400, 425, 400, 375, 350, 325, 300]))  # [450, 425, 400, 375, 350, 325, 300]
print(fix_prank_number([-5, 5, 10, 15, 20]))  # [0, 5, 10, 15, 20]
print(fix_prank_number([2, 4, 7, 8, 10]))
print(fix_prank_number([10, 10, 8, 7, 6]))
print(fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96]))
print(fix_prank_number([4, 1, -2, -5, -8, -5]))
print(fix_prank_number([0, 100, 200, 300, 150, 500]))
print(fix_prank_number([400, 425, 400, 375, 350, 325, 300]))
print(fix_prank_number([-5, 5, 10, 15, 20]))