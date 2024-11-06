# PRANAV UMAKANT PUJAR 1001965075

class DynamicArray:
    def __init__(self):
        self.size = 0  
        self.capacity = 1  

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
        # resize if run out of space
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        self.array[self.size] = value
        self.size += 1
    
    def _resize(self, new_capacity):
        new_array = [0] * new_capacity
        
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


def main():
    # init new dynamic C-style array
    dynamic_array = DynamicArray()
    
    print("Adding elements to the dynamic array:")
    for i in range(5):
        dynamic_array.pushback(i)
        print(f"Added {i}: size = {dynamic_array.length()}, capacity = {dynamic_array.capacity}")
    
    # Test get method
    print("\nTesting get method:")
    try:
        for i in range(dynamic_array.length()):
            print(f"Element at index {i}: {dynamic_array.get(i)}")
    except IndexError as e:
        print(e)
    
    # Test set method
    print("\nTesting set method:")
    try:
        dynamic_array.set(2, 99)
        print("Set index 2 to 99")
        print(f"Element at index 2 after set: {dynamic_array.get(2)}")
    except IndexError as e:
        print(e)

    # Test popback method
    print("\nTesting popback method:")
    try:
        while dynamic_array.length() > 0:
            removed = dynamic_array.popback()
            print(f"Popped {removed}: size = {dynamic_array.length()}, capacity = {dynamic_array.capacity}")
    except IndexError as e:
        print(e)
    
    # Test for popback on empty array
    print("\nTesting popback on empty array:")
    try:
        dynamic_array.popback()
    except IndexError as e:
        print(e)

if __name__ == "__main__":
    main()
