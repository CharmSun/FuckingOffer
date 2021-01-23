# 题目：数据流中的中位数
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

# 例如，

# [2,3,4] 的中位数是 3

# [2,3] 的中位数是 (2 + 3) / 2 = 2.5

# 设计一个支持以下两种操作的数据结构：

# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。

import heapq

# 大堆，小堆轮流存放


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        # 当前大顶堆和小顶堆的元素个数之和
        self.count = 0

    def addNum(self, num: int) -> None:
        if self.count & 1 == 0:
            if len(self.max_heap) > 0 and num < self.max_heap[0][1]:
                # 因为 Python 中的堆默认是小顶堆，所以要传入一个 tuple，用于比较的元素需是相反数，
                # 才能模拟出大顶堆的效果
                heapq.heappush(self.max_heap, (-num, num))
                _, max_heap_top = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, max_heap_top)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if len(self.min_heap) > 0 and num > self.min_heap[0]:
                heapq.heappush(self.min_heap, num)
                min_heap_top = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))
            else:
                heapq.heappush(self.max_heap, (-num, num))
        self.count += 1

    def findMedian(self) -> float:
        if self.count == 0:
            raise Exception('No Numbers')
        if self.count & 1:
            return self.min_heap[0]
        else:
            return (self.min_heap[0] + self.max_heap[0][1]) / 2
