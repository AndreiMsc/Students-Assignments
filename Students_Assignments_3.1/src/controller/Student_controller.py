'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

from domain.Student import Student
from validator.Student_validator import Student_validator

class Student_controller:
    '''
    Controls students repository
    '''

    def __init__(self, repository):
        '''
        Constructor
        '''
        
        self.__stud_repository = repository
        self.__stud_validator = Student_validator()
        
    def add_student(self,stud_id,name,group):
        '''
        Adds a new student to the repository after validating its properties
        Input:
        :param stud_id
        :param name
        :param group
        '''
        
        stud = Student(stud_id,name,group)
        self.__stud_validator.validate_student(stud)
        self.__stud_repository.add_student(stud)
        
    def add_sample_data(self):
        '''
        Adds sample students to the repository
        '''
        
        self.add_student(1,"Andrei",916)
        self.add_student(2,"Cristian",916)
        self.add_student(3,"Catalin",916)
        self.add_student(4,"Babenco",915)
        self.add_student(5,"Ramona",915)
        self.add_student(6,"Lorena",915)
        self.add_student(7,"Iulia",915)
        self.add_student(8,"Gandalf",916)
        self.add_student(9,"Sauron",916)
        self.add_student(10,"Harry Potter",916)
        
    def update_student(self,stud_id,name,group):
        '''
        Updates a student from the repository after validating its new properties
        Input:
        :param stud_id
        :param name
        :param group
        '''
        
        stud = Student(stud_id,name,group)
        self.__stud_validator.validate_student(stud)
        self.__stud_repository.update_student(stud)     
         
    def remove_student_by_id(self,stud_id):
        '''
        Removes the student with the given ID from the repository
        Input:
        :param stud_id
        '''
        
        self.__stud_repository.remove_student_by_id(stud_id)
        
    def find_student_by_id(self,stud_id):
        '''
        Finds the student with the given ID
        Input:
        :param stud_id
        Output:
        :return stud_with_id
        '''
        
        stud_with_id = self.__stud_repository.find_student(stud_id)
        return stud_with_id
    
    def students_length(self):
        '''
        Returns the number of students
        Output:
        :return self.__stud_repository.student_length()
        '''
        
        return self.__stud_repository.student_length()
        
    def list_all_students(self):
        '''
        Makes a list containing all students
        Output:
        :return self.__stud_repository.list_all_students()
        '''
        
        return self.__stud_repository.list_all_students()
    
    def replace(self,new_repo):
        self.__stud_repository.replace(new_repo)
        
    def repo(self):
        return self.__stud_repository.repo