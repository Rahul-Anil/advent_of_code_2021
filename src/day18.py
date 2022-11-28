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
                if currentNode.value != None:
                    currentVal = str(currentNode.value)
                    newVal = currentVal + v
                    currentNode.value = int(newVal)
                else:
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
        """Used in converting tree to snail number fn"""
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

    def reduce(self):
        reduceOp = True
        while reduceOp:
            reduceOp = self.explode(self.root)

            if reduceOp != True:
                reduceOp = self.split()

    def addRight(self, node, val):
        if node == None:
            return

        if node.value != None:
            node.value += val
            return
        else:
            self.addRight(node.right, val)

    def addLeft(self, node, val):
        if node == None:
            return

        if node.value != None:
            node.value += val
            return
        else:
            self.addLeft(node.left, val)

    def explode(self, curr, l=None, r=None):
        # base case
        if curr.value != None:
            return False

        if curr.depth == 4 and curr.left.value != None and curr.right.value != None:
            self.addRight(l, curr.left.value)
            self.addLeft(r, curr.right.value)
            curr.value = 0
            curr.left = None
            curr.right = None
            return True

        return self.explode(curr.left, l, curr.right) or self.explode(
            curr.right, curr.left, r
        )

    def findSplit(self):
        s = [self.root]

        while s:
            curr = s.pop()
            if curr.value != None and curr.value >= 10:
                return curr
            else:
                if curr.right:
                    s.append(curr.right)
                if curr.left:
                    s.append(curr.left)

        return None

    def split(self):
        nodeToSplit = self.findSplit()

        if nodeToSplit == None:
            return False

        splitVal = nodeToSplit.value
        newNodeDepth = nodeToSplit.depth + 1

        s1 = splitVal // 2
        s2 = splitVal - s1
        assert s1 + s2 == splitVal

        # create new Nodes
        lNode = Node(s1, newNodeDepth)
        rNode = Node(s2, newNodeDepth)

        # parent to child links
        nodeToSplit.left = lNode
        nodeToSplit.right = rNode

        # child to parent links
        lNode.parent = nodeToSplit
        rNode.parent = nodeToSplit

        # parent val to None
        nodeToSplit.value = None

        return True

    def pushDown(self, curr):
        if curr:
            curr.depth += 1
            self.pushDown(curr.left)
            self.pushDown(curr.right)

    def treeAdd(self, snailNumber):
        # reduce my current tree
        self.reduce()

        # create new tree
        newTree = Tree()
        newTree.snailNumToTree(snailNumber)

        # reduce new tree
        newTree.reduce()

        # increment depth values in both nodes
        self.pushDown(self.root)
        newTree.pushDown(newTree.root)
        assert self.root.depth == 1
        assert newTree.root.depth == 1

        # create new root node
        bigRoot = Node(None, 0)
        assert bigRoot.depth == 0

        # new root child old roots
        bigRoot.left = self.root
        bigRoot.right = newTree.root

        # old roots parent new root
        self.root.parent = bigRoot
        newTree.root.parent = bigRoot

        # tree root to big root
        self.root = bigRoot

    def magnitude(self, curr):
        if curr.value != None:
            return curr.value
        elif curr.left.value != None and curr.right.value != None:
            curr.value = 3 * curr.left.value + 2 * curr.right.value
            curr.left = None
            curr.right = None
            if curr.parent != self.root:
                self.magnitude(curr.parent)
            # need to start walking back up
        else:
            if curr.left:
                self.magnitude(curr.left)
            if curr.right:
                self.magnitude(curr.right)

    def treeMag(self):
        self.magnitude(self.root)
        return self.root.left.value * 3 + self.root.right.value * 2


def part1(input: str) -> int:
    snailNumber = input.strip().splitlines()

    tree = Tree()
    tree.snailNumToTree(snailNumber.pop(0))
    for sn in snailNumber:
        tree.treeAdd(sn)
    tree.reduce()
    tree.treeToSnailNumber()

    return tree.treeMag()


def part1Testing(input: str):
    snailNumber = input.strip().splitlines()

    tree = Tree()
    tree.snailNumToTree(snailNumber.pop(0))
    tree.treeToSnailNumber()
    tree.reduce()
    # tree.explode(tree.root)
    tree.treeToSnailNumber()


if __name__ == "__main__":
    with open("../tests/sample_inputs/day_18_sample.txt") as f:
        input = f.read()
    print(f"P1: {part1(input)}")
    # part1Testing(input)
