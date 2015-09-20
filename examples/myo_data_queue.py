class MyoDataQueue:
    def __init__(self, size=1000):
        self.size = size
        self.elts = DoublyLinkedList()
        
    def push(self,elt):
        if self.elts.size<self.size:            
            self.elts.addToBack(elt)

    def get(self):
        ret = None
        if not self.elts.empty:
            ret = self.elts.popFromFront()
        return ret

# underlying data structure to allow enqueue and dequeue in constant time
class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.empty = True
        self.first = None
        self.last = None

    def addToFront(self,val):
        node = Node(val)
        self.size += 1        
        if self.empty:
            self.empty = False
            self.first = node
            self.last = node
        else:
            node.post = self.first
            node.post.prev = node
            self.first = node

    def addToBack(self,val):
        node = Node(val)
        self.size += 1        
        if self.empty:
            self.empty = False
            self.first = node
            self.last = node
        else:
            self.last.post = node
            node.prev = self.last
            self.last = node

    def popFromFront(self):
        if not self.empty:
            node = self.first
            self.first = self.first.post
            if self.first is None:
                self.empty = True
            else:
                self.first.prev = None
            self.size -= 1
            return node.val

    def popFromBack(self):
        if not self.empty:
            node = self.last
            self.last = self.last.prev
            if self.last is None:
                self.empty = True
            else:
                self.last.post = None
            self.size -= 1
            return node.val

    def iterate(self):
        node = self.first
        elts = []
        while node is not None:
            elts.append(node.val)
            node = node.post
        return elts

class Node:
    def __init__(self,val):
        self.val=val
        self.prev = None
        self.post = None

    def setNext(self,post):
        self.post=post

    def setPrev(self,prev):
        self.prev=prev
        
