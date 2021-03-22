class Human:

    def __init__(self, first, last, age):
        self._first_name = first
        self._last_name = last
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.age = value
        else:
            raise ValueError("Age cannot be negative!!")

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, name):
        self._first_name, self._last_name = name.split(' ')

if __name__ == '__main__':
    p1 = Human(first='Prachi', last='Mehare', age=25)
    p2 = Human(first='Parag', last='Mehare', age=27)
    p3 = Human(first='Priyanka', last='Mehare', age=26)
    p4 = Human(first='Rohan', last='Mehare', age=15)

    print(p1.age)
    print(p1.full_name)
    p1.full_name = "Poulomi Saha"
    print(p1.full_name)
    print(p2.age)
    print(p3.full_name)
    p3.full_name = "Priyanka Katole"
    print(p3.full_name)
