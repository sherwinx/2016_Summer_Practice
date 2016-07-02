class Queue(object):
    def __init__(self):
        self.inStack = []
        self.outStack = []
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        self.inStack.append(x)
        """
        :type x: int
        :rtype: nothing
        """
        

    def pop(self):
        self.peek()
        self.outStack.pop()
        
        """
        :rtype: nothing
        """
        

    def peek(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]
        """
        :rtype: int
        """
        

    def empty(self):
        return len(self.inStack) + len(self.outStack) == 0
        """
        :rtype: bool
        """
        