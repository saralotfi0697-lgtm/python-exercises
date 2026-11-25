class Book:
    def __init__(self,title,author=None):
        self.title=title
        self.author=author
        self.is_available=True
    def Show_info(self):
        return(f'Title:{self.title}\nAuthor:{self.outhor}\nAvailable:{self.is_available}')
class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
    def Add_book(self,title,author=None):
        book=Book(title,author)
        self.books.append(book)
    def Add_member(self,name):
        member=Member(name)
        self.members.append(member)
class Member:
    def __init__(self,name):
        self.name=name
        self.borrowed_books=[]
    def Borrowed_books(self,title):
        self.borrowed_books.append(title)
lib = Library()

for book in lib.books:
    print(book.Show_info())
lib.Add_member('Sara')
lib.Add_member('Mina')
lib.Borrowed_books('python')
for member in lib.members:
    print(member.name)
for book in Borr

        
        