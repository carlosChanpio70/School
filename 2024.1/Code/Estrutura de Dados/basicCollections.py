# Author: Luiz Thadeu Grizendi
# UniAcademia - Juiz de Fora
# Minas Gerais - Brasil

class stack:                                                                                                                                       
     def __init__(self,iterable=None):
         self.__items = []
         if iterable:
              for item in iterable:
                   self.push(item)
                   
     def push(self, item):
         self.__items.append(item)

     def pop(self):
         if len(self) == 0:
              raise IndexError('pop from empty stack')
         return self.__items.pop()
         #return self.__items.pop(-1)
         #return self.__items.pop(len(self)-1)
     
     def peek(self):
         if len(self) == 0:
              raise IndexError('peek/top from empty stack')
         return self.__items[-1]
         #return self.__items[len(self)-1]

     def top(self):
         """the same as peek"""
         return self.peek()

     def clear(self):
         self.__init__()
         #self.__items = []
         
     def isEmpty(self):
         return len(self) == 0

     def extend(self,iterable):
         for element in iterable:
              self.push(element)              

     def copy(self):        
          """ returns a copy of the Collection"""
          #return self.__class__(reversed([element for element in self]))
          return stack(reversed([element for element in self]))
     
     """native python functions"""
     def __contains__(self,key):
        return key in self.__items

     def __str__(self):
        return '['+', '.join([str(item) for item in self]) +']'

     def __repr__(self):
        return 'stack ->'+str(self)

     def __eq__(self, iterable):
        "Test self==iterable"
        return list(self) == list(iterable)

     def __len__(self):
        return len(self.__items)

     def __iter__(self):
          self.__current = len(self)-1
          return self          

     def __next__(self):
          if self.__current < 0:
               raise StopIteration
          else:
               self.__current -= 1
               return self.__items[self.__current + 1]     

class queue:
     def __init__(self,iterable=None):
         self.__items = []
         if iterable:
              for item in iterable:
                   self.enqueue(item)

     def clear(self):
          self.__init__()
          ##self.__items = []
         
     def copy(self):        
          """ returns a copy of the Collection"""
          return self.__class__([element for element in self])
     
     def isEmpty(self):
          return len(self) == 0

     def enqueue(self, item): 
          self.__items.append(item)
          
     def offer(self, item):  
          """the same as enqueue"""
          self.enqueue(item)
	  
     def dequeue(self):  
          if len(self) == 0:
              raise IndexError('dequeue/poll from empty queue')
          return self.__items.pop(0)
     
     def poll(self):
          """the same as dequeue"""
          return self.dequeue()

     def peek(self):  
          if len(self) == 0:
              raise IndexError('peek/front from empty queue')
          return self.__items[0]

     def front(self):
          """the same as peek"""
          return self.peek()
     
     def extend(self,iterable):
          for element in iterable:
               self.enqueue(element)
               
     """native python functions"""
     def __contains__(self,key):
          return key in self.__items
     
     def __len__(self):
          return len(self.__items)

     def __str__(self):
          return str(self.__items) 
 
     def __repr__(self):
          return 'Queue->'+repr(self.__items)

     def __iter__(self):
          return iter(self.__items)

     def __eq__(self, iterable):
        "Test self==iterable"
        return list(self) == list(iterable)

class Node(object):
     """Represents a singly linked node."""
     def __init__(self, value, next = None):
          """Instantiates a Node with a default next of None."""
          self.value = value
          self.next = next

     def __str__(self):
          return str(self.value)+'-->'+str(self.next)

     def __repr__(self):
          return str(self)
     
class linkedList(object):
     """Represents a singly linked list."""
     def __init__(self,iterable=None):
          """Instantiates a linked list with a default
             head of None and size zeroe"""
          self._size = 0
          self._head = None
          if iterable:
               for value in iterable:
                    self.append(value)
          
     """native python functions"""
     def __str__(self):
          """ The string representation of the linkedList"""
          return str([e for e in self])

     def __len__(self):
          """ Length of the list"""
          return self._size

     def __repr__(self):
          """ The representation of the linkedList"""
          return "{0} {1}".format(self.__class__.__name__, self)
     
     def __iter__(self):
          """ Supports traversal with a for loop"""
          self.__current = self._head
          return self
     
     def __next__(self):
          if self.__current == None:
               raise StopIteration
          else:
            previous = self.__current
            self.__current = self.__current.next 
            return previous.value

     def __getitem__(self, index=-1):
          """ Subscript operator for access at index"""
          if isinstance(index,slice):
               return list(self)[index]
          if index < 0:
               index+=len(self)          
          if index < 0 or index >= len(self):
               raise IndexError('list index out of range')
          probe = self._head
          while index > 0 and probe.next != None:
               probe = probe.next
               index -= 1
          return probe.value
     
     def __setitem__(self, index, value):
          """ Subscript operator for replacement at index"""
          if index < 0:
               index+=len(self)          
          if index < 0 or index >= len(self):
               raise IndexError('list assignment index out of range')
          probe = self._head
          while index > 0 and probe.next != None:
               probe = probe.next
               index -= 1
          probe.value = value
          
     def clear(self):
          """ clear data"""
          self.__init__()

     def _addFirst(self,object):
          self._head = Node(object, self._head) 
          
     def insert(self, index, object):
          """add object in to position index"""
          if index < 0:
               index+=len(self)          
          if self._head is None or index <= 0: # insert unique/first
               self._addFirst(object)
          else:
               # Search for node at position index - 1 or the last position
               current = self._head
               while index > 1 and current.next != None:
                    current = current.next
                    index -= 1
               # Insert new node after node at position index - 1
               # or last position
               current.next = Node(object, current.next)
          self._size += 1

     def append(self, object):
          """add object Last position"""
          self.insert(len(self),object)
     
     def __removeFirst(self):
          removedItem = self._head.value
          self._head = self._head.next
          self._size -= 1
          return removedItem
     
     def pop(self, index=-1):
          """remove object in to position index"""
          if len(self) == 0:
               raise IndexError('pop from empty list')
          if index < 0:
               index+=len(self)          
          if index < 0 or index >= len(self):
               raise IndexError('pop index out of range')          
          if index == 0: # remove fisrt
               return self.__removeFirst()
          # Search for node at position index - 1 or
          # the next to last position
          current  = self._head
          while index > 1 and current.next.next != None:
               current  = current.next
               index -= 1
          removedItem = current.next.value
          current.next = current.next.next
          self._size -= 1
          return removedItem

     def remove(self,value):
          """remove object equal value"""
          if len(self) == 0:
               raise IndexError('pop from empty list')
          if self._head.value == value: # remove first
               self._head = self._head.next
               self._size -= 1
               return
          current = self._head
          previous = None
          while current.next != None:
               if current.value == value:
                    previous = current.next
                    self._size -= 1
                    return
               previous = current
               current = current.next
          raise ValueError('list.remove(x): x not in list')
          
     def extend(self,iterable=None):
          """append a iterable"""
          if not iterable:
               raise TypeError('list.extend() takes exactly one argument (0 given)')
          for value in iterable:
               self.append(value)

def show(matrix):
     s="\n"
     # print array
     if not (type(matrix[0]) is list):
          linha = "\t"  
          for e in matrix:
               linha += str(e)+'\t'
          s+=linha+"\n"
          print(s)
          return

     # print matrix
     m = len(matrix)
     n = len(matrix[0])
     for i in range(m):
          linha = '\t'
          for j in range(n):
             linha += str(matrix[i][j]) + '\t'
          s+=linha+"\n"
     print(s)

if __name__ == '__main__':
     s=stack([10,30])
     #q=queue([10,30])
     #L=linkedList([10,20,30])
     #show([[0]*2]*4)
     #show([0]*4)
     
head=Node(10,Node(20,Node(30,Node(40))))
print(head)