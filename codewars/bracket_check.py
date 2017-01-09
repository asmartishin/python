class BracketsStack:
    def __init__(self):
        self.curly, self.square, self.round = 0, 0, 0
        self.right = True
        self.prev = []
        self.prev_dict = {'{': '}', '[': ']', '(': ')'}

    def push(self, item):
        if item is '{':
            self.curly += 1
            self.prev.append(item)
        elif item is '[':
            self.square += 1
            self.prev.append(item)
        elif item is '(':
            self.round += 1
            self.prev.append(item)
        elif item is '}':
            if self.prev:
                if item is self.prev_dict[self.prev.pop()]:
                    self.curly -= 1
                else:
                    self.right = False
            else:
                self.right = False

        elif item is ']':
            if self.prev:
                if item is self.prev_dict[self.prev.pop()]:
                    self.square -= 1
                else:
                    self.right = False
            else:
                self.right = False

        elif item is ')':
            if self.prev:
                if item is self.prev_dict[self.prev.pop()]:
                    self.round -= 1
                else:
                    self.right = False
            else:
                self.right = False

    def check(self):
        if self.curly == 0 and self.square == 0 and self.round == 0 and self.right:
            return True
        else:
            return False


def group_check(s):
    stack = BracketsStack()
    for i in s:
        stack.push(i)
    return stack.check()

print(group_check('({(())})'))