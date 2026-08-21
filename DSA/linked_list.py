# This is a linked list

# One node contains of value and a pointer link to the next node
class Node:
    def __init__(self, value):

        self.value = value
        self.next = None

# A function to traverse data/value ad then print it out    
def traverse_print(head):
        currentNode = head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print("null")

# Assign value for each node created
node1 = Node("Monday")
node2 = Node("Tuesday")
node3 = Node("Wednesday")
node4 = Node("Thursday")
node5 = Node("Friday")
node6 = Node("Saturday")
node7 = Node("Sunday")

# Pointer next linking the next node contiguously
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

# function traverse and print will print out value
traverse_print(node1)