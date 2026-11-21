class Task:
    def __init__(self,title,is_done=False):
        self.title=title
        self.is_done=is_done
    def show_info(self):
        return(f'TaskTitle:{self.title}\nIs_done:{self.is_done}')
    @classmethod
    def from_string(cls,text):
        title,is_done=text.split(',')
        return cls(title.strip(),is_done.strip()=='True')
    

class TodoList:
    def __init__(self):
        self.tasks=[]
    @staticmethod
    def chek(title):
        if title.strip()!='':
            return True
        return False
    def add_task(self,title,is_done=False):
        if self.chek(title)==False:
            raise ValueError('this task is None!')
        task=Task(title,is_done)
        self.tasks.append(task)
    def show_tasks(self):
        for task in self.tasks:
            print(task.show_info())
    def mark_done(self,title):
        found=False
        for task in self.tasks:
            if task.title.lower()==title.lower():
                found=True
                if not task.is_done:
                   task.is_done=True
                   print(f'ok,"{title}" marked as done!')
                else:
                    print(f'"{title}" is already done!')
        if found==False:
         print(f'"{title}" not found!')
t1=Task.from_string('read a newspaper   ,   True   ')
print(t1.title)
print(t1.is_done)
t2=Task.from_string('sleep,False')
print(t2.is_done)
t=TodoList()
t.add_task('read a book')
t.add_task('watch a movie')
t.add_task('learn python',True)

t.mark_done('read a book')
t.mark_done('sleep')
t.mark_done('learn python')
t.show_tasks()



t=TodoList()
try:
  t.add_task('gg')
except ValueError as e:
    print(e)
else:
    print('added')
finally:
    print('have a good day!')
  
 

