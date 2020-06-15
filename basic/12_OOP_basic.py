class Person: # 클래스 객체 생성 (클래스 정의)
    name = '이름이란, 사람이 공통적으로 가지는 속성'
    age = '나이란 , 태어나서 죽을 때 까지의 기간'

    def greeting(self):
        return f'{self.name}이 인사합니다. 안녕하세요 ~ !'
    # 메서드 : 클래스 내에 정의된 함수
    def aging(self):
        return f'{self.name}은 {self.age}살 입니다.'
    @classmethod
    def age_means(cls):
        return f'{cls.name}은 나라마다 다르다.'
# list_a = list()
# 변수를 따로 생성하지 않고, 바로 인스턴스화 해서 메서드 호출
print(Person().greeting())

p1 = Person()
p1.name = "윤소윤"
p1.age = 100
print(p1.name)
print(p1.age)
print(Person.name)
print(Person.age)
#인스턴스 메서드의 접근 방법
print(p1.greeting())
print(p1.aging())


print(Person.age_means())
print(p1.age_means())


