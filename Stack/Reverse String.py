# Reversing a string using a stack

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return self.items == []

# Brute force approach
# input_str = "Educative"
# print(input_str[::-1])


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""

    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


if __name__ == '__main__':
    stack = Stack()
    input_str = "!evitacudE"
    print(reverse_string(stack, input_str))
