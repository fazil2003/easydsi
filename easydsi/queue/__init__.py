from multipledispatch import dispatch

class Queue():

    def __init__(self, size, elements):
        self.size = size
        self.elements = elements
        if(any(self.elements)):
            self.length = len(elements)
        else:
            self.elements = []
            self.length = 0

    def __str__(self):
        return str(self.elements)

    def __repr__(self):
        return str(self.elements)
    
    def index(self, position):
        return self.elements[position]

    def add(self, element):
        if(self.size == self.length):
            print("Queue is full. Cannot add element ", element)
        else:
            self.elements.append(element)
            self.length += 1

    def remove(self):
        if(self.length == 0):
            print("Queue is empty. Cannot remove an element.")
        else:
            elementToReturn = self.elements.pop(0)
            self.length -= 1
            return elementToReturn
            
    def display(self):
        print(self.elements)

    def get_elements(self):
        return self.elements
    
    def get_size(self):
        return self.size

    def get_length(self):
        return self.length

class DoubleEndedQueue(Queue):

    def __init__(self, size, elements):
        super().__init__(size, elements)

    def add_first(self, element):
        if(self.size == self.length):
            print("Queue is full. Cannot add element ", element)
        else:
            self.elements.insert(0, element)
            self.length += 1

    def add_last(self, element):
        if(self.size == self.length):
            print("Queue is full. Cannot add element ", element)
        else:
            self.elements.append(element)
            self.length += 1

    def remove_first(self):
        if(self.length == 0):
            print("Queue is empty. Cannot remove an element.")
        else:
            del self.elements[0]
            self.length -= 1

    def remove_last(self):
        if(self.length == 0):
            print("Queue is empty. Cannot remove an element.")
        else:
            del self.elements[-1]
            self.size -= 1
            self.length -= 1
    

def queue(size):

    if(isinstance(size, int)):
        elements = [0] * size
        return Queue(size, elements)

    elif(isinstance(size, list)):
        elements = size
        size = len(elements)
        return Queue(size, elements)

def double_ended_queue(size):

    if(isinstance(size, int)):
        elements = [0] * size
        return DoubleEndedQueue(size, elements)

    elif(isinstance(size, list)):
        elements = size
        size = len(elements)
        return DoubleEndedQueue(size, elements)