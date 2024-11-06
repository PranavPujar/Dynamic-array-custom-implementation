# PRANAV UMAKANT PUJAR 1001965075

class DynamicArray:
    def __init__(self):
        self.size = 0  # Current number of elements
        self.capacity = 1  # Total available space
        # Create a C-style array using a list with fixed capacity
        self.array = [0] * self.capacity
    
    def get(self, index):
        if index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]
    
    def set(self, index, value):
        if index >= self.size:
            raise IndexError("Index out of bounds")
        self.array[index] = value
    
    def pushback(self, value):
        # If we're out of space, resize
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        # Add the new element
        self.array[self.size] = value
        self.size += 1
    
    def _resize(self, new_capacity):
        # Create a new array with the new capacity
        new_array = [0] * new_capacity
        
        # Copy old elements
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        # Update array and capacity
        self.array = new_array
        self.capacity = new_capacity
    
    def popback(self):
        if self.size == 0:
            raise IndexError("Array is empty")
        
        self.size -= 1
        return self.array[self.size]
    
    def length(self):
        return self.size