import random

list = random.sample(range(100),10)
print(list)

#오름차순 버블소트
def bubblesort(list):

    for index in range(len(list)-1):
        isSwap = False # 반복문 안에서 교환이 되었는지 안되었는지 확인하는 변수, 반복문이 다 돌기전에 정렬이끝났을경우를 확인
       
        for index2 in range(len(list)-1-index):    
            if(list[index2] > list[index2+1]):
                list[index2] , list[index2+1] = list[index2+1] , list[index2]
                isSwap = True

        if isSwap == False:
            break

bubblesort(list)
print(list)
     
