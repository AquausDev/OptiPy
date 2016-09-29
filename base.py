#OptiPy - a python code optimisation program made in python
import fileinput

class DefineFixes:
    """outlies all the functions that run the fixes"""
    def switch_single_quotes():
        """switches quotes from ' to " """
        #takes the users file name
        file_name = input("Enter the python file name: ")

        with fileinput.FileInput(file_name+".py", inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace("('", '("'), end='')
        with fileinput.FileInput(file_name+".py", inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace("')", '")'), end='')
        print("Finished")
                
    def switch_double_quotes():
        """switches quotes from " to ' """
        #takes the users file name
        file_name = input("Enter the python file name: ")

        #opens the file, backs it up and then replaces
        with fileinput.FileInput(file_name+".py", inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace('("', "('"), end='')
        with fileinput.FileInput(file_name+".py", inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace('")', "')"), end='')
        print("Finished")

class RunFixes:
    """runs all the fixing functions"""      
    def manage_switches():
        """runs the main section of switches of sections"""
        #runs the single quote switch
        ask1 = input("Switch single quotes? ")
        if ask1 == "yes":
            DefineFixes.switch_single_quotes()
            
        #runs the double quote switch
        ask2 = input("Switch double quotes? ")
        if ask2 == "yes":
            DefineFixes.switch_double_quotes()
            
RunFixes.manage_switches()
