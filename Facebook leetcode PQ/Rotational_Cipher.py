import math


def rotationalCipher(input, rotation_factor):
    # Write your code here
    output = ""
    for i in input:
        if i.isnumeric():
            output += str((int(i) + rotation_factor) % 10) # output = output + str((int(i) + rotation_factor) % 10)
        elif i.isupper():
            new_output = (ord(i) - ord('A') + rotation_factor) % 26
            output += chr(ord('A') + new_output) # output = output + chr(ord('A') + new_output)
        elif i.islower():
            new_output = (ord(i) - ord('a') + rotation_factor) % 26
            output += chr(ord('a') + new_output)
        else:
            output += i   # for special characters.
    return output
