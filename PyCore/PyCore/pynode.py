class Node:

    #function to initialize node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    #initializes head
    def __init__ (self):
        self.head = None
        
    #inserts new node at beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Given reference to head of a list and a key
    # delete first occurence of key in linked list
    def deleteNode(self, key):
        temp = self.head

        #If head node itself holds key to delete
        if (temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp = None
                return
        #traverse list, if key found
        #break and 
        while(temp is not None):
            if temp.data == key:
                break
            prev=temp
            temp=temp.next

        #key is not present
        if (temp==None):
            print("\nkey not present")
            return
        prev.next = temp.next

        temp = None

    def printList(self):
        temp=self.head
        while(temp):
            print("%d" %(temp.data)),
            temp = temp.next

# Driver program  
llist = LinkedList()  
llist.push(7)  
llist.push(1)  
llist.push(3)  
llist.push(2)  
  
print ("Created Linked List: ") 
llist.printList()  
llist.deleteNode(1)  
print ("\nLinked List after Deletion of 1:")
llist.printList() 
print("\nattempting to delete the number 42:")
llist.deleteNode(42)
llist.printList()  
