'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

from validator.Student_validator import Student_repository_exception
from domain.Student import Student

class Student_repository:
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__students={}
        
    def find_id(self,stud_id):
        found = False
        for key in self.__students:
            if key == stud_id:
                found = True
        return found
        
    def add_student(self,stud):
        if stud.stud_id in self.__students:
            raise Student_repository_exception("Student ID is already taken!")
        else:
            self.__students[stud.stud_id] = stud
              
    def update_student(self,stud):
        if stud.stud_id not in self.__students:
            raise Student_repository_exception("This student ID does not belong to a student!")
        else:
            self.__students[stud.stud_id] = stud
     
    def remove_student(self,stud):
        if stud.stud_id not in self.__students:
            raise Student_repository_exception("This student ID does not belong to a student!")
        elif stud.name not in self.__students:
            raise Student_repository_exception("This student name does not belong to a student!\n")
        elif stud.group not in self.__students:
            raise Student_repository_exception("This group does not exist/contain any students!\n")
        else:
            del self.__students[stud.stud_id]
  
    def remove_student_by_id(self,stud_id):
        if stud_id not in self.__students:
            raise Student_repository_exception("This student ID does not belong to a student!")
        else:
            del self.__students[stud_id]   
     
    def find_student_by_id(self,stud_id):
        if stud_id not in self.__students:
            raise Student_repository_exception("Invalid Id!")
        else:
            return self.__students[stud_id]  
    
    def list_all_students(self):
        stud_list=[]
        for stud in self.__students.values():
            stud_list.append(stud)
        return stud_list
    
    def students_length(self):
        return len(self.__students)
    
    def __add_student__(self,stud):
        self.add_student(stud)
        
    def __update_student__(self,stud):
        self.update_student(stud)
        
    def __remove_student__(self,param):
        if type(param) is int:
            self.remove_student_by_id(param)    
        if type(param) is Student:
            self.remove_student(param)
                         
    def __find_student__(self,stud_id):
        return self.find_student_by_id(stud_id)          
    
    def __list_all_students__(self):
        return self.list_all_students()