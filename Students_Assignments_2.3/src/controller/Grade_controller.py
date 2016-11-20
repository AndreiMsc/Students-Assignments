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
        grade = Grade(assign_id,stud_id,0)
        self.__grade_validator.validate_grade(grade)
        self.__grade_repository.add_grade(grade)
         
    def add_sample_data(self):
        self.give_assignment(1,3)
        self.give_assignment(1,2)
        self.give_assignment(1,5)
        self.give_assignment(2,3) 
        self.give_assignment(3,5)
        self.give_assignment(4,7)
        self.give_assignment(5,9)
        self.give_assignment(6,7)
        self.give_assignment(7,5)
        self.give_assignment(8,3)
        self.give_assignment(9,1)
        self.give_assignment(10,2)
        self.evaluate_grade(3, 1, 10)
        self.evaluate_grade(2, 1, 4)
        self.evaluate_grade(5, 1, 6)
        
    def give_grade_by_group(self,assign_id,group):
        for student in self.__stud_repository.list_all_students:
            if str(student.group) == str(group):
                stud_id = student.stud_id
                grade = Grade(assign_id,stud_id,0)
                self.__grade_validator.validate_grade(grade)
                self.__grade_repository.add_grade(grade)
                
    def delete_grade_by_id(self,assign_id,stud_id):
        self.__grade_repository.remove_grade_by_id(assign_id,stud_id)
        
    def remove_grade_after_student_id(self,stud_id):
        self.__grade_repository.remove_grade_after_student_id(stud_id)
        
    def remove_grade_after_assignment_id(self,assign_id):
        self.__grade_repository.remove_grade_after_assignment_id(assign_id)
        
    def find_grade_by_id(self,assign_id,stud_id):
        return self.__repo[(assign_id,stud_id)]
            
    def list_all_grades(self):
        return self.__grade_repository.list_all_grades()
    
    def list_zero_grades_of_student(self,stud_id):
        return self.__grade_repository.list_zero_grades_of_student(stud_id)
    
    def evaluate_grade(self,stud_id,grade_to_evaluate,evaluation):
        self.__grade_repository.evaluate_grade(stud_id,grade_to_evaluate,evaluation)
        
    def list_students_with_assignment(self,assign_id):
        return self.__grade_repository.list_students_with_assignment(assign_id)
    
    def possible_late(self,possible_late_assign):
        possible_late = []
        for assign in possible_late_assign:
            studs_w_assign = self.__grade_repository.list_students_with_assignment(assign)
            for stud in studs_w_assign:
                possible_late.append(stud)
        return possible_late
    
    def average_for_students(self,list_of_all_students):
        student_with_average_list = []
        for student in list_of_all_students:
            student_id = student.stud_id
            student_with_average_list.append(self.__grade_repository.calculate_average_for_students(student_id))
        return student_with_average_list
       
    def average_for_assignments(self,list_of_all_assignments):
        assignments_with_average_list = []
        for assignment in list_of_all_assignments:
            assign_id = assignment.assign_id
            assignments_with_average_list.append(self.__grade_repository.calculate_average_for_assignments(assign_id))
        return assignments_with_average_list