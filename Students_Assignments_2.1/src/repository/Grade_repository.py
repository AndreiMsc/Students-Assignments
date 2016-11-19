'''
Created on Nov 6, 2016

@author: A Cell MUSCHITO
'''

from validator.Grade_validator import Grade_repository_exception

class Grade_repository:
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.__grades={}
    
    def add_grade(self,grade):
        self.__grades[(grade.assign_id, grade.stud_id)] = grade
        
    def remove_grade_by_id(self,assign_id,stud_id):
        if (assign_id, stud_id) not in self.__grades:
            raise Grade_repository_exception("Invalid ID!\n")
        del self.__grades[(assign_id,stud_id)]
        
    def find_grade_by_id(self,grade_id):
        if grade_id not in self.__grades:
            raise Grade_repository_exception("Invalid grade ID!\n")
        return self.__grades[grade_id]
        
    def list_all_grades(self):
        grade_list=[]
        for grade in self.__grades.values():
            grade_list.append(grade)
        return grade_list
    
    def list_zero_grades_of_student(self,stud_id):
        zero_grades_list=[]
        for grade in self.__grades:
            if grade[1] == stud_id:
                if self.__grades[grade].grade == 0:
                    zero_grades_list.append(self.__grades[grade].assign_id)
        return(zero_grades_list)
    
    def evaluate_grade(self,stud_id,grade_to_evaluate,evaluation):
        self.__grades[(grade_to_evaluate, stud_id)].grade = evaluation
    
    def __add_grade__(self,grade):
        self.add_grade(grade)
        
    def __remove_grade_by_id__(self,assign_id,stud_id):
        if (type(assign_id) is int) and (type(assign_id) is int):
            self.remove_grade_by_id(assign_id, stud_id)
            
    def __find_grade_by_id__(self,grade_id):
        return self.find_grade_by_id(grade_id)
            
    def __list_all_grades__(self):
        return self.list_all_grades()