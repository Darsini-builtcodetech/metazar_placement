#node class create painanum

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# node create painnurom
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

#10 and 20 c0nnect painrom
node1.next = node2

#20 and 30 connect
node2.next = node3

#30 and 40 connect
node3.next = node4

#25 node create painnura
new_node = Node(25)

#25-a 30-oda connect pannrom
new_node.next = node2.next #node is 20 than node2.next mean 30

#20-a 25-oda connect pannrom
node2.next = new_node

#print linked list
current = node1  #current nu temporary value create painnuro

while current:
    print(current.data, end=" → ")
    current = current.next

print("None")    