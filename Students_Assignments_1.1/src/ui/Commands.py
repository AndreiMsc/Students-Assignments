'''
Created on Nov 2, 2016

@author: AndreiMsc
'''
from validator.Assignment_validator import Assignment_validation_exception, Assignment_repository_exception
from validator.Student_validator import Student_validation_exception, Student_repository_exception

class Commands:
    '''
    classdocs
    '''

    def __init__(self, stud_ctrl, assign_ctrl, grade_ctrl):
        '''
        Constructor
        '''
        self.__stud_ctrl = stud_ctrl
        self.__assign_ctrl = assign_ctrl
        self.__grade_ctrl = grade_ctrl
        self.__cmds_list = {"add":self.__ui_add,"remove":self.__ui_remove,"update":self.__ui_update,"list":self.__ui_list}
    
    def __ui_read_command(self):
        return input().split(' ')
    
    def __ui_add(self,params):
        if params[0] == "student":
            params = params[1:]
            self.__ui_add_student(params)
        elif params[0] == "assignment":
            params = params[1:]
            self.__ui_add_assignment(params)
        elif params[0] == "grade":
            params = params[1:]
            self.__ui_add_grade(params)
        else:
            print("Invalid syntax!\n")
            
    def __ui_add_student(self,params):
        if len(params) != 3:
                print("Invalid number of paramters!")
                return 0
        try:
            stud_id = int(params[0])
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        name = params[1]
        try:
            group = int(params[2])
        except ValueError as ve:
            ve="The group must be a positive integer!\n"
            print(ve)
            return 0
        self.__stud_ctrl.add_student(stud_id, name, group)
            
    def __ui_add_assignment(self,params):
        if len(params) != 4:
                print("Invalid number of parameters!")
                return 0
        try:
            assign_id = int(params[0])
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        description = params[1]
        deadline = params[2]
        try:
            grade = int(params[3])
        except ValueError as ve:
            ve="The grade must be an integer from 1 to 10!\n"
            print(ve)
            return 0
        if int(params[3]) < 1 or int(params[3]) > 10:
            print("The grade must be from 1 to 10!\n")
            return 0
        self.__assign_ctrl.add_assignment(assign_id,description,deadline,grade)
        
    def __ui_add_grade(self,params):
        stud_id = params[1]
        for i in range(len(params)-2):
            try:
                assign_id = int(params[0])
            except ValueError as ve:
                ve="The assignment ID must be a positive integer!\n"
                print(ve)
                return 0
            try:
                grade = int(params[len(params)-1])
            except ValueError as ve:
                ve="The grade must be a positive integer!\n"
                print(ve)
                return 0
            if int(params[len(params)-1]) < 1 or int(params[len(params)-1]) > 10:
                print("The grade must be from 1 to 10!\n")
                return 0
            try:
                stud_id = int(params[i+1])
            except ValueError as ve:
                ve="The student ID must be a positive integer!\n"
                print(ve)
                return 0
            self.__grade_ctrl.add_grade(assign_id, stud_id, grade)
    
    def __ui_remove(self,params):
        if params[0] == "student":
            params = params[1:]
            self.__ui_remove_student(params)
        elif params[0] == "assignment":
            params = params[1:]
            self.__ui_remove_assignment(params)
        else:
            print("Invalid syntax!\n")
        
    def __ui_remove_student(self,params):
        if len(params) != 1:
            print ("There should be one parameter: the ID!\n")
        else:
            self.__ui_remove_student_by_id(params)
        
    def __ui_remove_student_by_id(self,params):
        try:
            stud_id = int(params[0])
        except ValueError as ve:
            ve = "ID must be a positive integer!\n"
            print(ve)
            return 0
        self.__stud_ctrl.remove_student_by_id(stud_id)
        
    def __ui_remove_assignment(self,params):
        if len(params) != 1:
            print ("There should be one parameter: the ID!\n")
        else:
            self.__ui_remove_assignment_by_id(params)
        
    def __ui_remove_assign_by_id(self,params):
        try:
            assign_id = int(params[0])
        except ValueError as ve:
            ve = "ID must be a positive integer!\n"
            print(ve)
            return 0
        self.__stud_ctrl.remove_assignment_by_id(assign_id)
    
    def __ui_update(self,params):
        if params[0] == "student":
            params = params[1:]
            self.__ui_update_student(params)
        elif params[0] == "assignment":
            params = params[1:]
            self.__ui_update_assignment(params)
        else:
            print("Invalid syntax!\n")
            
    def __ui_update_student(self,params):
        if len(params) != 3:
                print("Invalid number of paramters!")
                return 0
        try:
            stud_id = int(params[0])
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        name = params[1]
        try:
            group = int(params[2])
        except ValueError as ve:
            ve="The group must be a positive integer!\n"
            print(ve)
            return 0
        self.__stud_ctrl.update_student(stud_id, name, group)

    def __ui_update_assignment(self,params):
        if len(params) != 4:
                print("Invalid number of parameters!")
                return 0
        try:
            assign_id = int(params[0])
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        description = params[1]
        deadline = params[2]
        try:
            grade = int(params[3])
        except ValueError as ve:
            ve="The grade must be an integer from 1 to 10!\n"
            print(ve)
            return 0
        self.__assign_ctrl.update_assignment(assign_id,description,deadline,grade)
        
    def __print_list(self,l):
        for element in l:
            print(element)                  
                                                        
    def __ui_list(self,params):
        if len(params) != 1:
            print("Invalid syntax!\n")
        elif params[0] == "students":
            self.__print_list(self.__stud_ctrl.list_all_students())
        elif params[0] == "assignments":
            self.__print_list(self.__assign_ctrl.list_all_assignments())
        else:
            print("Invalid syntax!\n")    
                
    def ui_run(self):
        print("Wellcome! --- @author: AndreiMsc\n")
        while True:
            print("Please type a command..")
            cmd = self.__ui_read_command()
            if cmd[0] == 'return 0':
                return 
            if cmd[0] == "exit":
                print("Thank you for using the application!\n --- @author: AndreiMsc\n Also, don't forget to visit my website: https://github.com/AndreiMsc/")
                return
            if cmd[0] in self.__cmds_list:
                try:
                    self.__cmds_list[cmd[0]](cmd[1:])
                except Student_validation_exception as sve:
                    print("Student Validation Error:\n",sve)
                except Student_repository_exception as sre:
                    print("Student Repository Error:\n",sre)
                except Assignment_validation_exception as sve:
                    print("Student Validation Error:\n",sve)
                except Assignment_repository_exception as sre:
                    print("Student Repository Error:\n",sre)
            else:
                print("Invalid command!")