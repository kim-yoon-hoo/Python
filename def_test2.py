# 전역변수 지역변수
# 변수
'''
price = 1000
def sale():
    global price 
    price = 500


sale()
print(price)


#홀짝을 구하는 함수

def is0dd():
    global num
    if num % 2==0:
        print("짝수")
    else:
        print("홀수")

num = int(input("정수 하나 입력:"))
'''
#107
import random

n = random.randint(1,6)
n = random.randint(1,6)
print("결과1:",n)
print("결과2:",n)











