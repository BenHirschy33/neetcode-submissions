
class MyCircularQueue:

    def __init__(self, k: int):
        assert(k >= 1 and k <= 1000)
        self.k = k
        self.cq = [0] * k
        # Index of current front
        self.front_i = 0
        self.size = 0
        # insert_i = (front_i + size) % k 

    def enQueue(self, value: int) -> bool:
        assert(value >= 0 and value <= 1000)
        if (self.isFull()):
            return False
        
        # Set next insert index to value
        self.cq[(self.front_i + self.size) % self.k] = value
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        if (self.isEmpty()):
            return False
        
        # Move front index to next item
        self.front_i += 1
        self.size -= 1
        return True

        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.cq[self.front_i]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.cq[(self.front_i + self.size - 1) % self.k]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()