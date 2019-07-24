class Node(object):
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


class BinaryTree:
    def __init__(self):
        self.root = None

    def addSup(self, nvalue, elem):
        if elem.value > nvalue:
            if elem.left is not None:
                self.addSup(nvalue, elem.left)
            else:
                elem.left = Node(nvalue)
        else:
            if elem.right is not None:
                self.addSup(nvalue, elem.right)
            else:
                elem.right = Node(nvalue)

    def add(self, nvalue):
        if self.root is None:
            self.root = Node(nvalue)
        else:
            self.addSup(nvalue, self.root)

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

    def printTree(self):
        if self.root is not None:
            self.printTreeSupp(self.root)

    def printTreeSupp(self, elem):
        if elem is not None:
            self.printTreeSupp(elem.left)
            print(str(elem.value) + ' ')
            self.printTreeSupp(elem.right)

    def minimum_element(self, node):
        if self.root is None:
            print("Empty BST")
        else:
            while (node.left is not None):
                node = node.left
            #print(node.data)
            return node

    def delete(self, goal):
        flag = 0
        if self.root is None:
            print("The list is empty")
        else:
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
                    if current.leftchild is None:
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
    """    def output123(self):
        if self.root is None:
            return "empty"
        current = self.root
        while current is not None:
            l = []
            flag = 1
            if current.left is not None:
                l.append(current.left.value)
            if current.right is not None:
                flag = 0
                l.extend(["|", current.right.value])
            if flag:
                l.append("|")
            for i in l:
                print(i,  end="")

            l.clear()
            print("\n")

            currentleft = current.left
            if currentleft.left is not None:
                l.append(currentleft.left.value)
            if currentleft.right is not None:
                flag = 0
                l.extend(["|", currentleft.right.value])
            if flag:
                l.append("|")
            for i in l:
                print(i, end="")

            l.clear()
            print("  ", end="")

            currentright = current.right
            if currentright.left is not None:
                l.append(currentright.left.value)
            if currentright.right is not None:
                flag = 0
                l.extend(["|", currentright.right.value])
            if flag:
                l.append("|")
            for i in l:
                print(i, end="")"""

    def outputSup(self, elem):
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
            self.outputSup(elem.left)
        if rflag:
            self.outputSup(elem.right)

    def output(self):
        print()
        if self.root is None:
            return "empty"
        self.outputSup(self.root)
"""    def outputSup123(self, elem):
        if elem is not None:
            spaces = self.height(self.root)

            s = '    '
            data = {0: self.root}
            if elem.left is not None:
                print(s + str(elem.left.value))
            else:
                print(s + '  ')
            if elem.right is not None:
                print(s + str(elem.right.value))
            else:
                print(s + ' ')
            print("|||")
            self.outputSup123(elem.left)
            print("left")
            self.outputSup123(elem.right)

    def output123(self):
        print()
        print(self.root.value)
        self.outputSup123(self.root)"""



tree = BinaryTree()
tree.add(9)
tree.add(4)
tree.add(30)
tree.add(8)
tree.add(1)
#print(tree.find(8))
tree.add(15)
tree.add(35)
#tree.add(0)
tree.printTree()
tree.output()
#tree.output123()
#tree.add(0)
#print(tree.height(tree.root))
#tree.output1()
#tree.traverse(9)
#tree.delete(9)
#tree.output()
#tree.printTree()