class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.head = None
    def put(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new = Node(data)
            new.next = self.head
            self.head = new
    def pop(self):
        if self.head == None:
            return None
        else:
            popnode = self.head
            self.head = self.head.next
            popnode.next =None
            return popnode.data
    def isEmpty(self):
        if self.isEmpty():
            return True
        else:
            return False
    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
