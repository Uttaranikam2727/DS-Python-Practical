"""GD10 - Binary Search Tree: insert, delete, search, display"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            print("Duplicate key ignored")
        return node

    def search(self, key):
        cur = self.root
        while cur:
            if key == cur.key:
                return True
            cur = cur.left if key < cur.key else cur.right
        return False

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            print("Key not found")
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:            # 0 or 1 child (right)
                return node.right
            if node.right is None:           # 1 child (left)
                return node.left
            succ = node.right                # 2 children: inorder successor
            while succ.left:
                succ = succ.left
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)
        return node

    def inorder(self, n, out):
        if n:
            self.inorder(n.left, out); out.append(n.key); self.inorder(n.right, out)
        return out

    def preorder(self, n, out):
        if n:
            out.append(n.key); self.preorder(n.left, out); self.preorder(n.right, out)
        return out

    def postorder(self, n, out):
        if n:
            self.postorder(n.left, out); self.postorder(n.right, out); out.append(n.key)
        return out

    def display(self):
        if self.root is None:
            print("Tree is empty")
            return
        print("Inorder  :", self.inorder(self.root, []))
        print("Preorder :", self.preorder(self.root, []))
        print("Postorder:", self.postorder(self.root, []))


def main():
    t = BST()
    while True:
        print("\n--- Binary Search Tree ---")
        print("1.Insert  2.Delete  3.Search  4.Display  0.Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            for k in map(int, input("Key(s) to insert (space separated): ").split()):
                t.insert(k)
        elif ch == "2":
            t.delete(int(input("Key to delete: ")))
        elif ch == "3":
            print("Found" if t.search(int(input("Key to search: "))) else "Not found")
        elif ch == "4":
            t.display()
        elif ch == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
