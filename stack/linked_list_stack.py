class Node:
    def __init__(self,data=None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print('Stack is empty')
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += ' -->' + str(itr.data) 
            itr = itr.next
        print(llstr)

    def push_stack(self,data):
        node = Node(data,self.head)
        self.head = node

    def pop_stack(self):
        if self.head is None:
            print('Stack is empty')
            return
        self.head = self.head.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.push_stack(10)
    ll.push_stack(20)
    ll.push_stack(30)
    ll.print()     
    ll.pop_stack()
    ll.print()  
    ll.pop_stack() 
    ll.print()                    