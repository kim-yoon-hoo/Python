#실수형 (float) 숫자를 다루는 내장함수들 사용 가능
#복소수 complex 등등 ex) round(), range(), pow() 등
# (a+b a더하기b) (a-b a빼기b) (a*b a 곱하기 b) (a/b a 나누기 b)
#(a//b a를 b로 나눈 몫) (a%b a를 b로 나눈 나머지) (a**b a의 b제곱)

#int
a=10
b=5
#float
c=2.0
d=0.5

#나누기는 정수와 정수를 나누었을때 float 형태로 나올수있다.

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# (x or y) x나 y 둘 중 하나만 참이면 참
# (x and y) x,y 모두 참이어야 참
# (not x) x가 참이면 거짓/ x가 거짓이면 참

x=10
y=-10

print(x>0)
print(y>0)

print(x>y)
print(x<y)
 
print(x==10)
print(x!=y)

print(x>0 or y>0)
print(x>0 and y>0)

print(x>0)
print(not x>0) 
