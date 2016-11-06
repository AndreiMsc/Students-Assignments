'''
Created on Nov 6, 2016

@author: A Cell MUSCHITO
'''

from repository.Student_repository import Student_repository
from repository.Assignment_repository import Assignment_repository
from validator.Grade_validator import Grade_repository_exception

class Grade_repository:
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__grades=[]
        self.__stud_repo = Student_repository 
        self.__assign_repo = Assignment_repository
    
    def add_grade(self,grade):
        stud_id = grade.stud_id
        assign_id = grade.assign_id
        if self.__stud_repo.find_id(stud_id) == False:
            raise Grade_repository_exception("The ID does not belong to a student!\n")
        elif self.__assign_repo.find_id(assign_id) == False:
            raise Grade_repository_exception("The ID does not belong to an assignment!\n")
        else:
            self.__grades.append(grade)
        
    def list_all_grades(self):
        grade_list=[]
        for grade in self.__grades.values():
            grade_list.append(grade)
        return grade_list
    
    def __add_grade__(self,grade):
        self.add_grade(grade)

    def __list_all_grades__(self):
        return self.list_all_grades()