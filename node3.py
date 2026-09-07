class Node:
    def __init__(self, data):             #Node create pannumbodhu, oru value receive pannum. 
        self.data = data
        self.next = None                  #next node connect pannala.initally NONE is denoted

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

target = 20  #20 valu va search painnuro

#First node-la search start pannrom
current = node1    #current first node-a point pannum.

found = False


while current:                  #current-la node irukkura varaikkum search pannu.
    #loop start
    if current.data == target:     #check 10==30?
        print("Found")
        found = True
        break
    current = current.next

if not found :
    print("Not Found")    


