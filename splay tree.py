class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
    
    def equals(self, node):
        return self.key == node.key


class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None)


    def insert(self, key):
        if (self.root == None):
            self.root = Node(key)
        return

    self.splay(key)
    n = Node(key)
    if key < self.root.key:
        n.left = self.root.left
        n.right = self.root
        self.root.left = None

    else:
        n.right = self.root.right
        n.left = self.root
        self.root.right = None
        self.root = n


    def remove(self, key):
        self.splay(key)
        if key != self.root.key:
            print(f"Word '{key}' not found in Splay Tree and thus cannot be deleted.\n")
        elif self.root.left == None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x
            print(f"Word '{key}' deleted.\n")
            def findMin(self):
                if self.root == None:
                    return None
            x = self.root
            while x.left != None:
                x = x.left
                self.splay(x.key)
                return x.key

    def findMax(self):
        if self.root == None:
            return None
        x = self.root
        while (x.right != None):
            x = x.right
            self.splay(x.key)
            return x.key


    def find(self, key):
        if self.root == None:
            print("Splay Tree is Empty!\n")
            self.splay(key)
        if self.root.key != key:
            print(f"Word {key} not found in Splay Tree.")
            print(f"Word {key} found in Splay Tree.")
    
    def isEmpty(self):
        return self.root == None

    def splay(self, key):
        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y

            if t.left == None:
                break
                r.left = t
                r = t
                t = t.left


            elif key > t.key:
                if t.right == None:
                    break

            if key > t.right.key:
                y = t.right
                t.right = y.left
                y.left = t
                t = y

            if t.right == None:
                break
                l.right = t
                l = t
                t = t.right
    
            else:
                break
            l.right = t.left
            r.left = t.right
            t.left = self.header.right
            t.right = self.header.left
            self.root = t
    
    def preorder(self):
        if self.root is not None:
            print(self.root.key)
            self.preorder(self.root.left)
            self.preorder(self.root.right)


if __name__ == '__main__':
    rbtree = SplayTree()
    while True:
        print("\nOptions: 1. Insert 2. Delete 3. Search 4. Exit ")
        opt = int(input("Enter Option: "))
        if opt == 1:
            key = input("Enter data to be inserted: ")
            rbtree.insert(key)
        elif opt == 2:
            key = input("Enter data to be deleted: ")
            rbtree.remove(key)
        elif opt == 3:
            key = input("Enter data to be searched: ")
            rbtree.find(key)
        elif opt == 4:
            exit(0)
        else:
            print("Wrong Choice Entered.\n")
