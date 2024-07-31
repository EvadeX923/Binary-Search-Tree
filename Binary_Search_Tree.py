class Binary_Search_Tree:

    class __BST_Node:

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.__root = None
        self.__height = 1

    def __get_balance(self, node):
        bal = 0
        if node is not None:
            if node.left is not None:
                bal -= node.left.height
            if node.right is not None:
                bal += node.right.height
        return bal
    
    def __rotate_left(self, node):
        new_root = node.right
        node_right = new_root.left
        new_root.left = node
        node.right = node_right
        self.__update_height(node)
        self.__update_height(new_root)
        return new_root
    
    def __rotate_right(self, node):
        new_root = node.left
        node_left = new_root.right
        new_root.right = node
        node.left = node_left
        self.__update_height(node)
        self.__update_height(new_root)
        return new_root
        
    def __balance(self, node):
        if node is None:
            return node
        
        node_height = self.__get_balance(node)
        left_balance = self.__get_balance(node.left)
        right_balance = self.__get_balance(node.right)
        
        # left-heavy
        if node_height == -2:
            if left_balance == -1 or left_balance == 0:
                print('right rotate')
                # rotate right about t and return the new root.
                return self.__rotate_right(node)
            if left_balance == 1:
                print('left-right rotate')
                # rotate left about t's left child, then rotate right about t and return the new root.
                node.left = self.__rotate_left(node.left)
                return self.__rotate_right(node)
            
        # right-heavy
        elif node_height == 2:
            if right_balance == 1 or right_balance == 0:
                print('left rotate')
                # rotate left about t and return the new root.
                return self.__rotate_left(node)
            if right_balance == -1:
                print('right-left rotate')
                # rotate right about t’s right child, then rotate left about t and return the new root.
                node.right = self.__rotate_right(node.right)
                return self.__rotate_left(node)
        return node
       
    def __update_height(self, node):
        if node is None:
            return 0
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        node.height = 1 + max(left_height, right_height)
    
    def __recursive_insert(self, value, node):
        if node is None:
            return self.__BST_Node(value)
        if value < node.value:
            node.left = self.__recursive_insert(value, node.left)
        elif value > node.value:
            node.right = self.__recursive_insert(value, node.right)
        else:
            raise ValueError
        self.__update_height(node)
        return self.__balance(node)

    def insert_element(self, value):
        self.__root = self.__recursive_insert(value, self.__root)
    
    def __recursive_remove(self, value, node):
        if node is None:
            raise ValueError

        elif value < node.value:
            node.left = self.__recursive_remove(value, node.left)
            
        elif value > node.value:
            node.right = self.__recursive_remove(value, node.right)
            
        elif node.value == value:
            # no children
            if node.left is None and node.right is None:
                return None
            # left child
            elif node.right and node.left is None:
                return node.right
            # right child
            elif node.left and node.right is None:
                return node.left
            # two children
            elif node.left and node.right:
                min_node = self.__recursive_find_min(node.right)
                node.value = min_node.value
                node.right = self.__recursive_remove(min_node.value, node.right)
                self.__update_height(node)
                
        self.__update_height(node)
        return self.__balance(node)

    def __recursive_find_min(self, node):
        if node.left is None:
            return node
        else:
            return self.__recursive_find_min(node.left)

    def remove_element(self, value):
        self.__root = self.__recursive_remove(value, self.__root)
    
    def __recursive_in_order(self, node, result):
        if node is None:
            return
        self.__recursive_in_order(node.left, result)
        result.append(node.value)
        self.__recursive_in_order(node.right, result)
        return result

    def in_order(self):
        result = self.__recursive_in_order(self.__root, [])
        if result is None:
            return '[ ]'
        else:
            return '[ ' + (", ".join(map(str, result))) + ' ]'
    
    def __recursive_pre_order(self, node, result):
        if node is None:
            return
        result.append(node.value)
        self.__recursive_pre_order(node.left, result)
        self.__recursive_pre_order(node.right, result)
        return result

    def pre_order(self):
        result = self.__recursive_pre_order(self.__root, [])
        if result is None:
            return '[ ]'
        else:
            return '[ ' + (", ".join(map(str, result))) + ' ]'
    
    def __recursive_post_order(self, node, result):
        if node is None:
            return
        self.__recursive_post_order(node.left, result)
        self.__recursive_post_order(node.right, result)
        result.append(node.value)
        return result

    def post_order(self):
        result = self.__recursive_post_order(self.__root, [])
        if result is None:
            return '[ ]'
        else:
            return '[ ' + (", ".join(map(str, result))) + ' ]'

    def to_list(self):
        return self.__recursive_in_order(self.__root, [])

    def get_height(self):
        if self.__root is None:
            return 0
        return self.__root.height

    def __str__(self):
        return self.in_order()