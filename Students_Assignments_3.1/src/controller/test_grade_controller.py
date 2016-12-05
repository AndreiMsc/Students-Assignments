'''
Created on Nov 21, 2016

@author: AndreiMsc
'''

from unittest import TestCase
from domain.Grade import Grade
from repository.Grade_repository import Grade_repository
from controller.Grade_controller import Grade_controller

class Test_Grade_controller(TestCase):

    def setUp(self):
        super().setUp()
        self.__controller = Grade_controller(Grade_repository)

    def test_add_grade(self):
        grade = Grade(1, 1, 10)
        self.__controller.add_grade(grade)
        self.assertEqual(len(self.__controller.list_all_grades()), 1, "There should be 1 grade in the test repository!")