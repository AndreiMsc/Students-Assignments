'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

class Grade_repository_exception(Exception):
    '''
    Exception class for Grade_repository
    '''
    pass

class Grade_validation_exception(Exception):
    '''
    Exception class for Grade_validator
    '''
    pass

class Grade_validator:
    '''
    Validates grades
    '''
    
    def validate_grade(self,grade):
        '''
        Validates grades
        Input:
        :param grade
        Raises:
        :exception Grade_validation_exception(errors)
        '''
        
        errors =""
        if grade.assign_id < 0:
            errors += "Assignment ID must be a positive integer!\n"
        if grade.stud_id == 0:
            errors += "Student ID must be a positive integer!\n"   
        if len(errors) > 0:
            raise Grade_validation_exception(errors)        