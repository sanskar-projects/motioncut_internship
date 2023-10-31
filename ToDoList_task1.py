from pandas import DataFrame
import tkinter
import sys
all_tasks=[]
completed_tasks=[]

def add():
    header("CREATE TASK")
    global all_tasks
    name=input("enter name: ")
    text=input("enter description: ")
    date=input("enter due date(dd/mm/yyyy): ")
    priority=input("enter priority: ")
    list=[]
    list.append(name)
    list.append(text)
    list.append(date)
    list.append(priority)
    all_tasks.append(list)
    footer("TASK CREATED")

def display():
    header("PENDING TASKS")
    sort()
    d={}
    list=[]
    for i in all_tasks:
        list.append(i[0])
    d["name"]=list
    list=[]
    for i in all_tasks:
        list.append(i[1])
    d["description"]=list
    list=[]
    for i in all_tasks:
        list.append(i[2])
    d["due date"]=list
    list=[]
    for i in all_tasks:
        list.append(i[3])
    d["priority"]=list
    print(DataFrame(d).rename_axis("task id"))
    footer("")
    header("COMPLETED TASKS")
    d={}
    list=[]
    for i in completed_tasks:
        list.append(i[0])
    d["name"]=list
    list=[]
    for i in completed_tasks:
        list.append(i[1])
    d["description"]=list
    list=[]
    for i in completed_tasks:
        list.append(i[2])
    d["due date"]=list
    list=[]
    for i in completed_tasks:
        list.append(i[3])
    d["priority"]=list
    print(DataFrame(d).rename_axis("task id"))
    footer("")

def tick():
    header("MARK TASK AS COMPLETED")
    global all_tasks,completed_tasks
    n=int(input("enter task id: "))
    completed_tasks.append(all_tasks[n])
    all_tasks.pop(n)
    footer("TASK MARKED AS COMPLETED")

def update():
    header("UPDATE TASK")
    global all_tasks
    n=int(input("enter task id: "))
    name=input("enter name: ")
    text=input("enter description: ")
    date=input("enter due date: ")
    priority=input("enter priority: ")
    list=[]
    list.append(name)
    list.append(text)
    list.append(date)
    list.append(priority)
    all_tasks[n]=list
    footer("TASK UPDATED")

def pop_all():
    header("DELETE PENDING TASK")
    global all_tasks
    n=int(input("enter task id: "))
    all_tasks.pop(n)
    footer("TASK DELETED")

def pop_completed():
    header("DELETE COMPLETED TASK")
    global completed_tasks
    n=int(input("enter task id: "))
    completed_tasks.pop(n)
    footer("TASK DELETED")

def clear_all():
    header("")
    global all_tasks
    all_tasks.clear()
    print("PENDING TASKS CLEARED")
    footer("")

def clear_completed():
    header("")
    global completed_tasks
    completed_tasks.clear()
    print("COMPLETED TASKS CLEARED")
    footer("")

def load():
    header("")
    global all_tasks,completed_tasks
    try:
        f=open("all_tasks.txt","r")
        n=int(f.readline())
        for i in range(n):
            name=f.readline()
            text=f.readline()
            date=f.readline()
            priority=f.readline()
            list=[]
            list.append(name.rstrip("\n"))
            list.append(text.rstrip("\n"))
            list.append(date.rstrip("\n"))
            list.append(priority.rstrip("\n"))
            all_tasks.append(list)
        f.close()
        f=open("completed_tasks.txt","r")
        n=int(f.readline())
        for i in range(n):
            name=f.readline()
            text=f.readline()
            date=f.readline()
            priority=f.readline()
            list=[]
            list.append(name.rstrip("\n"))
            list.append(text.rstrip("\n"))
            list.append(date.rstrip("\n"))
            list.append(priority.rstrip("\n"))
            completed_tasks.append(list)
        f.close()
        print("DATA HAS BEEN LOADED")
    except:
        all_tasks=[]
        completed_tasks=[]
        print("DATA NOT FOUND")
    footer("")
        

def store():
    header("")
    sort()
    f=open("all_tasks.txt","w")
    n=len(all_tasks)
    f.write(str(n)+"\n")
    for i in all_tasks:
        name=i[0]
        text=i[1]
        date=i[2]
        priority=i[3]
        f.write(name+"\n")
        f.write(text+"\n")
        f.write(date+"\n")
        f.write(priority+"\n")
    f.close()
    f=open("completed_tasks.txt","w")
    n=len(completed_tasks)
    f.write(str(n)+"\n")
    for i in completed_tasks:
        name=i[0]
        text=i[1]
        date=i[2]
        priority=i[3]
        f.write(name+"\n")
        f.write(text+"\n")
        f.write(date+"\n")
        f.write(priority+"\n")
    f.close()
    print("DATA HAS BEEN STORED")
    footer("")

def sort():
    global all_tasks,completed_tasks
    all_tasks.sort(key=lambda x:x[3])
    completed_tasks.sort(key=lambda x:x[3])

def exit():
    header("EXIT")
    print("THANK YOU")
    sys.exit()

def header(s):
    x="-"*50
    print(x+"\n"+s+"\n\n\n\n\n")

def footer(s):
    x="-"*50
    print("\n\n\n\n\n"+s+"\n"+x)

def main():
    header("TO DO LIST")
    r=tkinter.Tk()
    f1=tkinter.Frame(r)
    f1.pack()
    label=tkinter.Label(f1,text='TO DO LIST',width=100,height=1,bg='yellow',fg='black')
    label.pack()
    b1=tkinter.Button(f1,text='CREATE TASK',width=100,height=1,command=add,bg='black',fg='white')
    b1.pack()
    f2=tkinter.Frame(r)
    f2.pack(side=tkinter.TOP)
    b2=tkinter.Button(f1,text='VIEW TASKS',width=100,height=1,command=display,bg='black',fg='white')
    b2.pack()
    f3=tkinter.Frame(r)
    f3.pack(side=tkinter.TOP)
    b3=tkinter.Button(f1,text='MARK TASK AS COMPLETED',width=100,height=1,command=tick,bg='black',fg='white')
    b3.pack()
    f4=tkinter.Frame(r)
    f4.pack(side=tkinter.TOP)
    b4=tkinter.Button(f1,text='UPDATE PENDING TASK',width=100,height=1,command=update,bg='black',fg='white')
    b4.pack()
    f5=tkinter.Frame(r)
    f5.pack(side=tkinter.TOP)
    b5=tkinter.Button(f1,text='DELETE PENDING TASK',width=100,height=1,command=pop_all,bg='black',fg='white')
    b5.pack()
    f6=tkinter.Frame(r)
    f6.pack(side=tkinter.TOP)
    b6=tkinter.Button(f1,text='DELETE COMPLETED TASK',width=100,height=1,command=pop_completed,bg='black',fg='white')
    b6.pack()
    f7=tkinter.Frame(r)
    f7.pack(side=tkinter.TOP)
    b7=tkinter.Button(f1,text='CLEAR PENDING TASKS',width=100,height=1,command=clear_all,bg='black',fg='white')
    b7.pack()
    f8=tkinter.Frame(r)
    f8.pack(side=tkinter.TOP)
    b8=tkinter.Button(f1,text='CLEAR COMPLETED TASKS',width=100,height=1,command=clear_completed,bg='black',fg='white')
    b8.pack()
    f9=tkinter.Frame(r)
    f9.pack(side=tkinter.TOP)
    b9=tkinter.Button(f1,text='LOAD DATA',width=100,height=1,command=load,bg='black',fg='white')
    b9.pack()
    f10=tkinter.Frame(r)
    f10.pack(side=tkinter.TOP)
    b10=tkinter.Button(f1,text='STORE DATA',width=100,height=1,command=store,bg='black',fg='white')
    b10.pack()
    f11=tkinter.Frame(r)
    f11.pack()
    b11=tkinter.Button(f1,text='EXIT',width=100,height=1,command=exit,bg='black',fg='white')
    b11.pack()
    r.mainloop()

main()
