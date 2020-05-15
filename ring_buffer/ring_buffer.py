class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = []
        self.storage_at_capacity = []
    
    def increment_size(self):
        self.size = self.size + 1

    def decrement_size(self):
        self.size = self.size - 1

    def at_capacity(self):
        return self.size > self.capacity

    def append(self, item):
        self.increment_size()
        if self.at_capacity():
            self.storage.remove(self.storage[0])
            self.decrement_size()
            self.storage.insert(0, item)
            return
        self.storage.append(item)


    def get(self):
        return self.storage
            