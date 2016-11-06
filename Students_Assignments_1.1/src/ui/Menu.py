'''
Created on Nov 6, 2016

@author: AndreiMsc
'''
     
from validator.Assignment_validator import Assignment_validation_exception, Assignment_repository_exception
from validator.Student_validator import Student_validation_exception, Student_repository_exception

class Menu:
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
    
    def __ui_read_command(self,request):
        print(request)
        return input()
    
    def __ui_add(self):
        while True:
            cmds_list = {"1":self.__ui_add_student, "2":self.__ui_add_assignment, "3":self.__ui_add_grade}
            com_list = ["1","2","3"]
            cmd = self.__ui_read_command("    Type <1> to add student, <2> to add assignment, <3> to add grade, <4> if you changed your mind..")
            if cmd in com_list:
                if cmd == "4":
                    return
                else:
                    cmds_list[cmd]()
                    return
            else:
                print("Invalid input!\n")
                return
            
    def __ui_add_student(self):
        stud_id = self.__ui_read_command("        Insert student ID: ")
        try:
            stud_id = int(stud_id)
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        name = self.__ui_read_command("        Insert student name: ")
        group = self.__ui_read_command("        Insert student group: ")
        try:
            group = int(group)
        except ValueError as ve:
            ve="The group must be a positive integer!\n"
            print(ve)
            return 0
        self.__stud_ctrl.add_student(stud_id, name, group)
            
    def __ui_add_assignment(self):
        assign_id = self.__ui_read_command("        Insert assignment ID: ")
        try:
            assign_id = int(assign_id)
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        description = self.__ui_read_command("        Insert assignment description: ")
        deadline = self.__ui_read_command("        Insert assignment deadline: ")
        grade = self.__ui_read_command("        Insert assignment grade: ")
        try:
            grade = int(grade)
        except ValueError as ve:
            ve="The grade must be a positive integer!\n"
            print(ve)
            return 0
        if int(grade) < 1 or int(grade) > 10:
            print("The grade must be between 1 and 10!\n")
            return 0
        self.__assign_ctrl.add_assignment(assign_id, description, deadline, grade)
        
    def __ui_add_grade(self):
        stud_id = self.__ui_read_command("        Insert student ID: ")
        try:
            stud_id = int(stud_id)
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        assign_id = self.__ui_read_command("        Insert assignment ID: ")
        try:
            assign_id = int(assign_id)
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        grade = self.__ui_read_command("        Insert assignment grade: ")
        try:
            grade = int(grade)
        except ValueError as ve:
            ve="The grade must be a positive integer!\n"
            print(ve)
            return 0
        if int(grade) < 1 or int(grade) > 10:
            print("The grade must be between 1 and 10!\n")
            return 0
        self.__grade_ctrl.add_grade(assign_id, stud_id, grade)
    
    def __ui_remove(self,params):
        while True:
            cmds_list = {"1":self.__ui_remove_student_by_id, "2":self.__ui_remove_assignment_by_id}
            com_list = ["1","2","3"]
            cmd = self.__ui_read_command("    Type <1> to remove student, <2> to remove assignment, <3> if you changed your mind..")
            if cmd in com_list:
                if cmd == "3":
                    return
                else:
                    cmds_list[cmd]()
                    return
            else:
                print("Invalid input!\n")
                return
        
    def __ui_remove_student_by_id(self):
        stud_id = self.__ui_read_command("        Insert student ID..")   
        try:
            stud_id = int(stud_id)
        except ValueError as ve:
            ve = "ID must be a positive integer!\n"
            print(ve)
            return 0
        self.__stud_ctrl.remove_student_by_id(stud_id)
        
    def __ui_remove_assign_by_id(self):
        assign_id = self.__ui_read_command("        Insert assign ID..")   
        try:
            assign_id = int(assign_id)
        except ValueError as ve:
            ve = "ID must be a positive integer!\n"
            print(ve)
            return 0
        self.__assign_ctrl.remove_assignment_by_id(assign_id)
    
    def __ui_update(self,params):
        while True:
            cmds_list = {"1":self.__ui_update_student, "2":self.__ui_update_assignment}
            com_list = ["1","2","3"]
            cmd = self.__ui_read_command("    Type <1> to remove student, <2> to remove assignment, <3> if you changed your mind..")
            if cmd in com_list:
                if cmd == "3":
                    return
                else:
                    cmds_list[cmd]()
                    return
            else:
                print("Invalid input!\n")
                return
            
    def __ui_update_student(self,params):
        stud_id = self.__ui_read_command("        Insert student ID: ")
        try:
            stud_id = int(stud_id)
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        name = self.__ui_read_command("        Insert student name: ")
        group = self.__ui_read_command("        Insert student group: ")
        try:
            group = int(group)
        except ValueError as ve:
            ve="The group must be a positive integer!\n"
            print(ve)
            return 0
        self.__stud_ctrl.update_student(stud_id, name, group)

    def __ui_update_assignment(self):
        assign_id = self.__ui_read_command("        Insert assignment ID: ")
        try:
            assign_id = int(assign_id)
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        description = self.__ui_read_command("        Insert assignment description: ")
        deadline = self.__ui_read_command("        Insert assignment deadline: ")
        grade = self.__ui_read_command("        Insert assignment grade: ")
        try:
            grade = int(grade)
        except ValueError as ve:
            ve="The grade must be a positive integer!\n"
            print(ve)
            return 0
        self.__assign_ctrl.update_assignment(assign_id, description, deadline, grade)
        
    def __print_list(self,l):
        for element in l:
            print(element)                  
                                                        
    def __ui_list(self):
        while True:
            cmds_list = {"1":self.__ui_list_students, "2":self.__ui_list_assignments}
            com_list = ["1","2","3"]
            cmd = self.__ui_read_command("    Type <1> to list students, <2> to list assignments, <3> if you changed your mind..")
            if cmd in com_list:
                if cmd == "3":
                    return
                else:
                    cmds_list[cmd]()
            else:
                print("Invalid input!\n")
                return
            
    def __ui_list_students(self):
            self.__print_list(self.__stud_ctrl.list_all_students())
        
    def __ui_list_assignments(self):
            self.__print_list(self.__assign_ctrl.list_all_assignments())  
                
    def ui_run(self):
        print("Wellcome! --- @author: AndreiMsc\n")
        while True:
            cmds_list = {"1":self.__ui_add, "2":self.__ui_remove, "3":self.__ui_update, "4":self.__ui_list}
            com_list = ["1","2","3","4","5"]
            cmd = self.__ui_read_command("Type <1> to add, <2> to remove, <3> to update, <4> to list, <5> to exit..")
            if cmd in com_list:
                if cmd == "5":
                    print("Thank you for using the application!\n --- @author: AndreiMsc\n Also, don't forget to visit my website: https://github.com/AndreiMsc/")
                    return
                else:
                    try:
                        cmds_list[cmd]()
                    except Student_validation_exception as sve:
                        print("Student Validation Error:\n",sve)
                    except Student_repository_exception as sre:
                        print("Student Repository Error:\n",sre)
                    except Assignment_validation_exception as sve:
                        print("Student Validation Error:\n",sve)
                    except Assignment_repository_exception as sre:
                        print("Student Repository Error:\n",sre)
            else:
                print("Invalid command!\n")