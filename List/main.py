from List.Classes import tasks

day_one = tasks("Cut corn", "Peel corn", "Wash pots")
day_two = tasks("Take out thrash", "Thaw tamales", "Cook")

print("Welcome to your amazing Task tracker, input your answers and in lowercase please")
print("""our tasks are divided in two groups. The first group are the work day tasks, and the second group are the 
non work day ones. """)
print("\n")
print("Work days")
day_one.list_tasks()
print("\n")
print("Non-work days")
day_two.list_tasks()

day_one.check_for_task()
print("\n")
day_two.check_for_task()

print("hI")
