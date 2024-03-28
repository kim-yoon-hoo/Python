#정수형 (int) 연산이 가능하다.

 
# (str) 다른 언어와 달리 문자와 문자열을 따로 구분하지 않는다.
#"또는 ""에 감싸져 있다.
#연산이 불가능하다,(예외: 문자+문자, 문자*정수)

a=5
b='5'
c=5.0
'''
print(a+a) # int+int
print(b+b) # str+str
print(a+b) # inf+str

'''
print(a+b) # int+ str
print(b*c) # str* float

#숫자와 문자는 더하는게 안됌
#실수는 문자와 곱하기가 안됌

#리스트 list 데이터를 순차적으로 저장> 열거형
#튜플 tuple 값을 변경할 수 없는 열거형 집합
#세트 set 순서가 없고 중복이 허용되지 않는 집합
#사전 dictionary 키와 값의 쌍으로 구성된 집합

#자료형 변환 (typecasting) 방법: 원하는 자료형 함수에 값을 넣는다.
#ex) str(10), int('10'), int(12.5), list('hello') 등

b=int(input('숫자를 입력하세요'))

print(b+b)

#실수<->정수
num=5.0
range(num)

range(int(num))
