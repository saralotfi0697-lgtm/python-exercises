class Task:
    def __init__(self,title,done=False):
        self.title=title
        self.done=done
    def show_info(self):
        return(f'Title of Task:{self.title}\nIs_done:{self.done}')
class TodoList:
    def __init__(self):
        self.tdlist=[]
    def add_task(self,title,done=False):
        t=Task(title,done)
        self.tdlist.append(t)
    def show_tasks(self):
        for i in self.tdlist:
            print(i.show_info())
td=TodoList()
td.add_task('read a book',True)
td.add_task('go to the shopping')
td.show_tasks()