def palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

text = input("Enter a string: ")
print(palindrome(text))