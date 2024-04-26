#컨테이너 변수 - 리스트[] 튜플() 딕셔너리{} 셋{}
#딕셔너리{} 사전
person = {
          '이름':'김윤후', 
          '나이':17,
           '키':175, 
          '집주소':'부평구 산곡동'}
print(person['이름'])
print(person)
person['몸무게'] = 45
print(person)
person['키'] = 185
print(person)
del person['나이'] 
print(person)

print(person.get('집주소'))
print(person.get('키'))
print(person.get('몸무게'))
print(person.get('이름'))
print ('몸무게' in person)
print ('나이' in person)
print ('김윤후' in person.values())