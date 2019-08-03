class Node(object):
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def __iter__(self):
        return self.root.__iter__()

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def add_sup(self, nvalue, elem):
        if elem.value > nvalue:
            if elem.left is not None:
                self.add_sup(nvalue, elem.left)
            else:
                elem.left = Node(nvalue)
        else:
            if elem.right is not None:
                self.add_sup(nvalue, elem.right)
            else:
                elem.right = Node(nvalue)

    def add(self, nvalue):
        if self.root is None:
            self.root = Node(nvalue)
        else:
            self.add_sup(nvalue, self.root)

    def find(self, elem):
        current = self.root
        while current is not None:
            if current.value == elem:
                return True
            if current.value > elem:
                current = current.left
            else:
                current = current.right
        return False

    def print_tree(self):
        if self.root is None:
            print("the tree is empty")
        else:
            self.print_tree_supp(self.root)

    def print_tree_supp(self, elem):
        if elem is not None:
            self.print_tree_supp(elem.left)
            print(str(elem.value) + ' ')
            self.print_tree_supp(elem.right)

    def delete(self, goal):
        flag = 0
        if self.root is None:
            print("The tree is empty")
        else:
            if self.root.value == goal:
                if self.root.left is None and self.root.right is None:
                    self.root = None
                    return
                elif self.root.left is not None and self.root.right is None:
                    self.root = self.root.left
                    return
            parent = None
            current = self.root
            replace_node = None
            while current is not None and current.value != goal:
                parent = current
                if goal >= current.value:
                    current = current.right
                    flag = 1
                else:
                    current = current.left
                    flag = 0

            if current is None:
                print("node not in this tree")
            else:
                if current.left is None and current.right is None:
                    if flag:
                        parent.right = None
                    else:
                        parent.left = None
                    del current

                elif (current.left is None) or (current.right is None):
                    if current.left is None:
                        if flag:
                            parent.right = current.right
                        else:
                            parent.left = current.right
                    else:
                        if flag:
                            parent.right = current.left
                        else:
                            parent.left = current.left

                    del current
                else:
                    replace_node = self.minimum_element(current.right)
                    temp = replace_node.value
                    self.delete(replace_node.value)
                    current.value = temp

    def minimum_element(self, node):
        if self.root is None:
            print("Empty BST")
        else:
            while (node.left is not None):
                node = node.left
            #print(node.data)
            return node

    def max_elem(self):
        node = self.root.left
        while node.right is not None:
            node = node.right
        return node.value

    def height(self, node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)

            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1

    def output_sup(self, elem):
        rflag, lflag = 0, 0
        print('root: {0}'.format(elem.value))
        if elem.left is not None:
            print('left: {0}'.format(elem.left.value))
            lflag = 1
        else:
            print('left:  ')

        if elem.right is not None:
            print('right: {0}'.format(elem.right.value)+"\n")
            rflag = 1
        else:
            print('right:  '+"\n")

        if lflag:
            self.output_sup(elem.left)
        if rflag:
            self.output_sup(elem.right)

    def output(self):
        print()
        if self.root is None:
            return "empty"
        self.output_sup(self.root)

    def out_sup(self, elem, i):
        lflag, rflag = 0, 0
        s = " " * (self.height(self.root) - 1 - i)
        if elem.left is not None:
            s += str(elem.left.value) + " "
            lflag = 1
        else:
            s += " "
        if elem.right is not None:
            s += str(elem.right.value) + ' '
            rflag = 1
        else:
            s += " "
        print(s)
        i += 1
        if lflag:
            self.out_sup(elem.left, i)
        if rflag:
            self.out_sup(elem.right, i)

    def out(self):
        if self.root is None:
            print("the tree is empty")
            return
        spaces = self.height(self.root)
        s = " "*(spaces-1) + str(self.root.value)
        print(s)
        i = 1
        self.out_sup(self.root, i)


tree = BinaryTree()
tree.add(9)
tree.add(4)
tree.add(30)
tree.add(8)
tree.add(1)
tree.add(35)
tree.add(15)
tree.add(40)
tree.out()
#tree.delete(40)
#print(tree.max_elem())
#tree.delete(9)
#tree.del_elem(9)
#tree.add(1)
#print(tree.find(8))
#tree.add(15)
#tree.add(35)
#tree.add(0)
#tree.print_tree()
#tree.output()
#tree.output123()
#tree.add(0)
#print(tree.height(tree.root))
#tree.output1()
#tree.traverse(9)
#tree.delete(9)
#tree.output()
#tree.printTree()