#for ii in range(1,101):
    #print(i)


'''
i = 1
while i <= 100:
    print(i)
    i += 1 # i = i+1


while i <= 5:
    print(i)
    i += 1 # i = i+1

n = 1
while n <= 13:
    print("파이썬 최고!!")
    n += 1
'''

i = 1
while i <= 100:
    if i % 5 == 0:
       print(i) #다음줄로 넘기지 않고 출력
    else:
       print(i, end=' ') #10단위마다 다음줄로 넘긴다
    
    i += 1

# 두개의 정수를 입력받아 더하여 출력하는 프로그램
#(첫번쨰 값 두번쨰 값)
#두 값 모두 0이 입력되었을때 종료 하도록 하세요 break
while True:
   print("두개의 정수값을 입력하세요")
   num1 = int(input("첫 번째 정수 값:"))
   num2 = int(input("두 번째 정수 값:"))
   print(f"두수의 합은 {num1+num2} 입니다")
   if num1==0 and num2 == 0: #무한 반복문에 탈출조건
      break
   
'''
x = 3
while x <6:
    print(x)
    x += 1

echo = input()
hello

while echo != "exit":
    print(echo)
    echo = input()

echo = input()
hello
    while True:
    if echo == "exit":
       break
    print(echo)
    echo = input()
'''