class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._queue = None
        if self._queue == None:
            self._queue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self._queue.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self._queue:
            del self._queue[0]
        

    def peek(self):
        """
        :rtype: int
        """
        if self._queue:
            a = self._queue[0]
            return a

    def empty(self):
        """
        :rtype: bool
        """
        return self._queue == []

q = Queue()
q.push(1)
print(q.peek())