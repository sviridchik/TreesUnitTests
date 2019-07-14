class Node:
    """"define elem"""

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """first last and len"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __str__(self):
        if self.head is not None:
            current = self.head
            result = str(current.value) + '\n'
            while current.next is not None:
                current = current.next
                result += str(current.value) + '\n'
            return result
        return "Empty"

    def addFirst(self, elem):
        self.len+=1
        if self.tail == None:
            self.head = self.tail = Node(elem)
        else:
            self.head = Node(elem, self.head)

    def add(self, elem):
        self.len += 1
        if self.head is None:
            self.tail = self.head = Node(elem, None)
        else:
            self.tail.next = self.tail = Node(elem, None)

    def destroy(self):
        self.__init__()

    def findIndexByValue(self, elem):
        lenght = 0
        if self.head is None:
            return "list is empty"
        current = self.head
        if current.value == elem:
            return lenght
        while current.next is not None:
            lenght += 1
            current = current.next
            if current.value == elem:
                return lenght
        return "not in list"

    """как сделать чтобы self.len срабатывало вместо def len() """
    def addAfter(self, index, elem):
        self.len += 1
        def len(self):
            length = 1
            if self.head is not None:
                current = self.head
                while current.next is not None:
                    current = current.next
                    length += 1
            return length
        if self.head is None:
            return "list is empty"
        if index > len(self):
            print("out of range")
        if index < 0:
            index = index % len(self)
        lenght = 0
        if index == 0:
            self.head.next = Node(elem, self.head.next)
        current = self.head.next
        while current is not None:
            lenght += 1
            if lenght == index:
                current.next = Node(elem, current.next)
                return
            current = current.next

    """ how can it work for the first elem? """
    def delAfter(self, index):
        def len(self):
            length = 1
            if self.head is not None:
                current = self.head
                while current.next is not None:
                    current = current.next
                    length += 1
            return length
        def GetByindex1(index):
            lenght = 0
            if self.head is None:
                return "list is empty"
            current = self.head
            if index == 0:
                return current.value
            while current.next is not None:
                lenght += 1
                current = current.next
                if index == lenght:
                    return current
            return "not in list"

        if self.head is None:
            return "list is empty"
        if index > len(self):
            print("out of range")
        if index < 0:
            index = index % len(self)
        if index == len(self)-1:
            self.tail.value = ""
        if index == len(self)-2:
            res = GetByindex1(index)
            res = res.next
            res.value = res.next.value
            res.next = res.next.next
        lenght = 0
        current = self.head.next
        while current is not None and current.next is not None and current.next.next:
            lenght += 1
            if lenght == index:
                temp = current.next
                temp.value = temp.next.value
                temp.next = temp.next.next
                return
            current = current.next
        return "invalid data"

    def del_first1(self):
        if self.head is None:
            raise RuntimeError("Empty List")
        current = self.head
        result = self.head.value
        if current.next is not None:
            current.value = current.next.value
            current.next = current.next.next

        elif current.next is None:
            self.head = Node('', None)
        return

    """_for_test"""
    def del_first(self):
        if self.head is None:
            raise RuntimeError("Empty List")
        current = self.head
        result = self.head.value
        if current.next is not None:
            current.value = current.next.value
            current.next = current.next.next

        elif current.next is None:
            self.head = Node('', None)
        return result

    def empty(self):
        if self.head is None:
            return True
        return False
    
    def bub_sort(self):
        end = None
        while end != self.head:
            r = first = self.head
            while first.next != end:
                second = first.next
                if first.value > second.value:
                    first.next = second.next
                    second.next = first
                    if first != self.head:
                        r.next = second
                    else:
                        self.head = second
                    first, second = second, first
                r = first
                first = first.next
            end = first

#o = LinkedList()
#o.add(4)
#o.add(3)
#o.add(2)
#o.bub_sort()
#print(o)
#print(o.empty())
#o.del_first()
#o.del_first()
#o.del_first()
#print(o)
#o.add(8)
#o.add(6)
#o.add(7)
#o.addAfter1(12, 9)
#o.addAfter1(1, 9)
#print(o)
#o.del_first()
#o.bubblesort1()
#o.delAfter1(3)
#print(o)
#print(o)

