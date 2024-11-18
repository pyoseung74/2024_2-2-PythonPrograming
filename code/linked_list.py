class Node:
    def __init__(self,data):
        self.next = None
        self.data = data



def display(head):
    ptr = head
    while ptr:
        print(ptr.data, "==>")
        ptr = ptr.next
        if ptr == None:
            print(end=" ")
        else:
            print(" ==> ", end = "")
        ptr = ptr.next
    print()
    
def append_data(head): # report : insert data using sorting
    input_data = int(input("Data: "))
    new_data = Node(input_data)
    #print(new_data.data, new_data.next)
    if head == None:
        head = new_data
        return
    else:
        ptr = head
        while ptr:
            if ptr.next == None:
                ptr.next = new_data
                return head
            else:
                ptr = ptr.next

head = None

while True:
    print(1.)
