# A palindrome is a word, number, phrase, or any other sequence of characters that reads the same forward as it does backward.
# Example: Was it a cat I saw


def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False 
        # repeat the process until the list is exhausted.
        i += 1 
        j -= 1
    return True

s = "Was it a cat I saw?"
# s = "Victor"
print(is_palindrome(s))