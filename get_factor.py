#1.create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

#2.Get the height
    def get_height(node):  #what is the node height to find and create a function |get_name=function name
        if node is None:
            return 0

        return node.height    

#3.Calculate Balance Factor
    def get_balance(node):
        if node is None:
            return 0

        return get_height(node.left) - get_height(node.right)

#3.create nodes        
root = Node(30)
root.left = Node(20)
root.right = Node(40)

#5.calculate balance factor 

balance = get_balance(root)
print("Balance Factor:", balance)