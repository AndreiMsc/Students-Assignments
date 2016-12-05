'''
Created on Nov 21, 2016

@author: AndreiMsc
'''

from unittest import TestCase
from domain.Assignment import Assignment
from repository.Assignment_repository import Assignment_repository

class Test_Assignment_repository(TestCase):

    def setUp(self):
        super().setUp()
        self.__repository = Assignment_repository()

    def test_add_student(self):
        assignment = Assignment(1, "fain", "23 12 1996", 10)
        self.__repository.add_assignment(assignment)
        self.assertEqual(len(self.__repository.list_all_assignments()), 1, "There should be 1 assignment in the test repository!")