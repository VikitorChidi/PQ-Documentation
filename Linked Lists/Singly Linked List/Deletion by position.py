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

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if prev_node:
            print('Previous node does not exist.')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node_at_pos(self, pos):
        if self.head:  # if self.head is None.
            cur_node = self.head  # cur_node is initialized to head node.
            if pos == 0:  # If pos == 0, update the head node to the next node of cur_node
                self.head = cur_node.next
                cur_node = None
                return
             # deleting a position other than the head.
            prev_node = None
            count = 0
            while cur_node and count != 0:  # The while loop will terminate if cur_node become None or count-
                # becomes equal to pos which will imply that cur_node will be the node that we want to delete.
                prev_node = cur_node
                cur_node = cur_node.next
                count += 1
            if cur_node is None:
                return
            
            prev_node.next = cur_node.next # link of the cur.node that was in between removed.
            cur_node = None


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')

llist.print_list()
