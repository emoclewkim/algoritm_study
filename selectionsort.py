import random

sort_list = random.sample(range(100),10)
print(sort_list)

#선택정렬

def SelectSort(list):
        
    for index2 in range(len(list)-1):

        min_index = index2 #한번 반복할때마다 최솟값을 넣어주기 위한 index
                           # min = list[index2] 처음에는 최솟값을 잡아주기위해서 최솟값의 변수와 그 값을 둘다 잡아줬었는데, 인덱스만 있으면 그 값은 필요가없다. 인덱스로 값을 구할수있으니까

        for index in range(index2,len(list)-1):

            if(list[min_index] > list[index+1]): # 계속해서 최솟값과 다른값들을 비교해서 최솟값을 갱신시켜나가야하는데 버블정렬생각하다가 그런건지 자꾸 앞뒤꺼를 계속 비교해서 최솟값을 갱신시켰따
                min_index = index+1

        list[min_index], list[index2] = list[index2], list[min_index] 
    

        
SelectSort(sort_list)
print(sort_list)

      

