class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next


node1 = Node(12)  # our first node
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3
node3.next = None

node1.traverse()
