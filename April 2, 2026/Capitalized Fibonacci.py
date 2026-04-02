"""
Capitalized Fibonacci
Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

The first character is at index 0.
If the index of non-letter characters is a Fibonacci number, leave it unchanged.


Tests:
Passed:1. capitalize_fibonacci("hello world") should return "HELLo woRld".
Passed:2. capitalize_fibonacci("HELLO WORLD") should return "HELLo woRld".
Passed:3. capitalize_fibonacci("hello, world!") should return "HELLo, wOrld!".
Passed:4. capitalize_fibonacci("The quick brown fox jumped over the lazy dog.") should return "THE qUicK broWn fox jUmped over thE lazy dog.".
Passed:5. capitalize_fibonacci("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar ex nibh, vel ullamcorper ligula egestas quis. Integer tincidunt fringilla accumsan. Integer et metus placerat, gravida felis at, pellentesque nisl.") should return "LOREm ipSum dOlor sit amet, consecTetur adipiscing elit. proin pulvinar ex nibh, vel ullaMcorper ligula egestas quis. integer tincidunt fringillA accumsan. integer et metus placerat, gravida felis at, pellentesque nisl.".
"""

def capitalize_fibonacci(s):
    fibbo = fibonacci(len(s))
    text = ""
    for index, val in enumerate(s):
        if index in fibbo:
            text += val.upper()
        else: text += val.lower()
    return text

def fibonacci(length):
    a = [0,1]
    for i in range(length-2):
        last_elem = a[-2] + a[-1]
        a.append(last_elem)
        if last_elem > length:
            return a
    return a


print(capitalize_fibonacci("hello world"))
print(capitalize_fibonacci("HELLO WORLD"))
print(capitalize_fibonacci("hello, world!"))
print(capitalize_fibonacci("The quick brown fox jumped over the lazy dog."))
print(capitalize_fibonacci("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar ex nibh, vel ullamcorper ligula egestas quis. Integer tincidunt fringilla accumsan. Integer et metus placerat, gravida felis at, pellentesque nisl."))