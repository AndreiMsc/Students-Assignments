'''
Created on Nov 6, 2016

@author: AndreiMsc
'''

class ui_Selector:
    '''
    classdocs
    '''

    @staticmethod
    def ui_selector():
        while True:
            method = input("Type <1> if you want to use the command-based application..\n Type <2> if you want to use the menu-based application..\n")
            if method == "1":
                method = "command"
                return method
            elif method == "2":
                method = "menu"
                return method
            else:
                print("Invalid input!\n")