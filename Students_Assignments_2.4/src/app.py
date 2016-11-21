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
from ui.Menu import Menu
from run_tests.run_tests import run_tests

stud_repo = Student_repository()
stud_ctrl = Student_controller(stud_repo)
assign_repo = Assignment_repository()
assign_ctrl = Assignment_controller(assign_repo)
grade_repo = Grade_repository()
grade_ctrl = Grade_controller(grade_repo)
menu = Menu(stud_ctrl,assign_ctrl,grade_ctrl)
run_tests
menu.ui_run()