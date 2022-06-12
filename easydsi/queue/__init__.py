from multipledispatch import dispatch

class Queue():

    def __init__(self, elements):
        self.size = len(elements)
        self.elements = elements

    def __str__(self):
        return str(self.elements)

    def __repr__(self):
        return str(self.elements)
    
    def index(self, position):
        return self.elements[position]

    @dispatch()
    def add(self, position, element):
        if(self.size == 0):
            self.elements = [0] * position
            self.elements.append(element)
        else:
            self.elements.insert(position, element)
        self.size += 1
    
    @dispatch()
    def add(self, element):
        self.elements.append(element)
        self.size += 1

    @dispatch()
    def add_and_remove(self, position, element):
        if(self.size == 0):
            self.elements = [0] * position
            self.elements.append(element)
        else:
            if(position < self.size):
                del self.elements[position]
            self.elements.insert(position, element)
        self.size += 1
    
    @dispatch
    def add_and_remove(self, element):
        self.elements.append(element)
        self.size += 1

    def add_first(self, element):
        self.elements.insert(0, element)
        self.size += 1

    def add_last(self, element):
        self.elements.append(element)
        self.size += 1

    @dispatch
    def remove(self, position):
        if(position >= self.size or position < 0):
            print("Index Out of Range")
            return -1
        else:
            elementToReturn = self.elements[position]
            del self.elements[position]
            self.elements.insert(position, 0)
            self.size -= 1
            return elementToReturn
    
    @dispatch
    def remove(self):
        if(self.size > 0):
            elementToReturn = self.elements.pop()
            self.size -= 1
            return elementToReturn
        else:
            print("No elements found.")

    def remove_first(self):
        if(self.size > 0):
            del self.elements[0]
            self.size -= 1
            self.length -= 1
        else:
            print("No elements found.")

    def remove_last(self):
        if(self.size > 0):
            del self.elements[-1]
            self.size -= 1
            self.length -= 1
        else:
            print("No elements found.")

    def display(self):
        print(self.elements)

    def get_elements(self):
        return self.elements
    
    def get_size(self):
        return self.size
    
# CREATE A QUEUE
# Passing one parameter
@dispatch(list)
def queue(elements):
    return Queue(elements)

# Passing zero parameter
@dispatch()
def queue():
    return Queue([])

# if(isinstance(size, int)):
#     elements = [0] * size
#     return Array(size, elements)

# elif(isinstance(size, list)):
#     elements = size
#     size = len(elements)
#     return Array(size, elements)