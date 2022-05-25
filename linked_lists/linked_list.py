class Node:
  def __init__(self, data):
    # print('In Node init')
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    # print('In LL Init')
    self.head = None
  
  def print_list(self):
    cur_node = self.head
    # The below stmt will print the first node info
    # print(cur_node.data) 
    while cur_node:
      print(cur_node.data)
      cur_node = cur_node.next

  def append(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    while last_node.next:
      last_node = last_node.next
    last_node.next = new_node

  def prepend(self, data):
    new_node = Node(data)

    new_node.next = self.head
    self.head = new_node
    
  def insert_after_node(self, prev_node, data):
    if not prev_node:
      print('Previous node does not exists')
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self,key):
    cur_node = self.head

    if cur_node and cur_node.data == key:
      self.head = cur_node.next
      cur_node = None
      return

    prev_node = None
    while cur_node and cur_node.data != key:
      prev_node = cur_node
      cur_node = cur_node.next

    if cur_node is None:
      return
    
    prev_node.next = cur_node.next
    cur_node = None

  def delete_node_at_pos(self,pos):
    if self.head:
      cur_node = self.head
      if pos == 0:
        self.head = cur_node.next
        cur_node = None
        return
      
      prev_node = None
      count = 0
      while cur_node and count != pos:
        prev_node = cur_node
        cur_node  = cur_node.next
        count += 1

      if cur_node is None:
        return
      
      prev_node.next = cur_node.next
      cur_node = None

  def find_length(self):
      cur_node = self.head
      count = 0
      while cur_node:
        count+=1
        cur_node = cur_node.next

      return count



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.print_list()
print('-------------------')
# llist.prepend("X")
# llist.insert_after_node(llist.head.next, "D")
# llist.print_list()

# llist.delete_node('B') 
llist.delete_node_at_pos(2)
llist.print_list()
print('-------------------')
print(llist.find_length())