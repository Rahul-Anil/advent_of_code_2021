class Node:
    def __init__(self, value=None, depth=None):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.depth = depth


class Tree:
    def __init__(self):
        self.root = None

    def snailNumToTree(self, snailNumber: str) -> None:
        depth = 0
        self.root = Node(None)
        currentNode = self.root
        currentNode.depth = depth

        for v in snailNumber:
            if v == "[":
                newNode = Node(None)
                newNode.parent = currentNode
                currentNode.left = newNode
                depth += 1
                newNode.depth = depth
                currentNode = newNode
            elif v == "]":
                currentNode = currentNode.parent
                depth -= 1
            elif v.isdigit():
                currentNode.value = int(v)
            elif v == ",":
                currentNode = currentNode.parent
                depth -= 1
                newNode = Node(None)
                newNode.parent = currentNode
                currentNode.right = newNode
                depth += 1
                newNode.depth = depth
                currentNode = newNode

    def buildSnailNumber(self, node):
        stack = []
        if node:
            if node.value == None:
                left = self.buildSnailNumber(node.left)
                right = self.buildSnailNumber(node.right)
                stack.append(left)
                stack.append(right)
            else:
                return node.value
        return stack

    def reduce(self):
        pass

    def findLeft(self, curr, leftVal):
        if curr.parent != self.root:
            if curr.parent.left.value != None:
                curr.parent.left.value += leftVal
            else:
                self.findLeft(curr.parent, leftVal)
        else:
            # here do from root search
            return

    def findRight(self, curr, rightVal):
        if curr.parent != self.root:
            if curr.parent.right.value != None:
                curr.parent.right.value += rightVal
            else:
                self.findRight(curr.parent, rightVal)
        else:
            return

    def tryExplode(self, curr):
        if curr:
            self.tryExplode(curr.left)
            if curr.depth == 4 and curr.value == None:
                self.findLeft(curr, curr.left.value)
                self.findRight(curr, curr.right.value)
                print(f"left: {curr.left.value}, right: {curr.right.value}")
                curr.value = 0
                curr.left = None
                curr.right = None
                return
            self.tryExplode(curr.right)
        pass

    def explode(self):
        # move through the tree in (inorder) traversal
        # find an element that is that is of depth 4 first
        # (this should be a node with value as none)
        # find an element that is left to it
        # find an element that is right to it
        # do the addition operations and then remove the excess nodes
        self.tryExplode(self.root)
        self.treeToSnailNumber()
        pass

    def split(self):
        pass

    def treeToSnailNumber(self):
        print(f"Snail Number: {self.buildSnailNumber(self.root)}")

    def treeTraversal(self, curr):
        if curr:
            self.treeTraversal(curr.left)
            print(f"[val: {curr.value} depth: {curr.depth}]", end="")
            self.treeTraversal(curr.right)

    def displayTree(self):
        self.treeTraversal(self.root)
        print(f"\n")


def part1(input: str) -> int:
    snailNumber = input.strip()
    tree = Tree()
    tree.snailNumToTree(snailNumber)
    tree.explode()
    print("\n")


if __name__ == "__main__":
    with open("../tests/sample_inputs/day_18_sample.txt") as f:
        input = f.read()
    print(f"P1: {part1(input)}")
