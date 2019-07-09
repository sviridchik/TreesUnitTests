class Defin:
    """"define elem"""

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class FLL:
    """first last and len"""

    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        if self.first != None:
            current = self.first
            result = str(current.value) + '\n'
            while current.next is not None:
                current = current.next
                result += str(current.value) + '\n'
            return result
        return "Empty"

    def addFirst(self, elem):
        if self.last == None:
            self.first = self.last = Defin(elem)
        else:
            self.first = Defin(elem, self.first)

    def add(self, elem):
        if self.first is None:
            self.last = self.first = Defin(elem, None)
        else:
            self.last.next = self.last = Defin(elem, None)

    def destroy(self):
        self.__init__()

    def search1(self,elem):
        lenght = 0
        if self.first is None:
            return "list is empty"
        current = self.first
        if current.value == elem:
            return lenght
        while current.next is not None:
            lenght += 1
            current = current.next
            if current.value == elem:
                return lenght
        return "not in list"


    def addAfter(self,index, elem):
        if self.first is None:
            return "list is empty"
        lenght = 0
        if index == 0:
            self.first.next = Defin(elem,self.first.next)
        current = self.first.next
        while current is not None:
            lenght += 1
            if lenght == index:
                current.next = Defin(elem, current.next)
                return
            current = current.next


    def delAfter(self, index):
        if self.first is None:
            return "list is empty"
        lenght = 0
        current = self.first.next
        while current is not None and current.next is not None and current.next.next:
            lenght += 1
            if lenght == index:
                temp = current.next
                temp.value = temp.next.value
                temp.next = temp.next.next
                return
            current = current.next
        return "invalid data"

    def sort(self):
        if self.first is None:
            return "list is empty"
        current = self.first
        newlist = []
        while current is not None:
            newlist.append(current.value)
            current = current.next
        newlist = sorted(newlist)
        result = Defin()
        for i in newlist:
            print(i)
        return result



    """не работает не мпеняет местами"""
    def selection_sort(self):
        def len(self):
            length = 1
            if self.first is not None:
                current = self.first
                while current.next is not None:
                    current = current.next
                    length += 1
            return length

        def search2(index):
            lenght = 0
            if self.first is None:
                return "list is empty"
            current = self.first
            if index == 0:
                return current.value
            while current.next is not None:
                lenght += 1
                current = current.next
                if index == lenght:
                    return current.value
            return "not in list"
        lenght = len(self)
        index = 0
        #print(search2(self,index))
        while index < lenght - 1:
            smallest = index
            j = index + 1

            while j < lenght:
                if search2(j) < search2(index):
                    smallest = j
                j += 1
            a, b = search2(index), search2(smallest)
            a, b = search2(smallest), search2(index)
            index += 1
        return self




o = FLL()
o.add(4)
o.add(3)
o.add(2)
#o.addAfter(1, 9)
#o.addAfter(1, 9)
print(o)
#o.delAfter(1)
#o.selection_sort()
print(o.sort())

