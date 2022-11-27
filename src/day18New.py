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
        print(f"left: {node.left.value}, right: {node.right.value}")

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

        self.treeToSnailNumber()

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
    tree.treeToSnailNumber()
    tree.explode()
    print("\n")


if __name__ == "__main__":
    with open("../tests/sample_inputs/day_18_sample.txt") as f:
        input = f.read()
    print(f"P1: {part1(input)}")
