'''
Created on Nov 2, 2016

@author: AndreiMsc
'''

class Student:
    '''
    classdocs
    '''

    def __init__(self, stud_id, name, group):
        '''
        Constructor
        '''
        self.__stud_id = stud_id
        self.__name = name
        self.__group = group
    
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
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @name.deleter
    def name(self):
        del self.__name
        
    @property
    def group(self):
        return self.__group
    
    @group.setter
    def group(self, group):
        self.__group = group
   
    @group.deleter
    def group(self):
        del self.__group

    def __str__(self):
        return self.__name+" from "+str(self.__group)