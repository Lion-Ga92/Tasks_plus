import datetime

class tasks(object):

    def __init__(self, task1, task2, task3):
        self.task1 = task1
        self.task2 = task2
        self.task3 = task3

    def list_tasks(self):
        print("1: " + self.task1)
        print("2: " + self.task2)
        print("3: " + self.task3)



    def check_for_task(self):
        completed_tasks = ""
        completed_tasks += input("Type in name and date: ")
        completed_tasks += "\n"
        print("Did you", self.task1, "?")
        task_one_check = input("Yes or no: ")
        if task_one_check == "yes":
            print("You", self.task1, "!")
            completed_tasks += "You " + self.task1 + "!" + "\n"
        elif task_one_check == "no":
            print("You still need to", self.task1)
            completed_tasks += "You still need to " + self.task1 + "\n"
        else:
            print("Not valid, type 'yes' or 'no' please")

        print("Did you", self.task2, "?")
        task_two_check = input("'Yes' or 'no': ")
        if task_two_check == "yes":
            print("You", self.task2, "!")
            completed_tasks += "You, " +self.task2 + "!" + "\n"
        elif task_two_check == "no":
            print("You still need to", self.task2)
            completed_tasks += "You still need to, " + self.task2 + "\n"
        else:
            print("Not valid, type 'yes' or 'no' please")

        print("Did you", self.task3, "?")
        task_three_check = input("'Yes' or 'no': ")
        if task_three_check == "yes":
            print("You", self.task3, "!")
            completed_tasks += "You, " + self.task3 + "!" + "\n"
        elif task_three_check == "no":
            print("You still need to", self.task3)
            completed_tasks += "You still need to, " + self.task3 + "\n"
        else:
            print("Response not valid")

        completed_tasks += "\n"

        task_file = open("task_list.txt", "a+")
        task_file.write(completed_tasks)








