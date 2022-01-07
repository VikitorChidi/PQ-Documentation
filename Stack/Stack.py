class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty:
            return self.items.pop()
        return IndexError('pop(): empty stack')

    def get_stack(self):
        return self.items

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return self.items == []


if __name__ == '__main__':
    myStack = Stack()
# myStack.push("A")
# myStack.push("B")
# myStack.push("C")
# myStack.push("D")
print(myStack.get_stack())
