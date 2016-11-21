'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

from domain.Assignment import Assignment
from validator.Assignment_validator import Assignment_validator
from repository.Assignment_repository import Assignment_repository
from datetime import date

class Assignment_controller:
    '''
    Controls assignments repository
    '''

    def __init__(self, repository):
        '''
        Constructor
        '''
        
        self.__today = date.today()
        self.__assign_repository = Assignment_repository()
        self.__assign_validator = Assignment_validator()
        
    def add_assignment(self,assign_id,description,deadline,grade):
        '''
        Adds a new assignment to the repository after validating its properties
        Input:
        :param assign_id
        :param description
        :param deadline
        :param grade
        '''
        
        assign = Assignment(assign_id,description,deadline,grade)
        self.__assign_validator.validate_assignment(assign)
        self.__assign_repository.add_assignment(assign)
        
    def add_sample_data(self):
        '''
        Adds sample assignments to the repository
        '''
        
        self.add_assignment(1,"ass1","20 1 2013",2)
        self.add_assignment(2,"ass2","21 1 2014",2)
        self.add_assignment(3,"ass3","22 1 2015",2)
        self.add_assignment(4,"ass4","23 1 2016",2)
        self.add_assignment(5,"ass5","24 1 2017",2)
        self.add_assignment(6,"ass6","25 1 2018",2)
        self.add_assignment(7,"ass7","26 1 2019",2)
        self.add_assignment(8,"ass8","27 1 2020",2)
        self.add_assignment(9,"ass9","28 1 2021",2)
        self.add_assignment(10,"ass10","29 1 2022",2)
        1
    def update_assignment(self,assign_id,description,deadline,grade):
        '''
        Updates an assignment from the repository after validating its new properties
        Input:
        :param assign_id
        :param description
        :param deadline
        :param grade
        '''
        
        assign = Assignment(assign_id,description,deadline,grade)
        self.__assign_validator.validate_assignment(assign)
        self.__assign_repository.update_assignment(assign)
         
    def remove_assignment_by_id(self,assign_id):
        '''
        Removes the assignment with the given ID from the repository
        Input:
        :param assign_id
        '''
        
        self.__assign_repository.remove_assignment_by_id(assign_id)
        
    def find_assignment_by_id(self,assign_id):
        '''
        Finds the assignment with the given ID
        Input:
        :param assign_id
        Output:
        :return assign_with_id
        '''
        
        assign_with_id = self.__assign_repository.find_assignment(assign_id)
        return assign_with_id        
    
    def assignments_length(self):
        '''
        Returns the number of assignments
        Output:
        :return self.__assign_repository.assignments_length()
        '''
        
        return self.__assign_repository.assignments_length()
        
    def list_all_assignments(self):
        '''
        Makes a list containing all assignments
        Output:
        :return self.__assign_repository.list_all_assignments()
        '''
        
        return self.__assign_repository.list_all_assignments()
    
    def find_id(self,assign_id):
        '''
        Check if the assignment with the given ID exists
        Input:
        :param assign_id
        Output:
        :return self.__assign_repository.find_id(assign_id)
        '''
        
        return self.__assign_repository.find_id(assign_id)
    
    def possible_late(self):
        '''
        Makes a list containing all IDs of assignments which have the deadline passed, so which could be late
        Output:
        :return possible_late
        '''
        
        possible_late = []
        for assign in self.__assign_repository.list_all_assignments():
            assign.deadline = assign.deadline.split(' ')
            assign_deadline = date(int(assign.deadline[2]), int(assign.deadline[1]), int(assign.deadline[0]))
            if self.__today > assign_deadline:
                possible_late.append(assign.assign_id)
        return possible_late