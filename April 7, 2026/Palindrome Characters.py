"""
Palindrome Characters
Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

A palindrome is a string that is the same forward and backward.
If it's not a palindrome, return "none".
Tests:
Passed:1. palindrome_locator("racecar") should return "e".
Passed:2. palindrome_locator("level") should return "v".
Passed:3. palindrome_locator("freecodecamp") should return "none".
Passed:4. palindrome_locator("noon") should return "oo".
Passed:5. palindrome_locator("11100111") should return "00".
"""

def palindrome_locator(s):
    len_str =len(s)
    mid=len_str//2
    if s==s[::-1]:return s[mid-1:mid+1] if len_str%2==0 else s[mid]
    else: return "none"
    return s

print(palindrome_locator("racecar"))
print(palindrome_locator("level"))
print(palindrome_locator("freecodecamp"))
print(palindrome_locator("noon"))
print(palindrome_locator("11100111"))