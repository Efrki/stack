class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        removed = self.stack.pop()
        return removed
        
    def is_empty(self):
        if len(self.stack) != 0:
            return True
        else:
            return False
#Доделать