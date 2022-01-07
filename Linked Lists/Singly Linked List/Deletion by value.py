# The constructor is a method that is called when an object is created.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# points to the first node in the linked list


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print('Empty linked list')
            return

        cur_node = self.head
        llstr = ''

        while cur_node:
            llstr += str(cur_node.data) + '-->'
            cur_node = cur_node.next
        print(llstr)

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = last_node

    def delete_node(self, key):
        cur_node = self.head  # keep track of the head

        if cur_node and cur_node.data == key:  # check if cur_node is None & its value == key
            # update the head with the next node of the previous head.
            self.head = cur_node.next
            cur_node = None  # current node will be deleted as its set to None
            return

        prev_node = None  # keep track of the previous node
        while cur_node and cur_node.data != key:  # while cur_node isn't None and and key doesn't match, loop continues
            prev_node = cur_node  # keep track of the pre_node
            cur_node = cur_node.next  # while current node is updated

        if cur_node is None:
            return

        prev_node.next = cur_node.next # link of the cur.node that was in between removed.
        cur_node = None


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.delete_node('A')

llist.print_list()
