'''
Created on Nov 21, 2016

@author: AndreiMsc
'''

from unittest import TestCase
from domain.Assignment import Assignment
from repository.Assignment_repository import Assignment_repository
from controller.Assignment_controller import Assignment_controller

class Test_Assignment_controller(TestCase):

    def setUp(self):
        super().setUp()
        self.__controller = Assignment_controller(Assignment_repository)

    def test_add_assignment(self):
        assignment = Assignment(1, "Andrei", 916)
        self.__controller.add_assignment(assignment)
        self.assertEqual(len(self.__controller.list_all_assignments()), 1, "There should be 1 assignment in the test repository!")