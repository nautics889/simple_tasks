class custom_property(object):
    def __init__(self, getter, setter, deleter):
        self.getter = getter
        self.setter = setter
        self.deletter = deleter

    def __get__(self, instance, owner):
        print(f'GET ATTRIBUTE FROM {instance}')
        return self.getter(instance)

    def __set__(self, instance, value):
        print(f'SET FOLLOWING VALUE {value}')
        self.setter(instance, value)

    def __delete__(self, instance):
        print(f'DELETE ATTRIBUTE FROM {instance}')
        self.deleter(instance)


class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be str-instance.')
        self.__name = value

    def del_name(self):
        del self.__name

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0 or value > 100:
            raise ValueError('Incorrect person age.')
        self.__name = value

    def del_age(self):
        del self.__age

    name = custom_property(get_name, set_name, del_name)
    age = custom_property(get_age, set_age, del_age)


def create_persons():
    print('Create person with correct name and age:')

    bob = Person('Bob', 20)

    print(f'Name: {bob.name}\nAge: {bob.age}')

    print('Set incorrect age for created person:')

    try:
        bob.age = 1200
    except ValueError as err:
        print(f'Error! {err}')