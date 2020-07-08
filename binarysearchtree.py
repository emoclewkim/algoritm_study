#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##binary search tree


# In[1]:


#binary search tree에쓰일 노드클래스 정의 
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# In[ ]:


#트리 정의
class NodeMgmt:
    def __init__(self,head):
        self.head = head
    
    #노드 삽입
    def insert(self,value):
        self.current = self.head
        while True:
            if value < self.current.value:
                if self.current.left !=None:
                    self.current = self.current.left
                else:
                    self.current.left = Node(value)
                    break
            else:
                if self.current.right !=None:
                    self.current = self.current.right
                else:
                    self.current.right= Node(value)
                    break 
     #노드 탐색
    def search(self,node):
        self.current = self.head
        while self.current:
            if node == self.current.value:
                return True
            elif node < self.current.value:
                self.current = self.current.left
            else:
                self.current = self.current.right
        return False
    
    #노드 삭제( 삭제할 노드가 무조건 존재한다고 가정)
    def delete(self,node):
        self.current = self.head
        self.parent = self.head
        
       # self.current 와 self.parent 지정
        while self.current:
            if self.current.value == node:
                break
            elif node < self.current.value:
                self.parent = self.current
                self.current = self.current.left
            else:
                self.parent = self.current
                self.current = self.current.right
        
        #  삭제하려는 노드가 leaf노드일경우
        if self.current.left == None and self.current.right == None:
            if node < self.parent.value:
                self.parent.left =None
            else:
                self.parent.right =None
            del self.current
        # 삭제하려는 노드가 childNode를 한개 가지고 있을 경우
        if self.current.left !=None and self.current.right == None:
            if node < self.parent.value:
                self.parent.left = self.current.left
            else:
                self.parent.right = self.current.left
        elif self.current.left ==None and self.current.right != None:
            if node < self.parent.value:
                self.parent.left = self.current.right
            else:
                self.parent.left = self.current.right
                
        # 삭제하려는 노드가 childNode를 두개 가지고 있을 경우
        if self.current.left !=None and self.current.right != None: 
            if node < self.parent.value: #삭제할 노드가 parentnode 왼쪽에 있을때
                self.change = self.current.right
                self.change.parent = self.current.right
                while self.change.left != None:
                    self.change.parent = self.change
                    self.change = self.change.left
                if self.change.right !=None:
                    self.change.parent.left = self.change.right
                else:
                    self.change.parent.left = None
                self.parent.left = self.change
                self.change.right = self.current.right
                self.change.left = self.current.left
                
            else: # 삭제할 노드가 parentnode 오른쪽에 있을때
                self.change = self.current.right
                self.change.parent = self.current.right
                while self.change.left != None:
                    self.change.parent = self.change
                    self.change = self.change.left
                if self.change.right !=None:
                    self.change.parent.left = self.change.right
                else:
                    self.change.parent.left = None
                self.parent.left = self.change
                self.change.right = self.current.right
                self.change.left = self.current.left
                
        return True
        
    
        


# In[ ]:


node = Node(1)
bst = NodeMgmt(node)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(5)

print(bst.search(3))
print(bst.search(-1))


# In[ ]:


#파이썬 전체코드 테스트
# 0 ~ 999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제
import random

# 0 ~ 999 중, 100 개의 숫자 랜덤 선택
bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))
# print (bst_nums)

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)
    
# 입력한 100개의 숫자 검색 (검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print ('search failed', num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)


# In[ ]:




