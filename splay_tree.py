class Node():
    def __init__(self, key):
        self.key_ = key
        self.parent_ = None
        self.left_ = None
        self.right_ = None
        self.height_ = 0
    
    def update_height(self):
        if self.left_ and self.right_:
            self.height_ = max(self.left_.height_, self.right_.height_) + 1
        elif self.left_:
            self.height_ = self.left_.height_ + 1
        elif self.right_:
            self.height_ = self.right_.height_ + 1
        else:
            self.height_ = 0
    
    def __str__(self):
        return "["+self.key_+"]"

    # rotate right
    def rotate_right(self):
        x = self.left_
        t2 = x.right_
        # perform the rotation
        t.parent_ = self
        x.parent_ = self.parent_
        x.right_ = self
        self.parent_ = x
        self.left_ = t2
        # update the height
        self.update_height()
        x.update_height()
        return x

    def rotate_left(self):
        return self

class Avl_Tree():
    def __init__(self, key):
        self.root_ = None
        self.size_ = 0
    
    def in_order(self, node, ret_list = None):
        if node is None:
            ret_list = []
        if node.left_:
            ret_list = self.in_order(node.left_, ret_list)
        ret_list += node.key_
        if node.right_:
            ret_list = self.in_order(node.right_, ret_list)
        return ret_list
    def insert(self, node):

def in_order(node, ret_list = None):
    if ret_list is None:
        ret_list = []
    if node.left_:
        ret_list = in_order(node.left_, ret_list)
    ret_list += [node.key_]
    if node.right_:
        ret_list = in_order(node.right_, ret_list)
    return ret_list

if __name__ == "__main__":
    z = Node(1)
    y = Node(2)
    x = Node(3)
    z.parent_ = y
    y.parent_ = x
    y.left_ = z
    x.left_ = y
    print str(x.key_)
    print in_order(x)
    x.rotate_right()
    print in_order(x)
    print in_order(y)
