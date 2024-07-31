class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1  # Size of the subtree rooted at this node

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_size(self, node):
        return node.size if node else 0

    def update_node(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
            node.size = 1 + self.get_size(node.left) + self.get_size(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_node(y)
        self.update_node(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_node(x)
        self.update_node(y)
        return y

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)
    

# --------------------------- Insert ( key )-----------------------------------------
    def insert(self, key):      # Insert ( key )
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return TreeNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        self.update_node(node)

        balance = self.get_balance(node)

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

#----------------------------------- Find ( key ) ------------------------------------------

    def find(self, key):   
        return self._find(self.root, key)

    def _find(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

#--------------------------- remove ( key ) ------------------------------------------------
    def remove(self, key):    
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if not node:
            return node
        
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._get_min(node.right)
            node.key = temp.key
            node.right = self._remove(node.right, temp.key)

        self.update_node(node)

        balance = self.get_balance(node)

        # left left Case
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)

        # left right Case
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # right right Case
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)

        # right left Case
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node
    
#-------------------------------- order_of_key ( key ) ----------------------------------------------------

    def order_of_key(self, key):
        return self._order_of_key(self.root, key)

    def _order_of_key(self, node, key):
        if not node:
            return 0
        if key <= node.key:
            return self._order_of_key(node.left, key)
        else:
            return 1 + self.get_size(node.left) + self._order_of_key(node.right, key)

#-------------------------------------------- get_by_order ( key ) ----------------------------------
    def get_by_order(self, k):
        return self._get_by_order(self.root, k)

    def _get_by_order(self, node, k):
        if not node:
            return None
        left_size = self.get_size(node.left)
        if k < left_size:
            return self._get_by_order(node.left, k)
        elif k > left_size:
            return self._get_by_order(node.right, k - left_size - 1)
        else:
            return node.key

#------------------------------------------ Implementation

avl_tree = AVLTree()

# eg 1: Insert keys into the AVL Tree
keys_to_insert = [10, 20, 30, 40, 50, 25]
for key in keys_to_insert:
    avl_tree.insert(key)

# eg 2: Find keys in the AVL Tree
print("Finding keys:")
print(avl_tree.find(10))  # True
print(avl_tree.find(15))  # False

# eg 3: Remove a key from the AVL Tree
print("\nRemoving key 20:")
avl_tree.remove(20)
print(avl_tree.find(20))  # False

# eg 4: Get the order of a key
print("\nOrder of key 25:")
print(avl_tree.order_of_key(25))  #  return the number of keys smaller than 25

# 5: Get the k-th smallest element
print("\nGetting the 2nd smallest element:")
print(avl_tree.get_by_order(1))  #  return the 2nd smallest key in the tree

# eg 6: Inserting more keys and checking the order
print("\nInserting more keys and checking order:")
avl_tree.insert(5)
avl_tree.insert(15)
print(avl_tree.order_of_key(15))  #  return the number of keys smaller than 15

# eg 7: Checking the k-th smallest element again
print("\nGetting the 4th smallest element:")
print(avl_tree.get_by_order(3))  #  return the 4th smallest key in the tree
