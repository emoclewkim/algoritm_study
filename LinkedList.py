# Linked list - python

class Node: # 클래스 노드 정의
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeManage:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self,data): # 링크드리스트 데이터 더하기
        node = self.head
        while node.next :
            node = node.next
        node.next = Node(data)

    def desc(self): # 링크드리스트 전체데이터 출력
        node = self.head
        while node:
            print(node.data)
            node= node.next

    def delete(self,data):
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    break
                else:
                    node = node.next

    def search_node(self,data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next

'''
    def insert(self,data,index): #링크드리스트 중간에 데이터 집어넣기
        node = self.head
        tmp_node = self.add(data)

        for i in range(1,index) :
            node = node.next
        
        tmp = node.next
        node.next = tmp_node
        tmp_node.next = tmp 

'''


node = NodeManage(1) # 인스턴스 생성

for index in range(2,10):
    node.add(index) #링크드리스트 2~9까지 더하기

node.delete(9) # 9번노드 삭제하기

node.desc() # 링크드리스트 데이터 출력하기








