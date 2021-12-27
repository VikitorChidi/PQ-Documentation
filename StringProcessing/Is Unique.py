# Your task is to implement an algorithm to determine if a string has all unique characters.
# def is_unique(input_str):
#     a = len(set(input_str))
#     b = len(input_str)
#     return a == b

# input_str = ('abCedFFghI')
# print(is_unique(input_str))

#           OR

def is_unique(input_str):
    d = dict()
    for i in input_str:
        if i in d:
            return False
        else:
            d[i] = 1
    return True


input_str = ('abCedFFghI')
print(is_unique(input_str))
