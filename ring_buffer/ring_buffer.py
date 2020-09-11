class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index = 0

    def append(self, item):
        # if the number of items is the same as the capacity, then set the current index to item
        if len(self.data) == self.capacity:
            self.data[self.index] = item

        # if the number of items is not the same as capacity, then set the index to add 1 and return the raminder of the index divided by the capacity
        else:
            self.data.append(item)
        self.index = (self.index + 1) % self.capacity

    def get(self):
        return self.data
