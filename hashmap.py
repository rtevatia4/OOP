class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    def __init__(self, size):
        self.size = size
        self.hash_map = [[] for i in range(self.size)]
    
    def hash_function(self, key):
        return key%self.size

    def set(self, key, value):
        hash_index = self.hash_function(key)

        for item in self.hash_map[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.hash_map[hash_index].append(Item(key,value))
    
    def get(self, key):
        hash_idx = self.hash_function(key)

        for item in self.hash_map[hash_idx]:
            if item.key == key:
                return item.value
        
        return "Key not found"
    
    def delete(self, key):
        hash_idx = self.hash_function(key)
        for idx, item in enumerate(self.hash_map[hash_idx]):
            if item.key == key:
                del self.hash_map[hash_idx][idx]
                return
        
        return "Key not found"

hashMap = HashMap(50)
hashMap.set(2,5)
hashMap.set(3,6)
print(hashMap.get(3))
print(hashMap.hash_map)
