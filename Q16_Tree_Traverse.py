class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data <= self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def left_traverse(self):
        l = []
        if self.data is None:
            return
        if self.left:
            l = l + self.left.left_traverse()
        l = l + [self.data]
        if self.right:
            l = l + self.right.left_traverse()
        return l


root = Node(9)

for i in range(5, 17, 3):
    root.insert(i)
for i in range(3, 20, 2):
    root.insert(i)

print(root.left_traverse())
