from multipledispatch import dispatch

class Stack():

    def __init__(self, size, elements):
        self.size = size
        self.elements = elements
        self.length = len(elements)
    
    def index(self, position):
        return self.elements[position]

    def add(self, element):
        if(self.size == len(self.elements)):
            print("Stack is full")
        else:
            self.elements.append(element)
            self.length += 1

    def remove(self):
        if(len(self.elements) == 0):
            print("Stack is empty")
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