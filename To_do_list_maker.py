import pickle
import os
def show_individual_task(task = None):
    if task==None: task = []
    print("_"*60)
    lst = ("Task Name" ,"Important" ,"Urgent")
    print("{:>10}     {:>10} {:>10}".format(*lst))
    print("_"*60)
    print(" {:>10}     {:>10} {:>10}".format(*task))
    print("_"*60)

def show_task(Task_List = None):
    if Task_List==None: Task_List = []
    print("_"*60)
    lst = ("Order" ,"Task Name" ,"Important" ,"Urgent")
    print("{:>10} {:>10}     {:>10} {:>10}".format(*lst))
    print("_"*60)
    for i,task in enumerate(Task_List):
        print(f"  {i+1}  "," {:>10}     {:>10} {:>10}".format(*task))   
    print("_"*60)
    print("\n")
def search_task(task_name="",task_list=None):
    if task_list==None or task_name == "": 
        task_list = []
        return None
    for i,task in enumerate(task_list):
        if task_name in task[0]:
            return task,i
    return None
try:
    if os.path.exists("to_do_list_task.txt"):
        with open("to_do_list_task.txt", "rb") as fp:
            to_do_task_list = pickle.load(fp)
            fp.close()
    else:
        to_do_task_list = []
except Exception as e:
    to_do_task_list  = []

# fp.close()
# fpc = open("completed_task_list.txt","rb")
# fpc.seek(0)
try:
    if os.path.exists("completed_task_list.txt"):
        with open("completed_task_list.txt", "rb") as fp:
            completed_task_list = pickle.load(fp)
            fp.close()
    else:
        completed_task_list = []
except Exception as e:
    completed_task_list  = []

print("\n","-"*25,"Welcome to TO DO TASK MANAGER","-"*25,"\n")
while True:
    choice = input("""
Main Menu 
    1. Show Task
    2. Add Task
    3. Edit Taks
    4. Mark Complete
    5. Delete Task
    6. Clear all
    7. Exit                 
    
    Your Choice ->  """).lower()
    if '1' in choice or 'show task' in choice:
        print("    Tasks To Do -> ")
        show_task(to_do_task_list)
        print("    Completed Tasks -> ")
        show_task(completed_task_list)
    elif '2' in choice or 'add task' in choice:
        task_name = input("     Task Name -> ").lower()
        isImportant = True if(input("     Is it Important? (Y/N) -> ").lower()) == 'y' else False
        isUrgent = True if(input("     Is it Urgent? (Y/N) -> ").lower()) == 'y' else False
        iscomplete = False
        value = int(isImportant) + int(isUrgent) * 2 + 1
        to_do_task = [task_name,isImportant,isUrgent,value,iscomplete] 
        to_do_task_list.append(to_do_task)
        to_do_task_list.sort(key = lambda task:task[3],reverse=True)
        fp = open("to_do_list_task.txt","wb")
        pickle.dump(to_do_task_list,fp)
        fp.close()
    elif '3' in choice or 'Edit task' in choice:
        # print("    Tasks To Do -> ")
        # show_task(to_do_task_list)
        # print("    Completed Tasks -> ")
        # show_task(completed_task_list)
        all_task_list = to_do_task_list+completed_task_list
        print("    All Tasks  -> ")
        show_task(all_task_list)
        while True:
            try:
                order_num = int(input("Enter the order of the task You Want to EDIT -> "))
                if(len(to_do_task_list)<order_num or order_num<1):
                    print("Out of Order-> ")
                    continue
            except:
                print("Plese Enter a valid integer -> ")
            else:
                break
        task_name = input("     New Task Name -> ").lower()
        isImportant = True if(input("     Is it Important? (Y/N) -> ").lower()) == 'y' else False
        isUrgent = True if(input("     Is it Urgent? (Y/N) -> ").lower()) == 'y' else False
        iscomplete = True if(input("     Wanna Mark it complete (Y/N) -> ").lower()) == 'y' else False
        value = int(isImportant) + int(isUrgent) * 2 + 1 
        edited_task = [task_name,isImportant,isUrgent,value,iscomplete]

        all_task_list.pop(order_num-1)
        all_task_list.append(edited_task)
        all_task_list.sort(key = lambda task:task[3],reverse=True)

        to_do_task_list = []
        completed_task_list = []

        for task in all_task_list:
            if(task[-1]==True):
                completed_task_list.append(task)
                fp = open("completed_task_list.txt","wb")
                pickle.dump(completed_task_list,fp)
                fp.close()

            else:
                to_do_task_list.append(task)
                to_do_task_list.sort(key = lambda task:task[3],reverse=True)
                fp = open("to_do_list_task.txt","wb")
                pickle.dump(to_do_task_list,fp)
                fp.close()

    elif '4' in choice or 'mark complete' in choice:
        print("    Tasks To Do -> ")
        show_task(to_do_task_list)
        while True:
            try:
                order_num = int(input("Enter the order of the task You want to mark complete-> "))
                if(len(to_do_task_list)<order_num or order_num<1):
                    print("Out of Order-> ")
                    continue
            except:
                print("Plese Enter a valid integer -> ")
            else:
                break
        show_individual_task(to_do_task_list[order_num-1])
        completed_task_list.append(to_do_task_list.pop(order_num-1))
        fp = open("to_do_list_task.txt","wb")
        pickle.dump(to_do_task_list,fp)
        fp.close()
        fp = open("completed_task_list.txt","wb")
        pickle.dump(completed_task_list,fp)
        fp.close()
        print("\n","-"*25,"Marked Complete","-"*25,"\n")
    elif '5' in choice or 'delete task' in choice:
        all_task_list = to_do_task_list+completed_task_list
        print("    All Tasks  -> ")
        show_task(all_task_list)
        while True:
            try:
                order_num = int(input("Enter the order of the task you want to delete -> "))
                if(len(all_task_list)<order_num<1):
                    continue
            except:
                print("Plese Enter a valid integer -> ")
            else:
                break

        show_individual_task(all_task_list.pop(order_num-1))

        to_do_task_list = []
        completed_task_list = []

        for task in all_task_list:
            if(task[-1]==True):
                completed_task_list.append(task)
                fp = open("completed_task_list.txt","wb")
                pickle.dump(completed_task_list,fp)
                fp.close()

            else:
                to_do_task_list.append(task)
                to_do_task_list.sort(key = lambda task:task[3],reverse=True)
                fp = open("to_do_list_task.txt","wb")
                pickle.dump(to_do_task_list,fp)
                fp.close()
        print("\n","-"*25,"Deleted Successfully","-"*25,"\n")

    elif '7' in choice or 'exit' in choice:
        print("\n","-"*25,"Good Bye !!","-"*25,"\n")
        break
    elif '6' in choice or 'clear_all' in choice:
        to_do_task_list = []
        completed_task_list = []
        fp = open("to_do_list_task.txt","wb")
        pickle.dump(to_do_task_list,fp)
        fp.close()
        fp = open("completed_task_list.txt","wb")
        pickle.dump(completed_task_list,fp)
        fp.close()
        print("\n","-"*25,"All Cleared","-"*25,"\n")
    else:
        print("\n","-"*25,"Invalid Choice !","-"*25,"\n")




        