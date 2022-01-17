# COLLECTION OF ARRAY METHODS
class Array():

    def __init__(self, size, elements):
        self.size = size
        self.elements = elements
        self.length = len(elements)
    
    def index(self, position):
        return self.elements[position]

    def add(self, position, element):
        if(self.length == 0):
            self.elements.append(element)
        else:
            if(position < self.length):
                del self.elements[position]
            self.elements.insert(position, element)
        self.length += 1

    def remove(self, position):
        if(position < self.length):
            elementToReturn = self.elements[position]
            del self.elements[position]
            self.elements.insert(position, 0)
            self.length -= 1
            return elementToReturn
        else:
            print("Index not found")

    def display(self):
        print(self.elements)

    def getElements(self):
        return self.elements
    
    def getSize(self):
        return self.size

    def getLength(self):
        return self.length
    

# CREATE AN ARRAY
def array(size):

    if(isinstance(size, int)):
        elements = [0] * size
        return Array(size, elements)

    elif(isinstance(size, list)):
        elements = size
        size = len(elements)
        return Array(size, elements)


