import copy


class node():
    def __init__(self, val):
        self.color = "red"
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


class tree():
    def __init__(self):
        self.nil = node(0)
        self.nil.color = "black"
        self.nil.right = None
        self.nil.left = None
        self.root = self.nil

    def insert(self, val):
        nNode = node(val)
        nNode.val = val
        nNode.parent = None
        nNode.right = self.nil
        nNode.left = self.nil
        nNode.color = "red"

        y = None
        x = self.root

        while x != self.nil:
            y = x
            if nNode.val > x.val:
                x = x.right
            else:
                x = x.left
        nNode.parent = y

        if y == None:
            self.root = nNode
        elif nNode.val > y.val:
            y.right = nNode
        else:
            y.left = nNode

        if nNode.parent == None:
            nNode.color = "black"
            return
        if nNode.parent.parent == None:  # 1child is red so no need to fix tree
            return

        self.fixtree(nNode)

    def rot_right(self, N):
        x = N.left
        N.left = x.right
        if x.right != self.nil:
            x.right.parent = N

        x.parent = N.parent
        if N.parent == None:
            self.root = x
        elif N == N.parent.right:
            N.parent.right = x
        else:
            N.parent.left = x

        x.right = N
        N.parent = x

    def rot_left(self, N):
        y = N.right
        N.right = y.left
        if y.left != self.nil:
            y.left.parent = N
        y.parent = N.parent
        if N.parent == None:
            self.root = y
        elif N == N.parent.right:
            N.parent.right = y
        else:
            N.parent.left = y

        y.left = N
        N.parent = y

    def fixtree(self, X):
        while X.parent.color == "red":
            if X.parent == X.parent.parent.right:
                U = X.parent.parent.left
                if U.color == "red":
                    X.parent.parent.color = "red"
                    X.parent.color = "black"
                    U.color = "black"
                    X = X.parent.parent
                else:
                    if X == X.parent.left:  # right left case
                        X = X.parent
                        self.rot_right(X)

                    X.parent.color = "black"  # right right case when last if is false
                    X.parent.parent.color = "red"
                    self.rot_left(X.parent.parent)
            else:
                U = X.parent.parent.right
                if U.color == "red":
                    X.parent.parent.color = "red"
                    X.parent.color = "black"
                    U.color = "black"
                    X = X.parent.parent
                else:
                    if X == X.parent.right:  # left right case
                        X = X.parent
                        self.rot_left(X)

                    X.parent.color = "black"  # left left case when last if is false
                    X.parent.parent.color = "red"
                    self.rot_right(X.parent.parent)
            if X == self.root:
                break
        self.root.color = "black"




    def search(self,root, key):
        if root is None or str(root.val)==key:
            return root
        if str(root.val)<key:
            return self.search(root.right,key)
        if str(root.val)>key:
            return self.search(root.left,key)




    def rbt_height(self, root):  # height according to number of elements along longest path
        if root == self.nil:
            return 0

        else:
            lsth = self.rbt_height(root.left)
            rsth = self.rbt_height(root.right)

        if lsth > rsth:
            return lsth + 1
        else:
            return rsth + 1

    def print_treeheight(self, root):
        h = self.rbt_height(root)
        print("The height of the tree is "+str(h))





    def rbt_size(self, root):
        if root == self.nil:
            return 0
        else:
            r = self.rbt_size(root.right)
            l = self.rbt_size(root.left)
            return r + l + 1

    def print_treesize(self, root):
        s = self.rbt_size(root)
        print("The size of the tree is  "+str(s))




    def load(self, root):
        hand = open("EN-US-Dictionary.txt", "r")
        data = hand.read()
        data = data.split("\n")

        for i in range(len(data)):
            if self.search(root,data[i]) == None and self.search(root,data[i].lower()) == None and self.search(root,data[i].capitalize()) == None and self.search(root,data[i].upper()) == None:
                self.insert(data[i])

        hand.close()




    def lookUp(self,root, key):
        if self.search(root,key) != None or self.search(root,key.lower()) != None or self.search(root,key.capitalize()) != None or self.search(root,key.upper()) != None  :
            print("Yes,word is in dictionary")
        else:
            print("No,word isn't in the dictionary")



    def insert_word(self, word, root):
        if self.search(root,word) == None and self.search(root,word.lower()) == None and self.search(root,word.capitalize()) == None and self.search(root,word.upper()) == None:
            self.insert(word)
            print("Word ("+word+") inserted successfully!")
            self.print_treesize(root)
            self.print_treeheight(root)
        else:
            print("Word already in dictionary!")



t1 = tree()

while True:

    print("\n")
    print("Welcome to the English Dictionary!")
    opt = input("Enter 0:Exit 1:load 2:Print Dictionary Size 3:Insert word 4:Lookup a word:\n")
    if opt == "1":
        t1.load(t1.root)
        print("Dictionary loaded successfully")

    elif opt == "2":
        t1.print_treesize(t1.root)

    elif opt == "3":
        x = input("Enter word U want to add: ")
        t1.insert_word(x, t1.root)

    elif opt == "4":
        y = str(input("Enter word to Look Up for: "))
        t1.lookUp(t1.root,y)

    elif opt == "0":
        print("Thanks for using English dictionary!")
        break








