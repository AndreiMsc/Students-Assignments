'''
Created on Nov 21, 2016

@author: AndreiMsc
'''

from unittest import TestCase
from domain.Student import Student
from repository.Student_repository import Student_repository
from controller.Student_controller import Student_controller

class Test_Student_controller(TestCase):

    def setUp(self):
        super().setUp()
        self.__controller = Student_controller(Student_repository)

    def test_add_student(self):
        student = Student(1, "Andrei", 916)
        self.__controller.add_student(student)
        self.assertEqual(len(self.__controller.list_all_students()), 1, "There should be 1 student in the test repository!")