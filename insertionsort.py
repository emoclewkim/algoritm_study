import random

sort_list = random.sample(range(100),10)
print(sort_list)

#삽입정렬
def insertionsort(list):
    for i in range(len(list)-1): # range를 처음에 len(list) 까지만 했다가 오류남. len(list)-1로 수정 len(list)의 값은 10이다.
        for j in range(i+1,0,-1): 
            if list[j-1] > list[j]:
                list[j-1] , list[j] = list[j] , list[j-1]
            else:
                break
    
insertionsort(sort_list)
print(sort_list)

            
