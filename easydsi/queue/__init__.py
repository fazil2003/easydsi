import sys
import time

class Queue():

    # Initialize
    def __init__(self, elements, visualize):

        start_time = time.time()

        self.size = len(elements)
        self.elements = elements
        
        # Settings
        self.visualize = visualize
        self.visualize_count = 0
        self.set_maximum_size = float('INF')
        self.set_allow_str = True

        end_time = time.time()
        time_taken = end_time - start_time

        if self.visualize:
            self.display_visualize_message("Queue has been created with the elements: " + str(elements), time_taken)
            

    def __str__(self):
        return str(self.elements)

    def __repr__(self):
        return str(self.elements)

    def display_visualize_message(self, message, time_taken):
        self.visualize_count += 1
        print(self.visualize_count, " - " , message)
        for index, element in enumerate(self.elements):
            if self.size == 1:
                print("Front <- | ", end = "")
                print(str(element), end = "")
                print(" | <- Rear", end = "")
                print()
            elif index == 0:
                print("Front <- | ", end = "")
                print(str(element), end = "")
            elif index == self.size - 1:
                print(" | " + str(element), end = "")
                print(" | <- Rear", end = "")
                print()
            else:
                print(" | " + str(element), end = "")

        print("Memory Usage: " + str(sys.getsizeof(self.elements)))
        print("Time Taken: " + str(time_taken))

    # Settings of the queue
    def set(
        self,
        visualize = False,
        maximum_size = float('INF'),
        allow_str = True
        ):
        self.visualize = visualize
        self.set_maximum_size = maximum_size
        self.set_allow_str = allow_str
        pass
    
    # Find the element on the index
    def index(self, position):
        if(position >= self.size or position < 0):
            print("Index out of Range")
        else:

            if self.visualize:
                self.display_visualize_message("Element at the position: " + str(position) + " is " + str(self.elements[position]))

            return self.elements[position]
            
    # Find the index of the element
    def find(self, element):
        try:

            start_time = time.time()
            position = self.elements.index(element)
            end_time = time.time()
            time_taken = end_time - start_time

            if self.visualize:
                self.display_visualize_message("The element " + str(element) + " is found at the position: " + str(position), time_taken)

        except ValueError:
            print("Value not present.")
            position = -1
        
        return position

    # Add the element to the queue
    def add(self, position = -1, element = None):

        start_time = time.time()

        # CHECK SETTINGS
        # Maximum size
        if(self.set_maximum_size != float('INF')):
            if(self.size >= self.set_maximum_size):
                return "Maximum size exceeded."
        
        # Allow Str
        if(not self.set_allow_str):
            if(isinstance(element, str)):
                return "String is not allowed."

        # If no element is given, but position is given, then take position as element
        if(element == None and position!=-1):
            element = position
            position = self.size
        elif(element == None):
            print('Please pass the element to insert.')
            return None

        # If no position is given, add it to the last
        if(position == -1):
            position = self.size

        if(self.size == 0):
            self.elements = [0] * position
            self.elements.append(element)
        else:
            if(position > self.size):
                self.elements += [0] * (position - self.size)
                self.elements.append(element)
                self.size += (position - self.size) 
            else:
                self.elements.insert(position, element)
        self.size += 1

        end_time = time.time()
        time_taken = end_time - start_time

        if self.visualize and element is not None:
            self.display_visualize_message("The element " + str(element) + " is inserted in the position: " + str(position), time_taken)


    # Add the element in the position and remove the other element
    def add_and_remove(self, position = -1, element = None):

        # If no element is given
        if(element == None):
            print('Please pass the element to insert.')
            return None

        # If no position is given, add it to the last
        if(position == -1):
            position = self.size

        if(self.size == 0):
            self.elements = [0] * position
            self.elements.append(element)
        else:
            if(position < self.size):
                del self.elements[position]
            self.elements.insert(position, element)

        self.size += 1


    def add_first(self, element):
        self.add(0, element)

    def add_last(self, element):
        self.add(self.size, element)

    # Remove the element from the queue
    def remove(self, position = 0):
        if(position >= self.size or position < 0):
            print("Index Out of Range")
            return -1
        else:
            element_to_return = self.elements[position]
            self.elements.pop(position)
            self.size -= 1

            return element_to_return

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self.size - 1)

    def display(self):
        print(self.elements)

    def get_elements(self):
        return self.elements
    
    def get_size(self):
        return self.size

    # Get the maximum element from the queue
    def get_max(self):
        maximum_value = -float('INF')
        for element in self.elements:
            if(isinstance(element, int)):
                if(element > maximum_value):
                    maximum_value = element
        if(maximum_value == float('INF')):
            maximum_value = "No integer is present."
        return maximum_value
    
    # Get the minimum element from the queue
    def get_min(self):
        minimum_value = float('INF')
        for element in self.elements:
            if(isinstance(element, int)):
                if(element < minimum_value):
                    minimum_value = element
        if(minimum_value == float('INF')):
            minimum_value = "No integer is present."
        return minimum_value

    # Get the sum of all the elements from the queue
    def get_sum(self):
        sum_value = 0
        for element in self.elements:
            if(isinstance(element, int)):
                sum_value += element
        return sum_value

    # Get the average of all the elements from the queue
    def get_avg(self):
        sum_value = 0
        count_value = 0
        for element in self.elements:
            if(isinstance(element, int)):
                sum_value += element
                count_value += 1
        avg_value = 0
        if(count_value != 0):
            avg_value = sum_value/count_value
        return avg_value

    # Reverse the queue
    def reverse(self, inplace = False):
        reversed_elements = []
        for element in self.elements[::-1]:
            reversed_elements.append(element)
        if(inplace):
            self.elements = reversed_elements
        return reversed_elements

    # Sort the queue
    def sort(self, desc = False, inplace = False):
        sorted_elements = []
        sorted_numbers = []
        sorted_strings = []
        for element in self.elements:
            if(isinstance(element, int)):
                sorted_numbers.append(element)
            elif(isinstance(element, str)):
                sorted_strings.append(element)
            else:
                pass
        sorted_numbers = sorted(sorted_numbers)
        sorted_strings = sorted(sorted_strings)
        sorted_elements.extend(sorted_numbers)
        sorted_elements.extend(sorted_strings)
        # Convert to descending
        if(desc):
            sorted_elements = list(reversed(sorted_elements))
        if(inplace):
            self.elements = sorted_elements
        return sorted_elements

    # Map all the values to the function
    def map(self, function = None, inplace = False):
        if(not function):
            print("Function parameter is missing.")
            return None
        mapped_elements = []
        for element in self.elements:
            value = function(element)
            mapped_elements.append(value)
        if(inplace):
            self.elements = mapped_elements
        return mapped_elements


# CREATE A QUEUE
def queue(elements = [], visualize = False):
    return Queue(elements, visualize)