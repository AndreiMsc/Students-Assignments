'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

class Grade:
    '''
    classdocs
    '''

    def __init__(self, assign_id, stud_id, grade):
        '''
        Constructor
        '''
        self.__assign_id = assign_id
        self.__stud_id = stud_id
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
    def stud_id(self):
        return self.__stud_id
    
    @stud_id.setter
    def stud_id(self, stud_id):
        self.__stud_id = stud_id
        
    @stud_id.deleter
    def stud_id(self):
        del self.__stud_id
        
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
        return "Assignment "+str(self.__assign_id)+" of student "+str(self.__stud_id)+" evaluated at "+str(self.__grade)