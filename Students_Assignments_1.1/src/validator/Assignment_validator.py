'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

class Assignment_repository_exception(Exception):
    pass


class Assignment_validation_exception(Exception):
    pass

class Assignment_validator:
    def validate_assignment(self,assign):
        errors =""
        if assign.assign_id < 0:
            errors += "Assignment ID must be a positive integer!\n"
        if assign.description == "":
            errors += "Assignment description cannot be empty!\n"
        if assign.deadline == "":
            errors += "Assignment deadline cannot be empty!\n"
        if assign.grade < 0:
            errors += "Assignment deadline cannot be empty!\n"  
        if len(errors) > 0:
            raise Assignment_validation_exception(errors)        