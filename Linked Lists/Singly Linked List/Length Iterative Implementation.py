class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def Iterative_count(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count +=1
            cur_node = cur_node.next
        return count