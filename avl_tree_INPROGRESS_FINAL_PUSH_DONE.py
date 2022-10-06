class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AvlTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        if self.root is None:
            self.root = Node(value)
            print("Root value set", self.root.value)
        else:
            self.root = self.insert_node(value, self.root)

    def insert_node(self, node_value: int, current_node):
        # Insert LEFT side
        if current_node.value >= node_value:
            if current_node.left is None:
                current_node.left = Node(node_value)

                current_node.height = max(self.get_height(current_node.left), self.get_height(current_node.right)) + 1
                print("Insert left", current_node.left.value, current_node.height, current_node.left.height)
                return current_node
            else:
                current_node.left = self.insert_node(node_value, current_node.left)

        # Insert RIGHT side
        if current_node.value < node_value:
            if current_node.right is None:
                current_node.right = Node(node_value)

                current_node.height = max(self.get_height(current_node.left), self.get_height(current_node.right)) + 1
                print("Insert right", current_node.right.value , current_node.height, current_node.right.height)
                return current_node
            else:
                current_node.right = self.insert_node(node_value, current_node.right)

        # Change the height for current node
        current_node.height = max(self.get_height(current_node.left), self.get_height(current_node.right)) + 1

        # Check for imbalance: if true -> rotate
        current_node = self.check_height_imbalance(current_node, node_value)

        print(current_node.value, "HEIGHT -", current_node.height, "Current value")
        return current_node

    def check_height_imbalance(self, node, node_value):
        # Check for imbalance in LEFT case
        print("Balance", self.get_height(node.right) - self.get_height(node.left), "for node", node.value)
        if (self.get_height(node.right) - self.get_height(node.left)) < -1:
            if node.left.value < node_value:
                # LR
                print("Left-Right case->LR turn", node.left.value)
                node = self.left_right_turn(node)
            else:
                # R
                print("Left case->R turn", node.left.value)
                node = self.right_turn(node)
                # print("Left case->R turn", node.left.value)

        # Check for imbalance in RIGHT case
        elif (self.get_height(node.right) - self.get_height(node.left)) > 1:
            if node.right.value >= node_value:
                # RL
                print("Right-Left case->RL turn", node.right.value)
                node = self.right_left_turn(node)
                # print("Right-Left case->RL turn", node.right.value)
            else:
                # L
                print("Right case->L turn", node.right.value)
                node = self.left_turn(node)
                # print("Right case->L turn", node.right.value)
        return node

    def right_turn(self, node):
        temp = node
        node = node.left
        temp_right_for_turning_child = node.right
        node.right = temp
        temp.left = temp_right_for_turning_child

        # Heights
        node.right.height = max(self.get_height(node.right.right), self.get_height(node.right.left)) + 1
        print(node.right.value, "node.right", node.right.height)
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        print(node.value, "node", node.height)
        return node

    def left_turn(self, node):
        temp = node
        node = node.right
        temp_left_for_turning_child = node.left
        node.left = temp
        temp.right = temp_left_for_turning_child

        # Heights
        node.left.height = max(self.get_height(node.left.right), self.get_height(node.left.left)) + 1
        print(node.left.height, "node.left", node.left.value)
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        print(node.height, "node", node.value)
        return node

    def left_right_turn(self, node):
        node.left = self.left_turn(node.left)
        node = self.right_turn(node)
        return node

    def right_left_turn(self, node):
        node.right = self.right_turn(node.right)
        node = self.left_turn(node)
        return node

    def get_height(self, node: Node):
        if node is None:
            return 0
        return node.height

    def print_the_avl_tree(self, node):
        if node is None:
            return
        print(node.value)
        self.print_the_avl_tree(node.left)
        self.print_the_avl_tree(node.right)


if __name__ == '__main__':
    tree = AvlTree()
    tree.insert(7)
    tree.insert(9)
    tree.insert(8)
    tree.insert(4)
    tree.insert(2)
    tree.insert(1)

    # tree.insert(6)
    # tree.insert(19)
    # tree.insert(21)
    # tree.insert(25)
    # tree.insert(27)
    # tree.insert(9)
    # tree.insert(99)
    tree.print_the_avl_tree(tree.root)
    print("Tree root----", tree.root.value, "height", tree.root.height)
    print("Tree root----", tree.root.left.value, tree.root.left.height)
    print("Tree root----", tree.root.right.value, tree.root.right.height)
