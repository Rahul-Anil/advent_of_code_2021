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
        reduceOp = True
        xplodeCount = 0
        splitCount = 0

        while reduceOp:
            reduceOp = self.explode()
            xplodeCount += 1
            print(f"xplode {xplodeCount}")
            self.treeToSnailNumber()

            if not reduceOp:
                reduceOp = self.split()
                splitCount += 1
                print(f"split: {splitCount}")
                self.treeToSnailNumber()

    def findExplode(self, node):
        s = [node]

        while s:
            curr = s.pop()
            if curr.value == None and curr.depth == 4:
                return curr
            else:
                if curr.right:
                    s.append(curr.right)
                if curr.left:
                    s.append(curr.left)

        return None

    def findLeftExplode(self, node):
        s = [node]

        while s:
            curr = s.pop()
            if curr.parent.left.value != None:
                return curr.parent.left
            else:
                if curr.parent != self.root:
                    s.append(curr.parent)

        if self.root.left != curr:
            rs = [self.root.left]

            while rs:
                curr = rs.pop()

                if curr.value != None:
                    return curr
                else:
                    if curr.left:
                        rs.append(curr.left)

                    if curr.right:
                        rs.append(curr.right)

        return None

    def findRightExplode(self, node):
        s = [node]

        while s:
            curr = s.pop()
            if curr.parent.right.value != None:
                return curr.parent.right
            else:
                if curr.parent != self.root:
                    s.append(curr.parent)

        if self.root.right != curr:
            rs = [self.root.right]

            while rs:
                curr = rs.pop()

                if curr.value != None:
                    return curr
                else:
                    if curr.right:
                        rs.append(curr.right)

                    if curr.left:
                        rs.append(curr.left)
        return None

    def explode(self):
        node = self.findExplode(self.root)
        # print(f"left: {node.left.value}, right: {node.right.value}")
        if node == None:
            return False

        leftNode = self.findLeftExplode(node)
        rightNode = self.findRightExplode(node)

        if leftNode != None:
            # print("HL")
            leftNode.value += node.left.value

        if rightNode != None:
            # print("HR")
            rightNode.value += node.right.value

        node.value = 0
        node.left = None
        node.right = None

        return True

    def findSplit(self, node):
        s = [node]

        while s:
            curr = s.pop()
            if curr.value != None:
                if curr.value >= 10:
                    return curr
            else:
                if curr.right:
                    s.append(curr.right)
                if curr.left:
                    s.append(curr.left)

        return None

    def split(self):
        node = self.findSplit(self.root)
        # print(f"node: {node.value}")

        if node == None:
            return False

        splitVal = node.value
        spV1 = splitVal // 2
        spV2 = splitVal - spV1
        newDepth = node.depth + 1

        node.value = None
        leftNode = Node(spV1, newDepth)
        rightNode = Node(spV2, newDepth)

        node.left = leftNode
        node.right = rightNode

        return True

    def increaseDepthOfAllNodes(self, curr):
        if curr:
            self.increaseDepthOfAllNodes(curr.left)
            curr.depth += 1
            self.increaseDepthOfAllNodes(curr.right)

    def snailNumberAddition(self, snailNumber):
        newTree = Tree()
        newTree.snailNumToTree(snailNumber)
        newTree.reduce()
        newRoot = Node(None, 0)
        newRoot.left = self.root
        newRoot.right = newTree.root
        self.root = newRoot
        self.increaseDepthOfAllNodes(self.root)
        self.reduce()

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

    def snailNumberMagnitude(self) -> int:
        self.magnitude(self.root.left)
        self.magnitude(self.root.right)
        return 3 * self.root.left.value + 2 * self.root.right.value

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
    snailNumber = input.strip().splitlines()
    # print(f"{snailNumber}")

    tree = Tree()
    tree.snailNumToTree(snailNumber.pop(0))
    # tree.split()
    # tree.explode()
    tree.reduce()
    tree.treeToSnailNumber()
    # tree.snailNumberAddition("[[[5,[2,8]],4],[5,[[9,9],0]]]")


if __name__ == "__main__":
    with open("../tests/sample_inputs/day_18_sample.txt") as f:
        input = f.read()
    print(f"P1: {part1(input)}")

# [[[[5, 0], [9, 0]], [[5, 0], [5, 7]]], [[[0, 8], [[5, 6], 12]], [14, [0, 9]]]]
