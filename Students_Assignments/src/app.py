'''
Created on Nov 3, 2016

@author: AndreiMsc
'''

from repository.Student_repository import Student_repository
from controller.Student_controller import Student_controller
from repository.Assignment_repository import Assignment_repository
from controller.Assignment_controller import Assignment_controller
from ui.Console import Console

stud_repo = Student_repository()
stud_ctrl = Student_controller(stud_repo)
assign_repo = Assignment_repository()
assign_ctrl = Assignment_controller(assign_repo)
con = Console(stud_ctrl,assign_ctrl)
con.run()