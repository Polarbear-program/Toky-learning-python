class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def traverse_and_print(head):
    while head:
        print(head.value, " -> ", end=" ")
        head = head.next
    print("NULL")


def reverse_and_print(head):
    prev = None
    curr = head

    while curr:
        # Next node will create first, it is after nolde
        next_node = curr.next

        # current node will point back to the node before it
        # Previous at first will point to None
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


# Assign value for each node
node1 = Node("Monday")
node2 = Node("Tuesday")
node3 = Node("Wednesday")
node4 = Node("Thursday")
node5 = Node("Friday")
node6 = Node("Saturday")
node7 = Node("Sunday")

# Connect one node to another
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

# Before reverse node
traverse_and_print(node1)

# Reverse node order using 3-pointer method
reverse_and_print(node1)

# After reverse node order, start at node 7
traverse_and_print(node7)
