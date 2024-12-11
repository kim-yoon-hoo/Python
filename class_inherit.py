class Person:
    total_count = 0 #클래스 변수 공유가능
    def init(self, name, age):
        self.name = name
        self.age = age
        Person.total_count += 1
    def introduce(self):
        print(f'제 이름은 {self.name}이고, 제 나이는 {self.age}살 입니다.')


p1 = Person('김윤후',17)
p1.introduce()
p2 = Person('윈터', 23)
p2.introduce
p3 = Person('박찬호', 29)
p3.introduce
print(p3.total_count)


#상속

class Person:
    total_count = 0 #클래스 변수 공유가능
    def init(self, name, age):
        self.name = name
        self.age = age
        Person.total_count += 1
    def introduce(self):
        print(f'제 이름은 {self.name}이고, 제 나이는 {self.age}살 입니다.')

class Student(Person):
    def init(self, name, age):
        super().init(name, age)
    def run(self):
        print(f'저는 뛸 수 있어요')



s1 = Student('아이유', 20)
s1.introduce()
s2 = Student('장원영', 21)
s2.introduce()
s3 = Student('안유진', 22)
s3.introduce()



#클래스 오버라이딩
class Person:
    total_count = 0 #클래스 변수 공유가능
    def init(self, name, age):
        self.name = name
        self.age = age
        Person.total_count += 1
    def introduce(self):
        print(f'제 이름은 {self.name}이고, 제 나이는 {self.age}살 입니다.')

class Student(Person):
    def init(self,name='박찬호',age=29):
        super().init('박찬호', 29)
    def run(self):
        print(f'저는 뛸 수 있어요')
    def introduce(self):
        print(f'제 이름은 {self.name}이고, 제 나이는 비밀 입니다.')


stu1 = Student()
stu1.introduce()

print(Student.mro())
print(Person.mro())
