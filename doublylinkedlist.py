class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print('List is empty')
            return
        itr =self.head             
        dlstr = ''
        while itr:
            dlstr += str(itr.data) + ' --> ' 
            itr = itr.next
        print('forward:',dlstr)    

    def print_reverse(self):
        if self.head is None:
            print('list is empty')
            return
        last_node = self.get_last_node()
        itr = last_node
        dlstr = ''
        while itr:
            dlstr += str(itr.data) + ' --> '
            itr = itr.prev
        print('reverse:',dlstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr        

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at_beginiing(self,data):
        if self.head is None:
            new_node = Node(data,self.head,None)
            self.head = new_node
        else:
            new_node = Node(data,self.head,None)   
            self.head.prev = new_node
            self.head = new_node 

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next =  Node(data,None,itr)   

    def insert_at(self,index,data):
        if index <0 or index >self.get_length():
            raise Exception('invalid index')
        if index == 0:
            self.insert_at_beginiing(data)
            return
        count  = 0
        itr = self.head
        while itr:
            if count == index - 1:
                new_node = Node(data, itr.next, itr)
                if new_node.next:
                    new_node.next.prev = new_node
                itr.next = new_node
                break
            itr = itr.next
            count += 1  

    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next  = itr.next
                if itr.next:
                    itr.next.prev =  itr.prev
                break
            itr = itr.next
            count += 1

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



if __name__ == '__main__':
    ll = DoublyLinkedList() 
    ll.print_forward() 
    print(ll.get_length())
    ll.insert_at_beginiing(10) 
    ll.insert_at_beginiing(20) 
    ll.insert_at_end(40)
    ll.insert_at(2,30)
    ll.print_forward() 
    ll.print_reverse()  
    ll.remove_at(2)
    ll.print_forward()   
    ll.print_reverse() 
    ll.insert_values([1,2,3,4]) 
    ll.print_forward()