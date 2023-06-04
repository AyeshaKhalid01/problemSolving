class MyStack:

    def __init__(self):
        self.q = collections.deque()        

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()
        
    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        if len(self.q)==0:
            return True
        return False