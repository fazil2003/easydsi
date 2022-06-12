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

    def getElements(self):
        return self.elements
    
    def getSize(self):
        return self.size

    def getLength(self):
        return self.length

class DoubleEndedQueue(Queue):

    def __init__(self, size, elements):
        super().__init__(size, elements)

    def addAtFirst(self, element):
        if(self.size == self.length):
            print("Queue is full. Cannot add element ", element)
        else:
            self.elements.insert(0, element)
            self.length += 1

    def addAtLast(self, element):
        if(self.size == self.length):
            print("Queue is full. Cannot add element ", element)
        else:
            self.elements.append(element)
            self.length += 1

    def removeAtFirst(self):
        if(self.length == 0):
            print("Queue is empty. Cannot remove an element.")
        else:
            del self.elements[0]
            self.length -= 1

    def removeAtLast(self):
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