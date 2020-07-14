# 1부터 num까지의 곱이 출력되는 반복문 / 재귀 함수
def multiple(num):
    sum = 1
    for index in range(1,num+1):
        sum = sum * index
    return sum
 
def mul_reculsive(num):
    if num <=1:
        return num
    else:
        return num * mul_reculsive(num-1)

#숫자리스트의 합을 리턴하는 함수
def sumList(list):
    if len(list) <=1:
        return list
    else:
        return list + sumList(list[1:])

#회문(앞으로읽어도 뒤로읽어도 똑같다!) 판별함수 - 재귀함수 와 리스트 슬라이싱을 이용
def palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

'''
1, 정수 n에 대해
2. n이 홀수이면 3 X n + 1 을 하고,
3. n이 짝수이면 n 을 2로 나눕니다.
4. 이렇게 계속 진행해서 n 이 결국 1이 될 때까지 2와 3의 과정을 반복합니다.

예를 들어 n에 3을 넣으면,
3
10
5
16
8
4
2
1
이 됩니다.
이렇게 정수 n을 입력받아, 위 알고리즘에 의해 1이 되는 과정을 모두 출력하는 함수를 작성하세요.
'''
def making_one(n):
    print (n) # 여기 한곳에만 프린트문 넣으면 되는데 if문 각각에 프린트문을 다 넣었다가 수정.

    if n == 1:
        return n 
    elif n%2 == 1:
        return making_one(3*n+1)
    else:
        return making_one(int(n/2)) # 나눗셈을 하면 값이 실수로 변하니까 int로 감싸줌으로써 값이 깔끔하게보이게 수정.

'''
문제: 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지가 있음
1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하시오
'''

def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4    
    
    return func(data -1) + func(data - 2) + func(data - 3)

