from binarytree import BinaryTree
from tree_insert_left import insert_left
from tree_insert_right import insert_right

a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')

c_node = a_node.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child

print(a_node.value)
print(b_node.value)
print(c_node.value)
print(d_node.value)
print(e_node.value)
print(f_node.value)
