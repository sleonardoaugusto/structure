class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def _hash(self, key):
        hash_idx = 0
        for letter in key:
            hash_idx = (hash_idx + ord(letter) * 23) % len(self.data_map)
        return hash_idx

    def set(self, key, value):
        idx = self._hash(key)
        if self.data_map[idx] is None:
            self.data_map[idx] = []
        self.data_map[idx].append([key, value])

    def get(self, key):
        idx = self._hash(key)
        if self.data_map[idx]:
            for data in self.data_map[idx]:
                if data[0] == key:
                    return data[1]

    def keys(self):
        keys = []
        for items in self.data_map:
            if items:
                for item in items:
                    keys.append(item[0])
        return keys
