'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

class Assignment_repository_exception(Exception):
    '''
    Exception class for Assignment_repository
    '''
    pass

class Assignment_validation_exception(Exception):
    '''
    Exception class for Assignment_validator
    '''
    pass

class Assignment_validator:
    '''
    Validates assignments
    '''
    
    def validate_date(self,date):
        '''
        Validates dates
        Input:
        :param date
        Output:
        :return '<The problem>'
        '''
        
        date=date.split(' ')
        if date[0]<"1" or date[0]>"31" or date[1]<"1" or date[1]>"12" or date[2]<"0":
            return 'The date must be a valid type\n'
        import time
        todayTime = time.strftime("%d %m %Y")
        todayTime = todayTime.split(' ')
        todayTime = [int(todayTime[0]),int(todayTime[1]),int(todayTime[2])]
        if date[2]<date[2]:
            return 'The year must be higher or equal than the current date\n'
        if date[2]==todayTime[2]:
            if date[1]<todayTime[1]:
                return 'The month must be higher or equal than the current date\n'
        if date[2]==todayTime[2] and date[1]==todayTime[1]:
            if date[0]<todayTime[0]:
                return 'The day must be higher or equal than the current date\n'
        if int(date[2])%4==0 and int(date[0])>29 and int(date[1])==2:
            return 'February only got 29 days\n'
        if int(date[2])%4!=0 and int(date[0])>28 and int(date[1])==2:
            return 'February only got 28 days\n'
        monthWith30Days = [4,6,9,11]
        if date[1] in monthWith30Days:
            if int(date[0])>30:
                return 'This month only got 30 days\n'
        return ''    
    
    def validate_assignment(self,assign):
        '''
        Validates assignments
        Input:
        :param assign
        Raises:
        :exception Assignment_validation_exception(errors)
        '''
        
        errors =""
        if assign.assign_id < 0:
            errors += "Assignment ID must be a positive integer!\n"
        if assign.description == "":
            errors += "Assignment description cannot be empty!\n"
        if assign.deadline == "":
            errors += "Assignment deadline cannot be empty!\n"
        errors+=str(self.validate_date(assign.deadline))
        errors+=self.validate_date(assign.deadline)
        if assign.grade < 0:
            errors += "Assignment deadline cannot be empty!\n"  
        if len(errors) > 0:
            raise Assignment_validation_exception(errors)