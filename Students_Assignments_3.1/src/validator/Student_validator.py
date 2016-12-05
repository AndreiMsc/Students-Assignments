'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

class Student_repository_exception(Exception):
    '''
    Exception class for Student_repository
    '''
    pass

class Student_validation_exception(Exception):
    '''
    Exception class for Student_validator
    '''
    pass

class Student_validator:
    '''
    Validates students
    '''
    
    def validate_student(self,stud):
        '''
        Validates students
        Input:
        :param stud
        Raises:
        :exception Student_validation_exception(errors)
        '''
        errors =""
        if stud.stud_id < 0:
            errors += "Student ID must be a positive integer!\n"
        if stud.name == "":
            errors += "Student name cannot be empty!\n"
        if stud.group < 0:
            errors += "Student group must be a positive integer!\n"
        if len(errors) > 0:
            raise Student_validation_exception(errors)        