'''
Created on Nov 21, 2016

@author: AndreiMsc
'''

from unittest import TestCase
from domain.Grade import Grade

class Test_Grade(TestCase):
    def setUp(self):
        super().setUp()
        self.__grade = Grade(1, 1, 10)

    def test_assign_id(self):
        self.assertEqual(self.__grade.assign_id, 1, "Tested grade assignment id should be <1>!")

    def test_stud_id(self):
        self.assertEqual(self.__grade.stud_id, 1, "Tested grade student id should be <1>!")
    
    def test_grade(self):
        self.assertEqual(self.__assignment.grade, 10, "Tested grade grade should be <10>!")