'''
Created on Nov 6, 2016

@author: AndreiMsc
'''
     
from validator.Assignment_validator import Assignment_validation_exception, Assignment_repository_exception
from validator.Student_validator import Student_validation_exception, Student_repository_exception
import copy

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
        self.__undo =[]
        self.__redo=[]
        
        
    def add_sample_data(self):
        self.__stud_ctrl.add_sample_data()
        self.__assign_ctrl.add_sample_data()
        self.__grade_ctrl.add_sample_data()
   
    def __ui_read_command(self,request):
        print(request)
        return input()
    
    def __ui_add(self):
        while True:
            cmds_list = {"1":self.__ui_add_student, "2":self.__ui_add_assignment, "3":self.__ui_give_assignment}
            com_list = ["1","2","3","4","5"]
            cmd = self.__ui_read_command("    Type <1> to add student, <2> to add assignment, <3> to give assignment,  <4> if you changed your mind..")
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
        deadline = self.__ui_read_command("        Insert assignment deadline: day/month/year ").split("/")
        if len(deadline)!=3:
            print("Invalid deadline format!\n")
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
        
    def __ui_give_assignment(self):
        cmds_list = {"1":self.__ui_give_assignment_by_student,"2":self.__ui_give_assignment_by_group}
        com_list = ["1","2","3"]
        cmd = self.__ui_read_command("    Type <1> to give assignment to a student, <2> to give assignment to a group, <3> if you changed your mind..")
        if cmd in com_list:
            if cmd == "3":
                return
            else:
                cmds_list[cmd]()
                return
        else:
            print("Invalid input!\n")
            return

    def __ui_give_assignment_by_student(self):
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
        self.__grade_ctrl.give_assignment(assign_id, stud_id)
          
    def __ui_give_assignment_by_group(self):
        assign_id = self.__ui_read_command("        Insert assignment ID: ")
        try:
            assign_id = int(assign_id)
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        stud_group = self.__ui_read_command("        Insert students group: ")
        try:
            stud_group = int(stud_group)
        except ValueError as ve:
            ve="The students group must be a positive integer!\n"
            print(ve)
            return 0
        ok=False
        for stud in self.__stud_ctrl.list_all_students():
            if stud.group == stud_group:
                self.__grade_ctrl.give_assignment(assign_id, stud.stud_id)
                ok=True
        if ok==False:
            print('There are no students in this group')

    def __ui_remove(self):
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
        self.__grade_ctrl.remove_grade_after_student_id(stud_id)
        self.__stud_ctrl.remove_student_by_id(stud_id)
        
    def __ui_remove_assignment_by_id(self):
        assign_id = self.__ui_read_command("        Insert assign ID..")   
        try:
            assign_id = int(assign_id)
        except ValueError as ve:
            ve = "ID must be a positive integer!\n"
            print(ve)
            return 0
        self.__grade_ctrl.remove_grade_after_assignment_id(assign_id)
        self.__assign_ctrl.remove_assignment_by_id(assign_id)
    
    def __ui_update(self):
        while True:
            cmds_list = {"1":self.__ui_update_student, "2":self.__ui_update_assignment, "3":self.__ui_evaluate_student}
            com_list = ["1","2","3","4"]
            cmd = self.__ui_read_command("    Type <1> to update student, <2> to update assignment, <3> to evaluate a grade of a student, <4> if you changed your mind..")
            if cmd in com_list:
                if cmd == "4":
                    return
                else:
                    cmds_list[cmd]()
                    return
            else:
                print("Invalid input!\n")
                return
            
    def __ui_update_student(self):
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
            
    def __ui_evaluate_student(self):
        stud_id = self.__ui_read_command("    Type the ID of the student you want to evaluate..")
        try:
            stud_id = int(stud_id)
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        zero_grades_of_stud = self.__grade_ctrl.list_zero_grades_of_student(stud_id)
        if zero_grades_of_stud == []:
            print("This student has no grades which are not evaluated..")
            return 0
        else:
            print(zero_grades_of_stud)
        grade_to_eval = self.__ui_read_command("        Type the grade you want to evaluate..")
        try:
            grade_to_eval = int(grade_to_eval)
        except ValueError as ve:
            ve="The grade must be a positive integer from the list above!\n"
            print(ve)
            return 0
        if grade_to_eval not in zero_grades_of_stud:
            print("Invalid grade selected..")
            return 0
        evaluation = self.__ui_read_command("            Type the grade with which you want to evaluate..")
        try:
            evaluation = int(evaluation)
        except ValueError as ve:
            ve="The grade must be positive!\n"
            print(ve)
            return 0
        if evaluation < 1 or evaluation > 10:
            print("The grade must be from 1 to 10")
        self.__grade_ctrl.evaluate_grade(stud_id,grade_to_eval,evaluation)
        
        
    def __print_list(self,l):
        for element in l:
            print(element)                  
                                                        
    def __ui_list(self):
        while True:
            cmds_list = {"1":self.__ui_list_students, "2":self.__ui_list_assignments, "3":self.__ui_list_grades}
            com_list = ["1","2","3","4"]
            cmd = self.__ui_read_command("    Type <1> to list students, <2> to list assignments, <3> to list grades, <4> if you changed your mind..")
            if cmd in com_list:
                if cmd == "4":
                    return
                else:
                    cmds_list[cmd]()
                    return
            else:
                print("Invalid input!\n")
                return
            
    def __ui_list_students(self):
        self.__print_list(self.__stud_ctrl.list_all_students())
        
    def __ui_list_assignments(self):
        self.__print_list(self.__assign_ctrl.list_all_assignments()) 
            
    def __ui_list_grades(self):
        self.__print_list(self.__grade_ctrl.list_all_grades())
        
    def __ui_statistics(self):
        while True:
            cmds_list = {"1":self.__ui_list_students_with_assignment, "2":self.__ui_list_late_students, "3":self.__ui_list_average_for_students, "4":self.__ui_list_average_for_assignments}
            com_list = ["1","2","3", "4"]
            cmd = self.__ui_read_command("    Type <x> to list: <1> students with a given assignment, <2> students who are late, <3> average situation for students, <4> average sittation for assignments, <5> if you changed your mind..")
            if cmd in com_list:
                if cmd == "5":
                    return
                else:
                    cmds_list[cmd]()
                    return
            else:
                print("Invalid input!\n")
                return
        
    def __ui_list_students_with_assignment(self):
        assign_id = self.__ui_read_command("    Type the ID of the assignment you want too see which students have..")
        try:
            assign_id = int(assign_id)
        except ValueError as ve:
            ve="The ID must be a positive integer!\n"
            print(ve)
            return 0
        exists = self.__assign_ctrl.find_id(assign_id)
        if exists == False:
            print("This ID does not belong to an assignment!")
            return 0
        studs_w_assign = self.__grade_ctrl.list_students_with_assignment(assign_id)
        if studs_w_assign == []:
            print("There are no students which have this assignment!")
            return 0
        for i in range(len(studs_w_assign)):
            studs_w_assign[i] = str(studs_w_assign[i][0])+" evaluated at "+str(studs_w_assign[i][1])
        self.__print_list(studs_w_assign)
        
    def __ui_list_late_students(self):
        possible_late_assign = self.__assign_ctrl.possible_late()
        possible_late_stud = self.__grade_ctrl.possible_late(possible_late_assign)
        print(possible_late_stud)
        list_of_late = []
        for stud in possible_late_stud:
            if stud[1] == 0:
                list_of_late.append(stud[0])       
        list_of_late_once = []
        for stud in list_of_late:
            if stud not in list_of_late_once:
                list_of_late_once.append(stud)
        if list_of_late_once == []:
            print("No students are late!")
            return 0
        self.__print_list(list_of_late_once)
        
    def __ui_list_average_for_students(self):
        list_of_all_students = self.__stud_ctrl.list_all_students()
        stud_average_list = self.__grade_ctrl.average_for_students(list_of_all_students)
        stud_average_list.sort(key=lambda x: x[2], reverse = True)
        for average in stud_average_list:
            print(str(average[0])+average[1]+average[2])
            
    def __ui_list_average_for_assignments(self):
        list_of_all_assignments = self.__assign_ctrl.list_all_assignments()
        assign_average_list = self.__grade_ctrl.average_for_assignments(list_of_all_assignments)
        assign_average_list.sort(key=lambda x: x[2], reverse = True)
        for average in assign_average_list:
            print(str(average[0])+average[1]+average[2])
            
    def __ui_save(self):
        self.__undo.append(copy.deepcopy([self.__grade_ctrl,self.__stud_ctrl,self.__assign_ctrl]))
        
    def __ui_undo(self):
        lenght = len(self.__undo) -1
        if lenght==-1:
            print('No more commands to undo!')
            return
        self.__redo.append(copy.deepcopy([self.__grade_ctrl, self.__stud_ctrl, self.__assign_ctrl]))
        self.__grade_ctrl = self.__undo[lenght][0]
        self.__stud_ctrl = self.__undo[lenght][1]
        self.__assign_ctrl = self.__undo[lenght][2]
        del self.__undo[lenght]
        
    def __ui_redo(self):
        lenght = len(self.__redo) -1
        if lenght==-1:
            print('No more commands to redo!')
            return
        self.__undo.append(copy.deepcopy([self.__grade_ctrl, self.__stud_ctrl, self.__assign_ctrl]))
        self.__grade_ctrl = self.__redo[lenght][0]
        self.__stud_ctrl = self.__redo[lenght][1]
        self.__assign_ctrl = self.__redo[lenght][2]
        del self.__redo[lenght]
        
    def ui_run(self):
        print("Wellcome! --- @author: AndreiMsc\n")
        self.add_sample_data()
        while True:
            cmds_list = {"1":self.__ui_add, "2":self.__ui_remove, "3":self.__ui_update, "4":self.__ui_list, "5":self.__ui_statistics, "6":self.__ui_undo, "7":self.__ui_redo}
            com_list = ["1","2","3","4","5","6","7","8"]
            cmd = self.__ui_read_command("Type <1> to add/give, <2> to remove, <3> to update/evaluate, <4> to list, <5> to list statistics, <6> to undo, <7> to redo, <8> to exit..")
            if cmd in com_list:
                if cmd == "8":
                    print("Thank you for using the application!\n --- @author: AndreiMsc\n Also, don't forget to visit my website: https://github.com/AndreiMsc/")
                    return
                else:
                    if (cmd=='1' or cmd=='2' or cmd=='3'):
                        self.__ui_save()
                    
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