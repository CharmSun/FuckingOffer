# 题目： 用两个栈实现队列
# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数
# appendTail 和 deleteHead, 分别完成在队列尾部插入节点
# 和在队列头部删除节点的功能。

class MyQueue:

    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, node):
        self.stack1.append(node)

    def deleteHead(self):
        if len(self.stack2) <= 0:
            while self.stack1:
                node = self.stack1.pop()
                self.stack2.append(node)
        if not self.stack2:
            raise Exception("Queue is empty!")
        return self.stack2.pop()

#延伸题：用两个队列实现实现一个栈

class MyStack:

    def __init__(self) -> None:
        self.queue1 = []
        self.queue2 = []

    def push(self, node):
        self.queue1.append(node)

    def pop(self):
        if not self.queue1:
            raise Exception("Stack is empty!")
        while len(self.queue1) > 1:
            node = self.queue1.pop(0)
            self.queue2.append(node)
        result = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result
