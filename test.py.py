#1. 두개의 정수 입력받아 합 구하기
'''
def add(a,b):
    a = int(a)
    b = int(b)
    sum = a+b
    return sum

no1, no2 = input("두 수를 입력하세요:").split()
result = add(no1,no2)
print(result)

#2.한개의 정수 입력받아 홀수인지 짝수인지 출력하는 프로그램
def isOdd(num):
    if num % 2 ==0:
       print("짝수입니다")
    else:
        print("홀수입니다")

         
num =int(input("정수 하나를 입력하세요:"))         
isOdd(num)
'''
#. 지역변수 전역변수 출력 결과
a = 9 #서울
def func(n):#제주
    a = n*3 

func(a)
print(a)
#전역변수
a = 9 #서울
def func(n): #복사
    global a #서울-> 제주
    a = n*3

func(a)
print(a)

#4.예외처리
try:
    예외가 발생할수 있는 코드
except:
    발생한 예외에 적절하게 대응할 수 있는 코드