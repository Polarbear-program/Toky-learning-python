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

# Insert new node into current linked list with position


def insertNewNode(head, newNode, position):
    currentNode = head
    # Return new Node if position given = 1
    if position == 1:
        newNode.next = currentNode
        return newNode

    # given currentNode = 2, imagine if newNode is nothing then break.
    # but if nothing happen, proceed node -> pointer ->....
    for _ in range(position - 2):
        if newNode is None:
            break
        currentNode = currentNode.next

    # And then, new Node's pointer replace currentNode's pointer.
    # CurrentNode pointer connect to new Node
    newNode.next = currentNode.next
    currentNode.next = newNode
    return currentNode

# Remove node in linked list


def removeNode(head, nodeDelete):
    currentNode = head
    if currentNode == nodeDelete:
        return currentNode.next
    
    while currentNode.next is not nodeDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return currentNode

    currentNode.next = currentNode.next.next
    return currentNode

# Node parameter is the Node datastructure created, not a value


def biggestValue(head):
    currentNode = head  # currentNode created
    bigValue = currentNode.value  # bigValue will assigned as currentNode value first
    
    while currentNode:
        if currentNode.value > bigValue:
            bigValue = currentNode.value
        currentNode = currentNode.next
    return bigValue

# Assign value for each node created
node1 = Node("Monday")
node2 = Node("Tuesday")
node3 = Node("Wednesday")
node4 = Node("Thursday")
node5 = Node("Friday")
node6 = Node("Saturday")
node7 = Node("Sunday")

node8 = Node(2)
node9 = Node(4)
node10 = Node(19)
node11 = Node(5)
node12 = Node(9)

newNode = Node(110)

# Pointer next linking the next node contiguously
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

node8.next = node9
node9.next = node10
node10.next = node11
node11.next = node12

# function traverse and print will print out value(before adding more element)
traverse_print(node1)
print("The biggest value in node 8 - node 11 is:", biggestValue(node8))

# After adding a new Node
insertNewNode(node1, newNode, 2)
traverse_print(node1)

# And then, delete the node 3 which is Wednesday Node
removeNode(node1, node3)
traverse_print(node1)
