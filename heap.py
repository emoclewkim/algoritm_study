#(max) heap 구현 
'''
1.배열은 인덱스 0부터시작하지만, 힙 구현 편의를 위해 root노드 인덱스 번호를 1로 지정후 구현
2.부모 노드 인덱스 번호 = 자식 노드 인덱스 번호 // 2
    부모 노드 인덱스 번호 *2 = 왼쪽 자식 노드 인덱스 번호
    부모 노드 인덱스 번호 *2 + 1 = 오른쪽 자식 노드 인덱스 번호
'''
class heap:
    def __init__(self,data):
        self.heap_array =list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def change_up(self, index): # 노드를 heap 집어넣었을때 그 노드가 자기 위치에 맞지않으면 부모노드와 자리를 바꿔주는 함수, inser함수안에서 쓰임
        if index <= 1:
            return False
        
        parent = index //2
        if self.heap_array[index] > self.heap_array[parent]:
            self.heap_array[index], self.heap_array[parent] = self.heap_array[parent], self.heap_array[index]
            return True
        else:
            return False
        

    def insert(self, data): # 노드 삽입 함수
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        index = len(self.heap_array) -1 # 삽입하는 노드의 인덱스번호를 알기위함
        
        while self.change_up(index): # 값들이 정렬할때까지 계속 실행
            index = index//2

        return True
    
heap = heap(10)
heap.insert(11)
heap.insert(8)
heap.insert(15)
heap.insert(7)
heap.insert(20)
heap.insert(2)
heap.insert(30)
print(heap.heap_array)
