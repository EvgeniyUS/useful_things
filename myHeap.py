import random


class MyHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def add(self, item):
        self.heap.append(item)
        self.size += 1
        self.sift_up(self.size - 1)

    def make_heap(self, l):
        self.heap = l
        self.size = len(l)
        for i in reversed(range(0, self.size // 2)):
            self.sift_down(i)

    def sift_up(self, index):
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[self.parent(
                index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def sift_down(self, index):
        max_index = index
        l = self.left_child(index)
        if l <= self.size - 1 and self.heap[l] > self.heap[index]:
            max_index = l
        r = self.right_child(index)
        if r <= self.size - 1 and self.heap[r] > self.heap[max_index]:
            max_index = r
        if index != max_index:
            self.heap[index], self.heap[max_index] = self.heap[max_index], self.heap[index]
            self.sift_down(max_index)

    def get_top(self):
        return self.heap[0]

    def extract_top(self):
        if self.size != 0:
            top = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            del self.heap[self.size - 1]
            self.size -= 1
            self.sift_down(0)
            return top
        else:
            return False

    def remove(self, index):
        self.heap[index] = self.heap[0] + 1
        self.sift_up(index)
        self.extract_top()

    def change_priority(self, index, priority):
        old_priority = self.heap[index]
        self.heap[index] = priority
        if priority > old_priority:
            self.sift_up(index)
        else:
            self.sift_down(index)

    def draw(self):
        lvl = []
        row1 = 0
        row2 = 0
        space = ' '
        for idx, i in enumerate(self.heap):
            space = ' '
            if idx <= row1:
                lvl.append(i)
            else:
                print(' ' * (self.size - row1), space.join([str(item) for item in lvl]))
                lvl = [i]
                if row1 == 0:
                    row1 = 2
                else:
                    row3 = int(row2)
                    row2 = int(row1)
                    row1 = row2 + (row2 - row3) * 2
        print(' ' * (self.size - row1), space.join([str(item) for item in lvl]))

    @staticmethod
    def parent(index):
        return (index - 1) // 2

    @staticmethod
    def left_child(index):
        return index * 2 + 1

    @staticmethod
    def right_child(index):
        return index * 2 + 2


H = MyHeap()
H.make_heap([random.randint(100, 200) for i in range(random.randint(14, 19))])

print(H.heap)
print(f'L = {H.size}')

H.draw()
print(f'\n__TOP__ - {H.extract_top()}')
H.draw()
print(f'\n__TOP__ - {H.extract_top()}')
H.draw()
print(f'\n__TOP__ - {H.extract_top()}')
H.draw()