# coding=utf-8

import sys
from typing import List


class Bank:
    def __init__(self, N: int, M: int):
        self.windows = []
        self.queueMax = M
        for i in range(N):
            self.windows.append([])

    def serveCustomers(self, K: int, times: List[int]):
        self.K = K
        self.times = times
        self.leaveTimes = [0] * K
        for i in range(K):
            self.enqueue(i, times[i])

    def enqueue(self, index: int, time: int):
        num = 0
        for i in range(1, len(self.windows)):
            if len(self.windows[i]) < len(self.windows[num]):
                num = i
        wQueue = self.windows[num]
        if len(wQueue) >= self.queueMax:
            num = 0
            for i in range(1, len(self.windows)):
                if self.leaveTimes[self.windows[i][0]] < self.leaveTimes[self.windows[num][0]]:
                    num = i
            wQueue = self.windows[num]
            wQueue.pop(0)
        if len(wQueue) == 0:
            self.leaveTimes[index] = time
        else:
            self.leaveTimes[index] = self.leaveTimes[wQueue[-1]] + time
        wQueue.append(index)

    def queryTime(self, index: int):
        if self.leaveTimes[index] - self.times[index] >= 540:
            return 'Sorry'
        else:
            h = 8 + self.leaveTimes[index] // 60
            m = self.leaveTimes[index] % 60
            hStr = '0' + str(h) if h < 10 else str(h)
            mStr = '0' + str(m) if m < 10 else str(m)
            return hStr + ':' + mStr


if __name__ == "__main__":
    line1 = sys.stdin.readline().strip()
    N, M, K, Q = list(map(int, line1.split()))

    line2 = sys.stdin.readline().strip()
    customer_times = list(map(int, line2.split()))

    line3 = sys.stdin.readline().strip()
    query_list = list(map(int, line3.split()))

    bank = Bank(N, M)
    bank.serveCustomers(K, customer_times)

    for index in query_list:
        print(bank.queryTime(index-1))
