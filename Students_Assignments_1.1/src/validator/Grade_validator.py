'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

class Grade_repository_exception(Exception):
    pass


class Grade_validation_exception(Exception):
    pass

class Grade_validator:
    def validate_grade(self,grade):
        errors =""
        if grade.assign_id < 0:
            errors += "Assignment ID must be a positive integer!\n"
        if grade.stud_id == "":
            errors += "Student ID must be a positive integer!\n"
        if grade.grade < 0:
            errors += "Grade must be a positive integer!\n"   
        if len(errors) > 0:
            raise Grade_validation_exception(errors)        