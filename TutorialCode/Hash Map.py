# Hash map is the underlying data structure for dictionary.
# The hash fxn converts the string key into an index, into an array.

class HashTable:
    def __init__(self):
        self.Max = 100  # This represents the size of the list.
        self.arr = [None for i in range(self.Max)]  # Looping through the list.

    def get_hash_fxn(self, key):
        h = 0
        for char in key:
            h += ord(char)  # ord() fxn provides the ascii value.
            # using 100 as the size of the list. It could be more or less.
        return h % self.Max

    def __setitem__(self, key, val):
        h = self.get_hash_fxn(key)
        self.arr[h] = val

    def __get__(self, key):
        h = self.get_hash_fxn(key)
        return self.arr[h]


if __name__ == '__main__':
    t = HashTable()
    val = t.get_hash_fxn('march 6')
    print(val)
