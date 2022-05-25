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

  def swap_nodes(self,key1, key2):
    if key1 == key2:
      return
    prev_1 = None
    curr_1 = self.head

    while curr_1 and curr_1.data != key1:
      prev_1 = curr_1
      curr_1 = curr_1.next

    prev_2 = None
    curr_2 = self.head
    # print('Curr_1: ',curr_1.data,'Prev_1: ',prev_1.data)

    while curr_2 and curr_2.data != key2:
      prev_2 = curr_2
      curr_2 = curr_2.next

    # print('Curr_2: ',curr_2.data,'Prev_2: ',prev_2.data)

    if not curr_1 and curr_2:  # if they don't exists ( curr_1 or curr_2 is None )
      return

    if prev_1:
      prev_1.next = curr_2
    else:
      self.head = curr_2

    if prev_2:
      prev_2.next = curr_1
    else:
      self.head = curr_1

    curr_1.next,curr_2.next = curr_2.next,curr_1.next


# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")

# llist.print_list()
# print('-------------------')
# # llist.prepend("X")
# # llist.insert_after_node(llist.head.next, "D")
# # llist.print_list()

# # llist.delete_node('B') 
# llist.delete_node_at_pos(2)
# llist.print_list()
# print('-------------------')
# print(llist.find_length())

# Swap 

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print("Original List")
llist.print_list()

llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print_list()

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node")
llist.print_list()

llist.swap_nodes("D", "B")
print("Swapping nodes D and B where key_2 is head node")
llist.print_list()