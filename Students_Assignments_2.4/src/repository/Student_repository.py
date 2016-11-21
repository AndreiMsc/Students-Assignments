'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

from validator.Student_validator import Student_repository_exception

class Student_repository:
    '''
    Keeps count of all students
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
        self.__students={}
        
    def find_id(self,stud_id):
        '''
        Checks if a students with the given ID exists
        Input:
        :param stud_id
        Output
        :return found
        '''
        
        found = False
        for key in self.__students:
            if key == stud_id:
                found = True
        return found
        
    def add_student(self,stud):
        '''
        Adds a student to the repository if the ID is free
        Input:
        :param stud
        Raises:
        :exception Student_repository_exception("Student ID is already taken!")
        '''
        
        if stud.stud_id in self.__students:
            raise Student_repository_exception("Student ID is already taken!")
        else:
            self.__students[stud.stud_id] = stud
              
    def update_student(self,stud):
        '''
        Updates a student from the repository
        Input:
        :param stud
        Raises:
        :exception Student_repository_exception("This student ID does not belong to a student!")
        '''
        
        if stud.stud_id not in self.__students:
            raise Student_repository_exception("This student ID does not belong to a student!")
        else:
            self.__students[stud.stud_id] = stud
     
    def remove_student(self,stud):
        '''
        Removes a student with the given properties
        Input:
        :param stud
        Raises:
        :exception Student_repository_exception("This student ID does not belong to a student!")
        :exception Student_repository_exception("This student name does not belong to a student!\n")
        :exception Student_repository_exception("This group does not exist/contain any students!\n")
        '''
        
        if stud.stud_id not in self.__students:
            raise Student_repository_exception("This student ID does not belong to a student!")
        elif stud.name not in self.__students:
            raise Student_repository_exception("This student name does not belong to a student!\n")
        elif stud.group not in self.__students:
            raise Student_repository_exception("This group does not exist/contain any students!\n")
        else:
            del self.__students[stud.stud_id]
  
    def remove_student_by_id(self,stud_id):
        '''
        Removes the student with the given ID from the repository if it exists
        Input:
        :param stud_id
        Raises:
        :exception Student_repository_exception("This student ID does not belong to a student!")
        '''
        
        if stud_id not in self.__students:
            raise Student_repository_exception("This student ID does not belong to a student!")
        else:
            del self.__students[stud_id]   
     
    def find_student_by_id(self,stud_id):
        '''
        Finds the student with the given ID if it exists
        Input:
        :param stud_id
        Output:
        :return stud_with_id
        Raises:
        :exception Student_repository_exception("This student ID does not belong to a student!")
        '''
        
        if stud_id not in self.__students:
            raise Student_repository_exception("This student ID does not belong to a student!")
        else:
            stud_with_id = self.__students[stud_id]
            return stud_with_id
    
    def list_all_students(self):
        '''
        Makes a list containing all students
        Output:
        :return stud_list
        '''
        
        stud_list=[]
        for stud in self.__students.values():
            stud_list.append(stud)
        return stud_list
    
    def students_length(self):
        '''
        Returns the number of students
        Output:
        :return len(self.__students
        '''
        
        return len(self.__students)
 
'''   
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
'''