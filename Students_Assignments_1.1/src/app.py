'''
Created on Nov 3, 2016

@author: AndreiMsc
'''

from repository.Student_repository import Student_repository
from controller.Student_controller import Student_controller
from repository.Assignment_repository import Assignment_repository
from controller.Assignment_controller import Assignment_controller
from repository.Grade_repository import Grade_repository
from controller.Grade_controller import Grade_controller
from ui.Commands import Commands
from ui.Menu import Menu
from ui.ui_Selector import ui_Selector

stud_repo = Student_repository()
stud_ctrl = Student_controller(stud_repo)
assign_repo = Assignment_repository()
assign_ctrl = Assignment_controller(assign_repo)
grade_repo = Grade_repository()
grade_ctrl = Grade_controller(grade_repo)
method = ui_Selector.ui_selector()
if method == "command":
    com = Commands(stud_ctrl,assign_ctrl,grade_ctrl)
    com.ui_run()
else:
    menu = Menu(stud_ctrl,assign_ctrl,grade_ctrl)
    menu.ui_run()