class Stack(object):
    def __init__(self):
        self.queueIn = []
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        self.queueIn.append(x)
        """
        :type x: int
        :rtype: nothing
        """
        

    def pop(self):
        for i in range(len(self.queueIn) - 1):
            self.queueIn.append(self.queueIn.pop(0))
        return self.queueIn.pop(0)
            
        """
        :rtype: nothing
        """
        

    def top(self):
        top = None
        for i in range(len(self.queueIn)):
            top = self.queueIn.pop(0)
            self.queueIn.append(top)
        return top
        
        
        """
        :rtype: int
        """
        

    def empty(self):
        return self.queueIn == []
        """
        :rtype: bool
        """
        