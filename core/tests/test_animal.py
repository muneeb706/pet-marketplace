from unittest import TestCase

from core.animal import Cat, Dog


class TestAnimal(TestCase):

    def setUp(self):
        pass

    def test_cat_speak(self):
        animal = Cat()
        self.assertEqual("Meow!", animal.speak())

    def test_dog_speak(self):
        animal = Dog()
        self.assertEqual("Woof!", animal.speak())
