'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

class Assignment:
    '''
    classdocs
    '''

    def __init__(self, assign_id, description, deadline, grade):
        '''
        Constructor
        '''
        self.__assign_id = assign_id
        self.__description = description
        self.__deadline = deadline
        self.__grade = grade
    
    @property  
    def assign_id(self):
        return self.__assign_id
        
    @assign_id.setter
    def assign_id(self, assign_id):
        self.__assign_id = assign_id
        
    @assign_id.deleter   
    def assign_id(self):
        del self.__assign_id
     
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, description):
        self.__description = description
        
    @description.deleter
    def description(self):
        del self.__description
        
    @property
    def deadline(self):
        return self.__deadline
    
    @deadline.setter
    def deadline(self, deadline):
        self.__deadline = deadline
   
    @deadline.deleter
    def deadline(self):
        del self.__deadline
        
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, grade):
        self.__grade = grade
        
    @grade.deleter
    def grade(self):
        del self.__grade

    def __str__(self):
        return str(self.__assign_id)+" "+self.__description+" until "+str(self.__deadline[0]+"/"+self.__deadline[1]+"/"+self.__deadline[2])+" evaluated at "+str(self.__grade)