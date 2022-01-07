# A balanced sets of brackets is one where the number and type of opening & closing brackets match-
# and that is also properly nested within the string of brackets.

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
            return self.items[-1] # returns the item at the top.

    def is_empty(self):
        return self.items == []


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    idx = 0

    while idx < len(paren_string) and is_balanced:
        paren = paren_string[idx]

        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        idx += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


if __name__ == '__main__':
    print("String : (((({})))) Balanced or not?")
    print(is_paren_balanced("(((({}))))"))
