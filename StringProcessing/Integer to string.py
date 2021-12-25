# Note that you cannot make use of the built-in str function:

def int_to_str(input_int):

    if input_int < 0:
        is_negative = True
        input_int *= -1
    else:
        is_negative = False

        # If input_int is less than 0, is_negative is set to True and is also converted to a positive integer by multiplication with -1.
        #  On the other hand, if input_int is a positive integer, is_negative is set to False.

# Once the sign of input_int is determined, the execution jumps to the next:
    output_str = []

    if input_int == 0:
        output_str.append('0')
    else:
        while input_int > 0:
            output_str.append(chr(ord('0') + input_int % 10))
            input_int //= 10
        output_str = output_str[::-1]

        # output_str is initialized to an empty list.
        #  If input_int is 0, the result is straightforward, i.e., ‘0’.
        #  But if the number is greater than 0, then the while loop is where the actual action happens.
        #  The last digit of input_int is extracted using the % operator.
        # For example:
        #  12 % 10 = 2
        # 17 % 10 = 7
        # 10 % 10 = 0

        # You notice that by taking the modulus of a number with 10, we always get the last digit of that number.
        # The last digit is converted into a character by chr() and ord() functions. So ord('0') + input_int % 10 gives the Unicode code point of the character that we want which when passed to chr() function returns a character..
        # That character is appended to output_str in the same line. As we have already dealt with the last digit, we remove it from input_int using the // operator.
        # The while loop repeats the code until input_int becomes less than or equal to 0.
        # on line23 output_str reverses the positions of its elements so that the last digit is on the last index of output_str instead of being on the first one.
        #  That brings us to the code on below.

    output_str = ''.join(output_str)

    if is_negative:
        return '-' + output_str
    else:
        return output_str


input_int = 123
print(input_int)
print(type(input_int))

output_str = int_to_str(input_int)
print(output_str)
print(type(output_str))
