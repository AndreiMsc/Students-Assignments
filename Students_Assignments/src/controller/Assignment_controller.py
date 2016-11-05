'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

from domain.Assignment import Assignment
from validator.Assignment_validator import Assignment_validator
from repository.Assignment_repository import Assignment_repository

class Assignment_controller:
    '''
    classdocs
    '''

    def __init__(self, repository):
        '''
        Constructor
        '''
        self.__assign_repository = Assignment_repository()
        self.__assign_validator = Assignment_validator()
        
    def add_assignment(self,assign_id,description,deadline,grade):
        assign = Assignment(assign_id,description,deadline,grade)
        self.__assign_validator.validate_assignment(assign)
        self.__assign_repository.add_assignment(assign)
        
    def update_assignment(self,assign_id,description,deadline):
        assign = Assignment(assign_id,description,deadline)
        self.__assign_validator.validate_assignment(assign)
        self.__assign_repository.update_assignment(assign)
        
    def remove_assignment(self,assign_id,description,deadline,grade):
        assign = Assignment(assign_id,description,deadline,grade)
        self.__assign_validator.validate_assignment(assign)
        self.__assign_repo.remove_assignment(assign)
         
    def remove_assignment_by_id(self,assign_id):
        self.__assign_repository.remove_assignment(assign_id)
        
    def find_assignment_by_id(self,assign_id):
        return self.__assign_repository.find_assignment(assign_id)         
    
    def assignments_length(self):
        return self.__assign_repository.assignments_length()
        
    def list_all_assignments(self):
        return self.__assign_repository.list_all_assignments()