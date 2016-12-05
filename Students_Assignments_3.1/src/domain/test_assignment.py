'''
Created on Nov 21, 2016

@author: AndreiMsc
'''

from unittest import TestCase
from domain.Assignment import Assignment

class Test_Assignment(TestCase):
    def setUp(self):
        super().setUp()
        self.__assignment = Assignment(1, "fain", "23 12 1996", 10)

    def test_assign_id(self):
        self.assertEqual(self.__assignment.assign_id, 1, "Tested assignment id should be <1>!")

    def test_description(self):
        self.assertEqual(self.__assignment.descriptione, "fain", "Tested assignment description should be <fain>!")
    
    def test_deadline(self):
        self.assertEqual(self.__assignment.deadline, "23 12 1996", "Tested assignment deadline should be <23 12 1996>!")

    def test_grade(self):
        self.assertEqual(self.__assignment.grade, 10, "Tested assignment grade should be <10>!")