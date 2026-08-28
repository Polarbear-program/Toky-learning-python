class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

a_Node = Node('A')
b_Node = Node('B')
c_Node = Node('C')
d_Node = Node('D')
e_Node = Node('E')
f_Node = Node('F')
g_Node = Node('G')

a_Node.left = b_Node
a_Node.right = c_Node

b_Node.left = d_Node
b_Node.right = e_Node

c_Node.left = f_Node
c_Node.right = g_Node