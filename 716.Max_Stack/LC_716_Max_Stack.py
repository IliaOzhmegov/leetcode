import heapq

class MaxStack:

    def __init__(self):
        self.heap = []
        self.stack = []

        self.stack_elements_to_remove = []
        self.heap_elements_to_remove = []

        self.is_heaped = False
        # self.is_stacked = False

    def push(self, x: int) -> None:
        self.__empty_stack_elements_to_remove()
        self.heap.append(-x)
        self.stack.append(x)
        self.is_heaped = False

    def pop(self) -> int:
        self.__empty_stack_elements_to_remove()
        val = self.stack.pop()
        self.heap_elements_to_remove.append(-val)
        self.is_heaped = False
        return val

    def top(self) -> int:
        self.__empty_stack_elements_to_remove()
        return self.stack[-1]

    def peekMax(self) -> int:
        self.__empty_heap_elements_to_remove()
        return -self.heap[0]

    def popMax(self) -> int:
        self.__empty_heap_elements_to_remove()
        val = -heapq.heappop(self.heap)
        self.stack_elements_to_remove.append(val)
        # self.is_stacked = False
        return val

    def __empty_heap_elements_to_remove(self):
        if len(self.heap_elements_to_remove):
            for element in self.heap_elements_to_remove:
                self.heap.remove(element)
            self.heap_elements_to_remove = []
            self.is_heaped = False
        if not self.is_heaped:
            heapq.heapify(self.heap)

    def __empty_stack_elements_to_remove(self):
        if len(self.stack_elements_to_remove):
            self.stack.reverse()
            for element in self.stack_elements_to_remove:
                self.stack.remove(element)
            self.stack_elements_to_remove = []
            self.stack.reverse()

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()