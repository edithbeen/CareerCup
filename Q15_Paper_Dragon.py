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

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def traverse(self):
        if self.data is None:
            return
        if self.left:
            self.left.traverse()
        print(self.data)
        if self.right:
            self.right.traverse()


root = Node(8)

for i in range(15):
    root.insert(i)

root.traverse()
