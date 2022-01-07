# When using a recursive approach, we need a base case.
# the base case is whether or not we've encountered the end of the linked list.

def len_recursive(self, Node):
    if Node is None:
        return 0
    return 1 + self.len_recursive(Node.next)