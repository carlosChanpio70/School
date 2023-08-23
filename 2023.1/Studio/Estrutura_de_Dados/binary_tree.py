class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)


root = None
for i in [-50,54,71,19,100]:
    root = insert(root, i)

for i in [22, 63, 54, 71, 19, 37]:
    if search(root, i) != None:
        print(f"{i} está no vetor")
    else:
        print(f"{i} não está no vetor")