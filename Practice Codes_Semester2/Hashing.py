class HashMap:
    def __init__(self):
        self.hashmap = {}

    def add(self, key, value):
        self.hashmap[key] = value

    def get(self, key):
        return self.hashmap.get(key, None)

    def remove(self, key):
        if key in self.hashmap:
            del self.hashmap[key]
        else:
            print(f"Key not found: {key}")

# Example usage:
hashmap = HashMap()

hashmap.add("name", "John")
hashmap.add("age", 25)
hashmap.add("city", "New York")

print(hashmap.get("name"))  # Output: John
print(hashmap.get("age"))   # Output: 25
print(hashmap.get("city"))  # Output: New York

hashmap.remove("age")
# print(hashmap.get("age"))  # This would raise a KeyError since "age" is removed
