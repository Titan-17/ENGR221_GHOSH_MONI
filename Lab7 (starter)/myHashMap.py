"""
Hey! We meet again!

Adapted from UCSD CSE12
"""

class MyHashMap:
    def __init__(self, load_factor=0.75,
                       initial_capacity=16):
        # Initializes the hash map
        # Input:
        #   load_factor (float) - threshold before resizing
        #   initial_capacity (int) - number of buckets
        # Output: None
        self.load_factor = load_factor 
        self.capacity = initial_capacity 
        self._size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    """
    Resizes the self.buckets array when the load_factor is reached.
    
    Input: None
    Output: None
    Effect: Doubles capacity and rehashes all existing entries
    """
    def resize(self):
        self.capacity *= 2 
        old_buckets = self.buckets 
        self.buckets = [[] for _ in range(self.capacity)]

        for bucket in old_buckets:
            if bucket != []:
                for entry in bucket:
                    self.put(entry.getKey(), entry.getValue())

    """
    Adds the specified key, value pair to the MyHashMap.
    
    Input:
        key   - hashable object (cannot be None)
        value - any object
    Output:
        True  -> if successfully added
        False -> if key already exists
    Raises:
        Exception if key is None
    """
    def put(self, key, value):
        if key is None:
            raise Exception("Key cannot be None")

        keyHash = hash(key)
        index = keyHash % self.capacity
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                return False

        if (self._size + 1) > self.load_factor * self.capacity:
            self.resize()
            index = hash(key) % self.capacity
            bucket = self.buckets[index]

        bucket.append(MyHashMap.MyHashMapEntry(key, value))
        self._size += 1
        return True

    """
    Replaces the value for a given key if it exists.
    
    Input:
        key      - existing key
        newValue - new value to assign
    Output:
        True  -> if replacement successful
        False -> if key not found
    Raises:
        Exception if key is None
    """
    def replace(self, key, newValue):
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for i, entry in enumerate(bucket):
            if entry.getKey() == key:
                bucket[i].setValue(newValue)
                return True
        return False

    """
    Removes the entry with the given key.
    
    Input:
        key - key to remove
    Output:
        True  -> if key existed and was removed
        False -> if key not found
    Raises:
        Exception if key is None
    """
    def remove(self, key):
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for i, entry in enumerate(bucket):
            if entry.getKey() == key:
                bucket.pop(i)
                self._size -= 1
                return True
        return False

    """
    Adds or updates a key-value pair.
    
    Input:
        key   - hashable object (cannot be None)
        value - any object
    Output:
        None
    Effect:
        Inserts new key OR updates existing key's value
    Raises:
        Exception if key is None
    """
    def set(self, key, value):
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                entry.setValue(value)
                return

        if (self._size + 1) > self.load_factor * self.capacity:
            self.resize()
            index = hash(key) % self.capacity
            bucket = self.buckets[index]

        bucket.append(MyHashMap.MyHashMapEntry(key, value))
        self._size += 1

    """
    Retrieves the value associated with a key.
    
    Input:
        key - key to search
    Output:
        value -> if key exists
        None  -> if key not found
    Raises:
        Exception if key is None
    """
    def get(self, key):
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                return entry.getValue()
        return None

    """
    Returns the number of key-value pairs.
    
    Input: None
    Output:
        int -> number of elements
    """
    def size(self):
        return self._size

    """
    Checks if the map is empty.
    
    Input: None
    Output:
        True  -> if empty
        False -> otherwise
    """
    def isEmpty(self):
        return self._size == 0

    """
    Checks if a key exists in the map.
    
    Input:
        key - key to check
    Output:
        True  -> if key exists
        False -> otherwise
    Raises:
        Exception if key is None
    """
    def containsKey(self, key):
        if key is None:
            raise Exception("Key cannot be None")

        index = hash(key) % self.capacity
        bucket = self.buckets[index]

        for entry in bucket:
            if entry.getKey() == key:
                return True
        return False

    """
    Returns a list of all keys.
    
    Input: None
    Output:
        List of keys (may be empty list if map is empty)
    """
    def keys(self):
        result = []
        for bucket in self.buckets:
            if bucket != []:
                for entry in bucket:
                    result.append(entry.getKey())
        return result

    class MyHashMapEntry:
        def __init__(self, key, value):
            # Input: key, value
            # Output: None
            self.key = key 
            self.value = value 

        def getKey(self):
            # Output: key
            return self.key 
        
        def getValue(self):
            # Output: value
            return self.value 
        
        def setValue(self, new_value):
            # Input: new_value
            # Output: None (updates value)
            self.value = new_value 


if __name__ == "__main__":
    m = MyHashMap()

    # Expected Output:
    # True (map starts empty)
    print("Is empty?", m.isEmpty())          

    # Expected Output:
    # True (new key added)
    print("Add a:", m.put("a", 1))           

    # Expected Output:
    # False (duplicate key not allowed)
    print("Add a again:", m.put("a", 2))     

    # Expected Output:
    # 1 (original value remains)
    print("Get a:", m.get("a"))              

    # Expected Output:
    # True (value replaced)
    print("Replace a:", m.replace("a", 3))   

    # Expected Output:
    # 3 (updated value)
    print("Get a after replace:", m.get("a"))

    # Expected Output:
    # Adds new key "b"
    m.set("b", 10)

    # Expected Output:
    # ['a', 'b'] (order may vary)
    print("Keys:", m.keys())                 

    # Expected Output:
    # 2
    print("Size:", m.size())                 

    # Expected Output:
    # True
    print("Contains a?", m.containsKey("a")) 

    # Expected Output:
    # True (removal successful)
    print("Remove a:", m.remove("a"))        

    # Expected Output:
    # None (no longer exists)
    print("Get a after remove:", m.get("a")) 

    # Expected Output:
    # 1 (only "b" remains)
    print("Size now:", m.size())             