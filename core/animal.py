from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        return "Woof!"


class Cat(Animal):

    def speak(self):
        return "Meow!"


def animal_factory(pet_type=None):
    animal_types = {
        'dog': Dog,
        'cat': Cat,
    }
    if pet_type and pet_type in animal_types:
        return animal_types[pet_type]()

    return None
