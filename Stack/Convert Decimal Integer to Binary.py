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


def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return 0

    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num //= 2

    binary_num = ""
    while not s.is_empty():
        binary_num += str(s.pop())

    return binary_num


if __name__ == '__main__':
    print(convert_int_to_bin(100))
