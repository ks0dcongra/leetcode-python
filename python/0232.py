class MyQueue:

    def __init__(self):
        self.stack1 = []  # 用於入隊
        self.stack2 = []  # 用於出隊

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self._move_elements_if_necessary()
        return self.stack2.pop() 

    def peek(self) -> int:
        self._move_elements_if_necessary()
        return self.stack2[len(self.stack2)-1] 

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

    def _move_elements_if_necessary(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())