class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None


  def push(self,new):
      new = Node(new)
      new.next = self.head
      self.head = new
  def deletenode(self,data):
      temp = self.head

      if temp is not None:
          if temp.data == data:
              temp = temp.next
              return
      while temp is not None:
          if temp.data == data:
              break
          prev = temp
          temp = temp.next

      if temp is None:
          return

      prev.next = temp.next

      temp = None


  def printlist(self):
    temp = self.head
    while temp is not None:
        print(temp.data)
        temp = temp.next




if __name__ == "__main__":
  l = LinkedList()

  l.push(1)
  l.push(2)
  l.push(3)
  l.push(4)
  l.push(5)
  l.push(6)

  l.printlist()

  l.deletenode(1)
  l.deletenode(4)

  l.printlist()