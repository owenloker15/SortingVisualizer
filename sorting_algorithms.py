import random, time


class Algorithm:
    def __init__(self, name):
        self.name = name
        self.array = random.sample(range(512), 512)

    def update_display(self, swap1=None, swap2=None):
        import sorting_visualiser

        sorting_visualiser.update(self, swap1, swap2)

    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed

class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        #start by traversing list to find smallest integer
        #once smallest is found, swap with currentIdx of sorted list starting at 0
        #increment currentIdx and repeat
        currentIdx = 0
        while currentIdx < len(self.array) - 1:
            smallestIdx = currentIdx
            for i in range(currentIdx + 1, len(self.array)):
                if self.array[i] < self.array[smallestIdx]:
                    smallestIdx = i
            self.array[currentIdx], self.array[smallestIdx] = self.array[smallestIdx], self.array[currentIdx]
            self.update_display(self.array[currentIdx], self.array[smallestIdx])
            currentIdx += 1

class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):

        # isSorted = False
        # num_iterations = 0
        # while not isSorted:
        #     isSorted = True
        #     for i in range(len(self.array) - 1 - num_iterations):
        #         if (self.array[i] > self.array[i + 1]):
        #             self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
        #             isSorted = False
        #     num_iterations += 1
        #     self.update_display(self.array[i], self.array[i + 1])

        for i in range(len(self.array)):
            for j in range(len(self.array) - 1 - i):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
            self.update_display(self.array[j], self.array[j + 1])

class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        #iterate through array from idx = 1 to len(array)
        #if array[i] < array[i - 1] swap them
        #create a temp var, j that = i and decrement j through array and compare and swap values respectively
        for i in range(1, len(self.array)):
            j = i
            while j > 0 and self.array[j] < self.array[j - 1]:
                self.array[j], self.array[j - 1] = self.array[j - 1], self.array[j]
                j -= 1
                self.update_display(self.array[j], self.array[j - 1])

class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self, array=[]):
        if array == []:
            array = self.array
        if len(array) < 2:
            return array
        mid = len(array) // 2
        left = self.algorithm(array[:mid])
        right = self.algorithm(array[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            self.update_display()
        result += left[i:]
        result += right[j:]
        self.array = result
        self.update_display()
        return result

class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self, array=[], start=0, end=0):
        if array == []:
            array = self.array
            end = len(array) - 1
        if start < end:
            pivot = self.partition(array, start, end)
            self.algorithm(array, start, pivot - 1)
            self.algorithm(array, pivot + 1, end)

    def partition(self, array, start, end):
        x = array[end]
        i = start - 1
        for j in range(start, end + 1, 1):
            if array[j] <= x:
                i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    self.update_display(array[i], array[j])
        return i

class HeapSort(Algorithm):
    def __init__(self):
        super().__init__("HeapSort")

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.array[i] < self.array[left]:
            largest = left
        if right < n and self.array[largest] < self.array[right]:
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.update_display(self.array[i], self.array[largest])
            self.heapify(n, largest)

    def algorithm(self):
        n = len(self.array)
        for i in range(n,-1,-1):
            self.heapify(n, i)
        for i in range(n-1,0,-1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(i, 0)