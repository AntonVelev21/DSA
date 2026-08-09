class MyQueue:
    def __init__(self):
        list1 = []
        list2 = []
        self.list1 = list1
        self.list2 = list2


    def push(self, x):
        self.list1.append(x)


    def pop(self):
        if not self.list2:
            while self.list1:
                self.list2.append(self.list1.pop())

        return self.list2.pop()


    def peek(self):
        if not self.list2:
            while self.list1:
                self.list2.append(self.list1.pop())
        return self.list2[-1]


    def empty(self):
        return not self.list1 and not self.list2



my_queue = MyQueue()

for i in range(10):
    my_queue.push(i)

while not my_queue.empty():
    print(my_queue.pop())
    print(my_queue.empty())

