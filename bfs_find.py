from bst_insert import BinarySearchTree

bst = BinarySearchTree(45)

bst.insert_node(10)
bst.insert_node(8)
bst.insert_node(12)
bst.insert_node(20)
bst.insert_node(17)
bst.insert_node(25)
bst.insert_node(19)

# checking the find_node method
print(bst.find_node(45))
print(bst.find_node(10))
print(bst.find_node(8))
print(bst.find_node(12))
# and so on...





