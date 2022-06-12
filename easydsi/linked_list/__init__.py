from multipledispatch import dispatch

# COLLECTION OF LINKED LIST METHODS
class LinkedList():

    def __init__(self, elements):
        self.size = len(elements)
        self.elements = elements
        self.length = len(elements)
    
    def index(self, position):
        return self.elements[position]

    def add(self, position, element):
        if(self.length == 0):
            self.elements.append(element)
        else:
            while(position > self.size):
                self.elements.append(0)
                self.size += 1
            self.elements.insert(position, element)

        self.size += 1
        self.length += 1

    def add_first(self, element):
        self.elements.insert(0, element)
        self.size += 1
        self.length += 1

    def add_last(self, element):
        self.elements.append(element)
        self.size += 1
        self.length += 1

    def remove(self, position):
        if(position < self.size):
            elementToReturn = self.elements[position]
            del self.elements[position]
            self.size -= 1
            self.length -= 1
            while(self.elements[-1] == 0):
                del self.elements[-1]
                self.size -= 1
            return elementToReturn
        else:
            print("List Index Out of Bounds")

    def remove_first(self):
        if(self.length > 0):
            del self.elements[0]
            self.size -= 1
            self.length -= 1

    def remove_last(self):
        if(self.length > 0):
            del self.elements[-1]
            self.size -= 1
            self.length -= 1

    def display(self):
        print(self.elements)

    def get_elements(self):
        return self.elements
    
    def get_size(self):
        return self.size

    def get_length(self):
        return self.length
    

# CREATE AN LINKED LIST

#passing one parameter
@dispatch(list)
def linked_list(elements):
    return LinkedList(elements)

#passing zero parameter
@dispatch()
def linked_list():
    return LinkedList([])


