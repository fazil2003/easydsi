from multipledispatch import dispatch

class Queue():

    def __init__(self, size, elements):
        self.size = size
        self.elements = elements
        self.length = len(elements)
    
    def index(self, position):
        return self.elements[position]

    def add(self, element):
        if(self.size == len(self.elements)):
            print("Queue is full")
        else:
            self.elements.append(element)
            self.length += 1

    def remove(self):
        if(len(self.elements) == 0):
            print("Stack is empty")
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


def queue(size):

    if(isinstance(size, int)):
        elements = [0] * size
        return Queue(size, elements)

    elif(isinstance(size, list)):
        elements = size
        size = len(elements)
        return Queue(size, elements)