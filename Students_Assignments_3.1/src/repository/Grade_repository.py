'''
Created on Nov 6, 2016

@author: AndreiMsc
'''

from validator.Grade_validator import Grade_repository_exception

class Grade_repository:
    '''
    Keeps count of all grades
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
        self.__grades={}
    
    def add_grade(self,grade):
        '''
        Adds a student to the repository if the combination assignmentID-studentID is free
        Input:
        :param grade
        Output:
        :print ("Grade assignmentID-studentID combination is already taken!")
        '''
        
        if (grade.assign_id, grade.stud_id) in self.__grades:
            print("Grade assignmentID-studentID combination is already taken!")
            return
        self.__grades[(grade.assign_id, grade.stud_id)] = grade
        
    def remove_grade_by_id(self,assign_id,stud_id):
        '''
        Removes the grade with the given assignmentID-studentID combination if it exists
        Input:
        :param assign_id
        :param stud_id
        Raises:
        :exception Grade_repository_exception("Invalid ID!\n")
        '''
    
        if (assign_id, stud_id) not in self.__grades:
            raise Grade_repository_exception("Invalid ID!\n")
        del self.__grades[(assign_id,stud_id)]
        
    def remove_grade_after_student_id(self,stud_id):
        '''
        Removes all grades belonging to the student with the given ID
        Input:
        :param stud_id
        '''
        
        list_of_grades = []
        for grade in self.__grades:
            list_of_grades.append([grade[0],' ',grade[1]])
        index = 0
        while index <= len(list_of_grades)-1:
            if list_of_grades[index][2] == stud_id:
                del self.__grades[(list_of_grades[index][0], stud_id)]
            index = index + 1
            
    def remove_grade_after_assignment_id(self,assign_id):
        '''
        Removes all grades containing the assignment with the given ID
        Input:
        :param assign_id
        '''
        
        list_of_grades = []
        for grade in self.__grades:
            list_of_grades.append([grade[0],' ',grade[1]])
        index = 0
        while index <= len(list_of_grades)-1:
            if list_of_grades[index][0] == assign_id:
                del self.__grades[(assign_id, list_of_grades[index][2])]
            index = index + 1
        
    def find_grade_by_id(self,grade_id):
        '''
        Checks if a grade with the given ID exists
        Input:
        :param grade_id
        Output
        :return found
        '''
        
        if grade_id not in self.__grades:
            raise Grade_repository_exception("Invalid grade ID!\n")
        return self.__grades[grade_id]
        
    def list_all_grades(self):
        '''
        Makes a list of all grades
        Output:
        :return grade_list
        '''
        
        grade_list=[]
        for grade in self.__grades.values():
            grade_list.append(str(grade))
        return grade_list
    
    def list_zero_grades_of_student(self,stud_id):
        '''
        Makes a list with students which have at least one grade which is not evaluated
        Input:
        :param stud_id
        Output:
        :return (zero_grades_list)
        '''
        
        zero_grades_list=[]
        for grade in self.__grades:
            if grade[1] == stud_id:
                if self.__grades[grade].grade == 0:
                    zero_grades_list.append(self.__grades[grade].assign_id)
        return (zero_grades_list)
    
    def evaluate_grade(self,stud_id,grade_to_evaluate,evaluation):
        '''
        Evaluates a grade of the student with the given ID
        Input:
        :param stud_id
        :param grade_to_evaluate
        :param evaluation
        '''
        
        self.__grades[(grade_to_evaluate, stud_id)].grade = evaluation
        
    def list_students_with_assignment(self,assign_id):
        '''
        Makes a list containing the IDs of all students which have assigned the assignment with the given ID
        Input:
        :param assign_id
        Output:
        :return studs_w_assign
        '''
        
        studs_w_assign = []
        for grade in self.__grades:
            if grade[0] == assign_id:
                studs_w_assign.append([self.__grades[grade].stud_id, self.__grades[grade].grade])
        if studs_w_assign == []:
            return studs_w_assign
        studs_w_assign = self.__order_descending_by_grade(studs_w_assign)
        return studs_w_assign
    
    def calculate_average_for_students(self,stud_id):
        '''
        Calculates the average of the grades of the student with the given ID
        Input:
        :param stud_id
        Output:
        :return (stud_id,' has average ',str(average))
        '''
        
        sum_of_evaluations = 0
        number_of_evaluations = 0
        for grade in self.__grades:
            if grade[1] == stud_id:
                sum_of_evaluations = sum_of_evaluations + self.__grades[grade].grade
                number_of_evaluations = number_of_evaluations + 1
        if number_of_evaluations == 0:
            return (stud_id,' has no assignments','.')
        average = float(sum_of_evaluations)/float(number_of_evaluations)
        return (stud_id,' has average ',str(average))
 
    def calculate_average_for_assignments(self,assign_id):
        '''
        Calculates the average of the grades of the assignment with the given ID
        Input:
        :param assign_id
        Output:
        :return (assign_id,' has average ',str(average))
        '''
        
        sum_of_evaluations = 0
        number_of_evaluations = 0
        for grade in self.__grades:
            if grade[0] == assign_id:
                sum_of_evaluations = sum_of_evaluations + self.__grades[grade].grade
                number_of_evaluations = number_of_evaluations + 1
        if number_of_evaluations == 0:
            return (assign_id,' is not assigned to anyone','.')
        average = float(sum_of_evaluations)/float(number_of_evaluations)
        return (assign_id,' has average ',str(average))
    
    def replace(self,new_repo):
        self.__grades = new_repo
        
    def repo(self):
        return self.__grades
    
'''    
    def __add_grade__(self,grade):
        self.add_grade(grade)
        
    def __remove_grade_by_id__(self,assign_id,stud_id):
        if (type(assign_id) is int) and (type(assign_id) is int):
            self.remove_grade_by_id(assign_id, stud_id)
            
    def __find_grade_by_id__(self,grade_id):
        return self.find_grade_by_id(grade_id)
            
    def __list_all_grades__(self):
        return self.list_all_grades()
    
    def __order_descending_by_grade(self, studs_w_assign):
        studs_w_assign.sort(key=lambda x: x[1], reverse = True)
        return studs_w_assign
'''    
    