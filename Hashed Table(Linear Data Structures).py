class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total

    def add(self, key, value):
        hashed_key = self.hash(key)

        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}

        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            bucket = self.collection[hashed_key]
            if key in bucket:
                del bucket[key]

            if not bucket:
                del self.collection[hashed_key]

    def lookup(self, key):
        hashed_key = self.hash(key)

        if hashed_key in self.collection:
            bucket = self.collection[hashed_key]
            if key in bucket:
                return bucket[key]

        return None

