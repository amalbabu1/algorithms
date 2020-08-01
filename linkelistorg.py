class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def appendf(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def printLL(self):
        c_node = self.head
        while c_node:
            print(c_node.data, " ")
            c_node = c_node.next


ll = LinkedList()
ll.appendf("a")
ll.appendf("b")
ll.printLL()

