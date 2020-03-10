import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList



class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # entering the queue to the end ('tail') 
    def enqueue(self, value):
        self.size += 1
        print(value)
        self.storage.add_to_tail(value)
        
    # Leaving the queue the front ('front')
    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            value = self.storage.remove_from_head()
        return value 
    # length of te queue
    def len(self):
        return self.storage.__len__()
