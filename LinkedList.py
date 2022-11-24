class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}'


class LinkedList:
    def __init__(self):
        self.head = None

    # checking if list is empty or not
    def isEmpty(self):
        return self.head == None

    # finding length of list
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # displaying data of list
    def view(self):
        current = self.head
        while current:
            if current == self.head:
                print(f"[Head: {self.head.data}] -> ", end="")
                current = current.next
            elif current.next is None:
                print(f"[Tail: {current.data}]")
                break
            else:
                print(f"{current} -> ", end="")
                current = current.next

    # prepending data
    def prepend(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data

    # appending data
    def append(self,data):
        new_data = Node(self,data)
        if self.head is None:
            self.head = new_data
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_data

    # inserting data at certain index
    def ins(self, data, index):
        current = self.head
        prev = None
        count = 0
        while current or prev:
            if index == 0:
                self.prepend(data)
                return
            elif count == index:
                prev.next = Node(data)
                prev.next.next = current
                return
            else:
                prev = current
                current = current.next
                count += 1

    # searching by value
    def search(self, value):
        current = self.head
        found = False
        while current and not found:
            if current.data == value:
                found = True
            current = current.next
        if found:
            return f'{value} found in the list'
        return f'{value} not found in the list'

    # finding nth value
    def find_nth(self, index):
        current = self.head
        count = 0
        found = False
        while current:
            if count == index:
                return current
            count += 1
            current = current.next

    # delete by value
    def delete_by_value(self, data):
        current = self.head.next
        prev = self.head
        if self.head.data == data:
            self.head = self.head.next
            print(f'Node Deleted having value {data}')
            return
        while current:
            if current.data == data:
                prev.next = current.next
                print(f'Node Deleted having value {data}')
                return
            prev = current
            current = current.next

    # delete by index
    def delete_by_index(self, index):
        if index == 0:
            self.head = self.head.next
            print(f"Node {index} Deleted")
            return
        current = self.head.next
        prev = self.head
        count = 1
        while current:
            if count == index:
                prev.next = current.next
                print(f"Node {index} Deleted")
                return
            prev = current
            current = current.next
            count +=1


# if __name__ == "__main__":
#     l = LinkedList()
#     print(l.isEmpty())
#     l.prepend(10)
#     l.prepend(20)
#     l.prepend(30)
#     l.prepend(40)
#     l.prepend(50)
#     l.prepend(60)
#     l.view()
#     print(l.size())
#     l.ins(15,1)
#     l.ins(25,3)
#     l.view()
#     print(l.size())
#     print(l.search(10))
#     print(l.find_nth(3))
#     l.delete_by_index(3)
#     l.delete_by_value(15)
#     l.view()
#     l.size()
