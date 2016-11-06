'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

from domain.Student import Student
from validator.Student_validator import Student_validator
from repository.Student_repository import Student_repository

class Student_controller:
    '''
    classdocs
    '''

    def __init__(self, repository):
        '''
        Constructor
        '''
        self.__stud_repository = Student_repository()
        self.__stud_validator = Student_validator()
        
    def add_student(self,stud_id,name,group):
        stud = Student(stud_id,name,group)
        self.__stud_validator.validate_student(stud)
        self.__stud_repository.add_student(stud)
        
    def update_student(self,stud_id,name,group):
        stud = Student(stud_id,name,group)
        self.__stud_validator.validate_student(stud)
        self.__stud_repository.update_student(stud)
        
    def remove_student(self,stud_id,name,group):
        stud = Student(stud_id,name,group)
        self.__stud_validator.validate_student(stud)
        self.__stud_repository.remove_student(stud)
         
    def remove_student_by_id(self,stud_id):
        self.__stud_repository.remove_student_by_id(stud_id)
        
    def find_student_by_id(self,stud_id):
        return self.__stud_repository.find_student(stud_id)
    
    def students_length(self):
        return self.__stud_repository.student_length()
        
    def list_all_students(self):
        return self.__stud_repository.list_all_students()