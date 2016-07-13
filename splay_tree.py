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
        if t2 is not None:
            t2.parent_ = self
        x.parent_ = self.parent_
        x.right_ = self
        self.parent_ = x
        self.left_ = t2
        # update the height
        self.update_height()
        x.update_height()
        return x

    # rotate left
    def rotate_left(self):
        y = self.right_
        t2 = y.left_
        # perform the rotation
        if t2 is not None:
            t2.parent_ = self
        y.parent_ = self.parent_
        y.left_ = self
        self.right_ = t2
        self.parent_ = y
        # update height
        self.update_height()
        y.update_height()
        return x

class Splay_Tree():
    def __init__(self):
        self.root_ = None
        self.size_ = 0
    
    def in_order_helper(self, node, ret_list = None):
        if ret_list is None:
            ret_list = []
        if node.left_ :
            ret_list = self.in_order_helper(node.left_, ret_list)
        ret_list += [node.key_]
        if node.right_:
            ret_list = self.in_order_helper(node.right_, ret_list)
        return ret_list

    def in_order(self):
        if self.root_ is None:
            return []
        return self.in_order_helper(self.root_)

    def find(self, key):
        self.root_ = self.splay(self.root_, key)
        if self.root_ is not None and self.root_.key_ == key:
            return True
        return False
    
    # 1. find whether key is already in the tree
    # 2. True, return the node of the key
    #    False, new a node and insert into the tree
    def insert(self, key):
        self.root_ = self.splay(self.root_, key)
        if self.root_ is not None and self.root_.key_ == key:
            return self.root_, False
        new_node = Node(key)
        new_node.key_ = key
        self.size_ += 1
        if self.root_ is not None:
            # the tmp root_ should be left
            if self.root_.key_ < key:
                new_node.left_ = self.root_
                new_node.right_ = self.root_.right_
                if self.root_.right_ is not None:
                    self.root_.right_.parent_ = new_node
                self.root_.parent_ = new_node
            else:
                new_node.left_ = self.root_.left_
                new_node.right_ = self.root_
                if self.root_.left_ is not None:
                    self.root_.left_.parent_ = new_node
                self.root_.parent_ = new_node
        self.root_ = new_node
        return self.root_, True
            
    # splay the node of key to root
    # node is not in the tree, splay the closest one
    # return the splayed node
    def splay(self, root, key):
        # base case, root is the targeted node
        if root is None or root.key_ == key:
            return root
        # target is in the left sub_tree
        if key < root.key_:
            if root.left_  is None:
                return root
            # zig-zig    
            if key < root.left_.key_:
                root.left_.left_ = self.splay(root.left_.left_, key)
                root = root.right_rotate()
            # zig-zag
            elif key > root.left_.key_ and root_.left_.right_ is not None:
                root.left_.right_ = self.splay(root.left_.right_, key)
                root.left_ = root.left_.left_rotate()
            if root.left_ is not None:
                root = root.right_rotate()
        # target is in the right sub_tree, symmetric with left case
        else:
            if root.right_  is None:
                return root
            # zag-zag
            if key > root.right_.key_:
                root.right_.right_ = self.splay(root.right_.right_, key)
                root = root.left_rotate()
            # zag-zig
            elif key < root.right_.key_ and root.right_.left_ is not None:
                root.right_ = root.right_.right_rotate()
            if root.right_ is not None:
                root = root.left_rotate()
        return root

    # return the size of the tree
    def size(self):
        return self.size_;

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
    splay_map = Splay_Tree()
    for i in range(1, 100):
        splay_map.insert(i)
    print splay_map.in_order()
