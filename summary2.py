#1학기 총정리
'''
1. 예약어(키워드) p27
False True  and or not if elif else
for in while break import

import 특정 모듈을 나의 파이썬 프로그램에 포함시키는 명령어
ex) import turtle     p29

2.변수 P38
데이터를 담는 장소 
의미있는 단어로 이름을 짓는다 
동적타이핑:실행중에 동적으로 자료형이 결정
예약어를 변수명으로 쓸수 없다
첫 번째 문자에는 숫자가 올 수 없다
공백 쓸수없다
밑줄문자(_) 쓸 수 있다 
대소문자 구분 한다

주석: 프로그램의 실행과 상관없는 설명을 적을때 사용
 # 한줄주석 
  '''''' """""" 여러줄주석
  
4. 연산자 p37
산술 연산자 p37
 // 나눗셈의 몫
 %  나머지 구하기
비교 연산자 p60
> >= < <= == !=
논리 연산자 p60
and(모두다 참이면 참)
or(둘중 하나만 참이어도 참) 
not(반대로 바꿔준다)

#5. 문자열 슬라이싱
school = "인평자동차고등학교"
print(school[0:5]) #인평자동차

#6.input() 함수 : 키보드로부터 값을 입력 문자로 입력됨
i =input() #10
j =inpur() #20
print(i+j) #30 x => 1020

i =int(input()) #10 캐스트 연산자로 형변환 필요
j =int(input()) #20 
print(i+j) #30

#7.컨테이너 변수 (여러개의 값을 담을수 있는 변수)
# 리스트 튜플 딕서너리 셋

#리스트 [] 튜플 () 딕셔너리 {}

#8.리스트 변수 인덱싱

name = ["유우진","심승호","서정민","서예찬"]
print(name[3]) #서예찬
print(name[1:3]) #심승호 서정민
print(name[0:2]) #유우진 심승호

#리스트변수 요소 추가 삭제
num = [1,2,3,4,5]
num.append(6) #=> [1,2,3,4,5,6] append() 추가
num.insert(3,9) #=> [1,2,3,9,4,5,6] insert () 삽입
num.remove(5) #=> [1,2,3,9,4,6] remove 값 제거
num.extend([10,11]) #=> [1,2,3,9,4,6,10,11] 추가

#9. 키보드 로 부터 정수 입력받아 홀짝판별 

n=int(input("정수 하나 입력:"))
               
if n % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

#10. 구구단 출력 

for i in range(2,10):  #단 2 3 4 5 6 7 8 9 8바퀴
    for j in range(1,10): #곱해지는 수 2*1 2*2 ...2*9 9바퀴
        print(str(i) +"*"+ str(j) +"="+ str (i*j))

        print(f"{i} * {j} = {i*j}")

#11. while반복문 (수행평가)
i=0
while True:
    i = i+1
    if i >= 3:
        print(i)
        break

#함수의 개념
1. 연광성 있는 코드를 묶어놓은 것
2. 여러번 사용할 것을 고려하여 만든 코드 조각(재사용)
3. 실제 코드를 모아서 이름 붙여놓고 이름을 호출(call)하여 사용
4. 실행 결과를 호출한 쪽에 돌려줄 수 있으며 돌려줄 수 있으면 이렇게 돌려주는 값을 리턴 값(return value) 또는 반환 값이라 한다.
5. 인수(인자), 매개변수, 리턴값 
6. def 명령어로 정의한다(만들어준다)

def hello(name):
    print("안녕하세여")
    print("인평자동차고")
    print(name, "입니다")


hello('김윤후')
hello('윈터')
hello('카리나')


# 두 수를 더하는 계산기를 함수로 구현
def add_num(num1, num2):
    n = num1+num2
    return n

add_result = add_num(7,9)
print(add_result)
add_result = add_num(10,5)
print(add_result)
add_result = add_num(8,6)
print(add_result)
'''

#13. 표준 함수 (내장 함수) 
#abs()- 절댓값 bin()- 2진수 oct()- 8진수 hex()- 16진수
#max() min() sum() pow()-거듭제곱
#round() - 반올림

print(abs(10)) #절댓값
print(abs(-10))

print(bin(16)) #2진수
print(oct(16)) #8진수
print(hex(16)) #16진수

numbers = [1,5,-2,0,6]
print(max(numbers)) #최댓값
print(min(numbers)) #최솟값
print(sum(numbers)) #합

print(pow(10,2)) #거듭제곱

pi = 3.14152
print(round(pi,3))