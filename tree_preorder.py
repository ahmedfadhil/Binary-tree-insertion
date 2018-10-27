from binarytree import BinaryTree


def pre_order(self):
    print(self.value)

    if self.left_child:
        self.left_child.pre_order()
    if self.right_child:
        self.right_child.pre_order()


def in_order(self):
    if self.left_child:
        self.left_child.in_order()
    print(self.value)

    if self.right_child:
        self.right_child.in_order()


def post_order(self):
    if self.left_child:
        self.left_child.post_order()

    if self.right_child:
        self.right_child.post_order()

    print(self.value)
