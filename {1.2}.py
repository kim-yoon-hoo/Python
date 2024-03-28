print('A')
print('B')
print('C')

#주석처리.

print('안녕하세요') #인사코드

#print('불필요한 코드')

print('필요한 코드')

print('A')

'''
여러줄의
주석을
처리하는
방법입니다.

'''
#드려쓰기.

n=10

if n%2==0:
    print('even')
    print('짝수')
else:
    print('odd')
    print('홀수')
#변수 #변수는 이름이 필요함.
#변수 값은 언제든지 변경가능함.
#첫글자는 영어 또는 언더바로 시작할수있다.
#대소문자 구분 a와A는 서로 다른 문자이다.
a=10
b=5
print('a')
print(a)
print(a+b)
b=7
print(a+b)

#함수

#함수 이름(인자 값)--> 리턴 값
#print 표준 출력
#input 입력

name=input('이름을 입력해주세요.')

print('안녕하세요,',name)
