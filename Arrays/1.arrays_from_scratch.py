class Array:
    def __init__(self, size: int):
        self.data = {}
        self.length = 0
        self.size = size
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            raise IndexError("Index out of bounds")
        if index not in self.data:
            raise ValueError("Value not found at index")
        
        return self.data[index]

    def append(self, item:int):
        self.data[self.length] = item
        self.length += 1
        if self.length > self.size:
            raise OverflowError("Array size exceeded")
        return self.length
    
    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem
    
    def delete(self,index:int):
        item = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
            del self.data[i + 1]
        self.length -= 1
        print(f"Deleted item: {item}")
        print(f"Array after deletion: {self.data}")
        if self.length < 0:
            raise IndexError("Array is empty")
        return item

my_array = Array(10)
my_array.append(1)
my_array.append(2)
my_array.append("Andrei")

# [1, 2, "Andrei"]

print(my_array.get(0))  # Output: 1
print(my_array.get(2))
# print(my_array.get(3))
# my_array.pop()
my_array.delete(1)
print(my_array.get(1))