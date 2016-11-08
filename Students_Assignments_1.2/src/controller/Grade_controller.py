'''
Created on Nov 6, 2016

@author: A Cell MUSCHITO
'''

from domain.Grade import Grade
from validator.Grade_validator import Grade_validator
from repository.Grade_repository import Grade_repository
from repository.Student_repository import Student_repository
from repository.Assignment_repository import Assignment_repository

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
        self.__stud_repository = Student_repository()
        self.__assign_repository = Assignment_repository()
        
    def give_assignment(self,assign_id,stud_id):
        self.__assign_repository[assign_id]
        self.__stud_repository[stud_id]
        grade = Grade(assign_id,stud_id,0)
        self.__grade_repository.add_grade(grade)
        
    def add_sample_data(self):
        self.give_assignment(1,1)
        self.give_assignment(2,3)
        self.give_assignment(3,5)
        self.give_assignment(4,7)
        self.give_assignment(5,9)
        self.give_assignment(6,7)
        self.give_assignment(7,5)
        self.give_assignment(8,3)
        self.give_assignment(9,1)
        self.give_assignment(10,2)
        
    def give_grade_by_group(self,assign_id,group):
        for student in self.__stud_repository.list_all_students:
            if str(student.group) == str(group):
                stud_id = student.stud_id
                grade = Grade(assign_id,stud_id,0)
                self.__grade_validator.validate_grade(grade)
                self.__grade_repository.add_grade(grade)
                
    def delete_grade_by_id(self,assign_id,stud_id):
        self.__grade_repository.remove_grade_by_id(assign_id,stud_id)
        
    def find_grade_by_id(self,assign_id,stud_id):
        return self.__repo[(assign_id,stud_id)]
            
    def list_all_grades(self):
        return self.__grade_repository.list_all_grades()