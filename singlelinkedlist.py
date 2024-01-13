class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llitr = ''
        while itr:
            llitr += str(itr.data) + ' ---> ' 
            itr = itr.next
        print(llitr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count   
    
    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next            
        itr.next = Node(data,None)

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1  

    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def remove_data(self,data):
        if self.head is None:
            print("Linked List is empty")
            return
        if data == self.head.data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if data == itr.next.data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)






if __name__ == '__main__':
    ll = LinkedList()
    ll.print()  
    print(ll.get_length())     
    ll.insert_at_begining(10) 
    ll.insert_at_begining(20)
    ll.insert_at_begining(30) 
    ll.print()  
    print(ll.get_length())     
    ll.insert_at_end(9)
    ll.print()                  
    ll.insert_at(2,100)
    ll.print()
    ll.remove_at(2)
    ll.print()
    ll.insert_values([1,2,3,4,5])
    ll.print()
    ll.remove_data(5)
    ll.print()