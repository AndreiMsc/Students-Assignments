'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

from validator.Assignment_validator import Assignment_repository_exception

class Assignment_repository:
    '''
    Keeps count of all assignments
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
        self.__assignments={}
        
    def find_id(self,assign_id):
        '''
        Checks if an assignment with the given ID exists
        Input:
        :param assign_id
        Output
        :return found
        '''
        
        found = False
        for key in self.__assignments:
            if key == assign_id:
                found = True
        return found
        
    def add_assignment(self,assign):
        '''
        Adds an assignment to the repository if the ID is free
        Input:
        :param assign
        Raises:
        :exception Assignment_repository_exception("Assignment ID is already taken!")
        '''
        
        if assign.assign_id in self.__assignments:
            raise Assignment_repository_exception("Assignment ID is already taken!")
        else:
            self.__assignments[assign.assign_id] = assign
              
    def update_assignment(self,assign):
        '''
        Updates an assignment from the repository
        Input:
        :param stud
        Raises:
        :exception Assignment_repository_exception("This assignment ID does not belong to a assignment!")
        '''
        
        if assign.assign_id not in self.__assignments:
            raise Assignment_repository_exception("This assignment ID does not belong to a assignment!")
        else:
            self.__assignments[assign.assign_id] = assign
     
    def remove_assignment(self,assign):
        '''
        Removes a student with the given properties
        Input:
        :param assign
        Raises:
        :exception Assignment_repository_exception("This assignment ID does not belong to a assignment!")
        :exception Assignment_repository_exception("This assignment description does not belong to a assignment!\n")
        :exception Assignment_repository_exception("This group does not exist/contain any assignments!\n")
        '''
        
        if assign.assign_id not in self.__assignments:
            raise Assignment_repository_exception("This assignment ID does not belong to a assignment!")
        elif assign.description not in self.__assignments:
            raise Assignment_repository_exception("This assignment description does not belong to a assignment!\n")
        elif assign.group not in self.__assignments:
            raise Assignment_repository_exception("This group does not exist/contain any assignments!\n")
        else:
            del self.__assignments[assign.assign_id]
  
    def remove_assignment_by_id(self,assign_id):
        '''
        Removes the assignment with the given ID from the repository if it exists
        Input:
        :param assign_id
        Raises:
        :exception Assignment_repository_exception("This assignment ID does not belong to a assignment!")
        '''
        
        if assign_id not in self.__assignments:
            raise Assignment_repository_exception("This assignment ID does not belong to a assignment!")
        else:
            del self.__assignments[assign_id]   
     
    def find_assignment_by_id(self,assign_id):
        '''
        Finds the assignment with the given ID if it exists
        Input:
        :param assign_id
        Output:
        :return assign_with_id
        Raises:
        :exception Assignment_repository_exception("This ID does not belong to an assignment!")
        '''
        
        if assign_id not in self.__assignments:
            raise Assignment_repository_exception("This ID does not belong to an assignment!")
        else:
            assign_with_id = self.__assignments[assign_id]
            return assign_with_id  
        
    def assignments_length(self):
        '''
        Returns the number of assignments
        Output:
        :return len(self.__assignments)
        '''
        
        return len(self.__assignments)
    
    def list_all_assignments(self):
        assign_list=[]
        for assign in self.__assignments.values():
            assign_list.append(assign)
        return assign_list
 
'''   
    def __add_assignment__(self,assign):
        self.add_assignment(assign)
        
    def __update_assignment__(self,assign):
        self.update_assignment(assign)
        
    def __remove_assignment__(self,param):
        if type(param) is int:
            self.remove_assignment_by_id(param)    
        if type(param) is Assignment:
            self.remove_assignment(param)
                         
    def __find_assignment__(self,assign_id):
        return self.find_assignment_by_id(assign_id)          
    
    def __list_all_assignments__(self):
        assign_list = ""
        for assign in self.__assignments.values():
            assign_list += str(assign)+"\n"
        return assign_list
'''