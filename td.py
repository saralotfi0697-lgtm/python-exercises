class Task:
    def __init__(self,title , done=False):
        self.title=title
        self.done=done
    @classmethod
    def from_string(cls,text):
        title,done=text.split(',')
        return cls(title.strip() ,done.strip()=='True' )
    def show_info(self):
        return (f'Title:{self.title}\nIs_done:{self.done}')
class TodoList:
    def __init__(self):
        self.tasks=[]
    def add_task(self,title,done=False):
        t=Task(title,done)
        self.tasks.append(t)
    def __iter__(self):
        return iter(self.tasks)
    def show_all(self):
        for task in self:
            print(task.title)
t=Task.from_string('buy milk , True')
print(t.title)
print(t.done) 
print('----')
ob=TodoList()
ob.add_task('read a book')
ob.add_task('watch a movie',True)
ob.add_task('go to the shop')
ob.show_all() 
print(iter(ob))   
it=iter(ob)
while True:
    try:
      print(next(it).title)
    except StopIteration:
        break
 


