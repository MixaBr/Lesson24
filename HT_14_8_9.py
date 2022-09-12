class NonNegativeZeroValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.name} возраст не может быть отрицачельный или нулевой")
        instance.__dict__[self.name] = value


class NonEmptyStrValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if len(value) == 0:
            raise ValueError(f"{self.name} строка не может быть пустой")
        instance.__dict__[self.name] = value

class Pet:
    age = NonNegativeZeroValue()
    name = NonEmptyStrValue()
    master = NonEmptyStrValue()
    def __init__(self,name,age,master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f'{self.name} бегает')

    def jump(self):
        print(f'{self.name} прыгает')

    def birthday(self):
        self.age += 1

    def sleep(self):
         print(f'{self.name} спит')

class Dog(Pet):
        def bark(self):
            print(f'{self.name} лает')

class Cat(Pet):
        def meow(self):
            print(f'{self.name} мяучит')

class  Parrot(Pet):
        def fly(self):
            print(f'{self.name} летает')



d = Dog("Жук",10,"R")
print(d.name)
d.run()
d.jump()