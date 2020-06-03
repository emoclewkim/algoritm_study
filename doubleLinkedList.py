# Doubly linked list - python  

class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
    
class NodeManage:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else :
            node = self.head
            while node.next:
                node = node.next
            tmp = Node(data)
            node.next= tmp
            tmp.prev = node
            self.tail = tmp
    
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search_head(self,data): #앞에서부터 찾기
        if self.head == None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return True
            else:
                node = node.next
        return False
    
    def search_tail(self, data): # 뒤에서부터 찾기'
        if self.tail == None:
            return False

        node = self.tail
        while node:
            if node.data == data:
                return True
            else:
                node = node.tail
        return False

    def insert_before(self, new_data, data): #특정 데이터앞에 새로운데이터 추가
        if self.head == None:
            self.head = Node(new_data)
            
        else:
            node = self.tail
            while True:
                if node.data == data:
                    break
                node = node.prev
                    
            tmp = Node(new_data) # 새로운 node.prev 객체화
            node_prv = node.prev # 기존 node.prev

            node_prv.next = tmp 
            tmp.prev = node_prv

            node.prev = tmp
            tmp.next = node
            

DLL = NodeManage(0)
for data in range(1,10):
    DLL.insert(data)

DLL.insert_before(22,5)

DLL.desc()
























