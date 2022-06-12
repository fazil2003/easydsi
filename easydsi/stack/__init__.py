from multipledispatch import dispatch

class Stack():

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
            print("Stack is full. Cannot add element ", element)
        else:
            self.elements.append(element)
            self.length += 1

    def remove(self):
        if(self.length == 0):
            print("Stack is empty. Cannot remove an element.")
        else:
            elementToReturn = self.elements.pop()
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


def stack(size):

    if(isinstance(size, int)):
        elements = [0] * size
        return Stack(size, elements)

    elif(isinstance(size, list)):
        elements = size
        size = len(elements)
        return Stack(size, elements)