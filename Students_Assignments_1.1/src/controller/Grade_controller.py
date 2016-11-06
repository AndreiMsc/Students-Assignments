'''
Created on Nov 6, 2016

@author: A Cell MUSCHITO
'''

from domain.Grade import Grade
from validator.Grade_validator import Grade_validator
from repository.Grade_repository import Grade_repository

class Grade_controller:
    '''
    classdocs
    '''

    def __init__(self, repository):
        '''
        Constructor
        '''
        self.__grade_repository = Grade_repository()
        self.__grade_validator = Grade_validator()
        
    def add_grade(self,assign_id,stud_id,grade):
        grade = Grade(assign_id,stud_id,grade)
        self.__grade_validator.validate_grade(grade)
        self.__grade_repository.add_grade(grade)
        
    def list_all_grades(self):
        return self.__grade_repository.list_all_grades()