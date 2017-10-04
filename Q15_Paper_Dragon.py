# given a paper stick, fold n times from right to left, find the valleys and peaks

# let's assume valley is 0 and peak is 1, we use a list to show them

# recursive method
def find_vp(n):
    # pre-requisites check
    if n == 1:
        return [0]
    else:
        temp = find_vp(n-1)
        l = []
        for i in range(len(temp)):
            if i%2 == 0:
                l += [0, temp[i], 1]
            else:
                l += [temp[i]]
        return l

print(find_vp(4))


# binary tree method
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self):
        if self.data is not None:
            if self.left:
                self.left.insert()
            else:
                self.left = Node(0)
            if self.right:
                self.right.insert()
            else:
                self.right = Node(1)
        else:
            print('root node is invalid')

    def traverse(self):
        l = []
        if self.data is None:
            return
        if self.left:
            l = l + self.left.traverse()
        l = l + [self.data]
        if self.right:
            l = l + self.right.traverse()
        return l


root = Node(0)
for i in range(3):
    root.insert()

print(root.traverse())
