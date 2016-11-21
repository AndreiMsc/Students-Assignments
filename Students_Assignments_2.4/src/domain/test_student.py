'''
Created on Nov 21, 2016

@author: AndreiMsc
'''

from unittest import TestCase
from domain.Student import Student

class Test_Student(TestCase):
    def setUp(self):
        super().setUp()
        self.__student = Student(1, "Andrei", 916)

    def test_stud_id(self):
        self.assertEqual(self.__student.stud_id, 1, "Tested student id should be <1>!")

    def test_name(self):
        self.assertEqual(self.__student.name, "Andrei", "Tested student name should be <Andrei>!")

    def test_group(self):
        self.assertEqual(self.__student.group, 916, "Tested student group should be <916>!")