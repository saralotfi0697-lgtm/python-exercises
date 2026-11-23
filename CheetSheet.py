# ==========================================================
#  چیت‌شیت کامل پایتون سارا 🌿
#  بخش ۱: پایتون مقدماتی    بخش ۲: شی‌گرایی (OOP)
#  هر مثال کوتاهه؛ هر وقت چیزی یادت رفت، فقط همون بخش رو بخون
#  این فایل رو اجرا نکن، فقط مرجعه (بعضی تیکه‌ها کامنت شدن)
# ==========================================================


# ##########################################################
#                  بخش ۱: پایتون مقدماتی
# ##########################################################

# ---------- انواع داده‌ها ----------
a = 5            # int      (عدد صحیح)
b = 3.14         # float    (اعشاری)
c = 'hello'      # str      (رشته/متن)
d = True         # bool     (درست/نادرست)
e = None         # هیچی
print(type(a))   # <class 'int'>
int('7')         # تبدیل: متن به عدد
str(7)           # تبدیل: عدد به متن
bool('False')    # True! (هر متن غیرخالی True است)


# ---------- عملگرها (operators) ----------
# ریاضی:   +  -  *  /  //  %  **
7 / 2      # 3.5   تقسیم معمولی
7 // 2     # 3     تقسیم صحیح (خارج‌قسمت)
7 % 2      # 1     باقی‌مانده
2 ** 3     # 8     توان
# مقایسه:  ==  !=  >  <  >=  <=
# منطقی:   and  or  not
# عضویت:   in  not in      ('a' in 'cat' → True)
x = 5
x += 2     # یعنی x = x + 2


# ---------- دستورات شرطی ----------
age = 20
if age < 18:
    print('child')
elif age < 60:
    print('adult')
else:
    print('senior')
# عبارت یک‌خطی:
status = 'ok' if age >= 18 else 'no'


# ---------- حلقه‌ها ----------
for i in range(3):          # 0 1 2
    print(i)
for name in ['ali', 'sara']:
    print(name)
for i, name in enumerate(['ali', 'sara']):   # شماره + مقدار
    print(i, name)

n = 3
while n > 0:
    print(n)
    n -= 1
# break = خروج از حلقه   continue = رفتن به دور بعد


# ---------- رشته (string) ----------
s = 'Hello World'
s[0]               # 'H'
s[-1]              # 'd'
s[0:5]             # 'Hello'   (برش/slice)
s.lower()          # 'hello world'
s.upper()          # 'HELLO WORLD'
s.strip()          # حذف فاصله‌های دو طرف
s.split(' ')       # ['Hello', 'World']
'-'.join(['a', 'b'])   # 'a-b'
s.replace('World', 'Sara')
s.find('o')        # 4  (اگه نبود -1)
f'name: {s}'       # f-string
# رشته تغییرناپذیره (immutable)


# ---------- لیست (list) ----------
L = [1, 2, 3]
L.append(4)        # اضافه به آخر
L.insert(0, 99)    # اضافه به جای مشخص
L.remove(2)        # حذف با مقدار
L.pop()            # حذف آخری (و برگردوندنش)
L[0]               # دسترسی با شماره
L[1:3]             # برش
L.sort()           # مرتب‌سازی (خود لیست عوض می‌شه)
sorted(L)          # لیست جدید مرتب‌شده
len(L)
squares = [x**2 for x in range(5)]   # list comprehension


# ---------- تاپل (tuple) ----------
# مثل لیسته ولی تغییرناپذیره
T = (1, 2, 3)
T[0]               # 1
# T[0] = 5         # ارور!
a, b = (10, 20)    # باز کردن (unpacking)


# ---------- دیکشنری (dict) ----------
D = {'name': 'sara', 'age': 20}
D['name']                  # 'sara'
D['city'] = 'tehran'       # اضافه/تغییر
D.get('job', 'none')       # اگه نبود، مقدار پیش‌فرض
del D['age']
D.keys()                   # کلیدها
D.values()                 # مقادیر
for k, v in D.items():     # کلید و مقدار
    print(k, v)
'name' in D                # چک کردن کلید


# ---------- مجموعه (set) ----------
# بدون تکرار، بدون ترتیب
S = {1, 2, 2, 3}           # {1, 2, 3}
S.add(4)
S.remove(1)
{1, 2} | {2, 3}            # اجتماع {1,2,3}
{1, 2} & {2, 3}            # اشتراک {2}
{1, 2} - {2, 3}            # تفاضل {1}
list(set([1, 1, 2]))       # حذف تکراری‌ها از لیست


# ---------- تابع - بخش اول ----------
def add(a, b):
    return a + b           # return = برگردوندن نتیجه
add(2, 3)                  # 5

def greet(name='friend'):  # مقدار پیش‌فرض
    print('hi', name)
greet()                    # hi friend
greet(name='sara')         # آرگومان نام‌دار


# ---------- تابع - بخش دوم ----------
def total(*args):          # هر تعداد ورودی → تاپل
    return sum(args)
total(1, 2, 3)             # 6

def info(**kwargs):        # ورودی‌های نام‌دار → دیکشنری
    print(kwargs)
info(a=1, b=2)             # {'a': 1, 'b': 2}

# متغیر محلی و سراسری (global)
counter = 0
def inc():
    global counter         # می‌گیم از متغیر بیرون استفاده کن
    counter += 1


# ---------- تابع بازگشتی (recursion) ----------
# تابعی که خودش رو صدا می‌زنه. حتماً شرط توقف لازمه!
def factorial(n):
    if n <= 1:             # شرط توقف
        return 1
    return n * factorial(n - 1)
factorial(5)               # 120


# ---------- عبارت لامبدا (lambda) ----------
# تابع کوچولوی یک‌خطی و بدون اسم
square = lambda x: x ** 2
square(4)                  # 16
# کاربرد اصلی: با sorted / map / filter
people = [('ali', 30), ('sara', 20)]
sorted(people, key=lambda p: p[1])        # مرتب بر اساس سن
list(map(lambda x: x * 2, [1, 2, 3]))     # [2, 4, 6]
list(filter(lambda x: x > 1, [1, 2, 3]))  # [2, 3]


# ---------- مدیریت استثناء‌ها (exceptions) ----------
try:
    x = int('abc')
except ValueError as e:        # ارور مشخص
    print('bad number:', e)
except ZeroDivisionError:
    print('zero!')
else:                          # اگه ارور نیومد
    print('ok')
finally:                       # همیشه اجرا می‌شه
    print('done')

# ارور خودمون رو بسازیم:
# raise ValueError('title is empty')
assert 2 + 2 == 4, 'math is broken!'   # شرط False → ارور


# ---------- فایل (file) ----------
# with خودش فایل رو می‌بنده (بهترین روش)
with open('a.txt', 'w') as f:      # w = نوشتن (پاک می‌کنه)
    f.write('hello\n')
with open('a.txt', 'a') as f:      # a = اضافه به آخر
    f.write('more\n')
with open('a.txt', 'r') as f:      # r = خوندن
    text = f.read()                # همه‌ی متن
    # f.readlines()                # لیستی از خط‌ها
    # for line in f: ...           # خط‌به‌خط
# فایل نبود؟ FileNotFoundError → با try/except بگیرش

# JSON (برای ذخیره‌ی لیست/دیکشنری)
# import json
# json.dump(data, f)  /  data = json.load(f)


# ---------- عبارت‌های منظم (regex) ----------
import re
re.search(r'\d+', 'abc 123')        # اولین تطابق → '123'
re.findall(r'\d+', 'a1 b22 c333')   # ['1', '22', '333']
re.match(r'^\d{4}$', '2026')        # کل متن باید ۴ رقم باشه
re.sub(r'\s+', ' ', 'a   b')        # جایگزینی → 'a b'
# \d رقم   \w حرف/رقم   \s فاصله   .  هر کاراکتر
# *  صفر یا بیشتر   +  یک یا بیشتر   ?  اختیاری   {n}  دقیقاً n بار
# [abc] یکی از این‌ها   ^ شروع   $ پایان   | یا


# ---------- الگوریتم‌های مرتب‌سازی ----------
# Bubble sort: هر بار دو همسایه رو مقایسه و جابه‌جا می‌کنه
def bubble_sort(L):
    n = len(L)
    for i in range(n):
        for j in range(n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]   # جابه‌جایی
    return L

# Selection sort: هر بار کوچک‌ترین رو پیدا می‌کنه و می‌ذاره اول
def selection_sort(L):
    for i in range(len(L)):
        m = i
        for j in range(i + 1, len(L)):
            if L[j] < L[m]:
                m = j
        L[i], L[m] = L[m], L[i]
    return L
# تو کار واقعی از sorted() / .sort() استفاده می‌کنیم


# ##########################################################
#              بخش ۲: شی‌گرایی (OOP)
# ##########################################################

# ---------- مفاهیم اولیه شی‌گرایی ----------
# class = نقشه   object = چیزی که از نقشه ساخته می‌شه
class Student:
    school = 'MyUni'                    # ویژگی کلاس (مشترک بین همه)

    def __init__(self, name, grade):    # سازنده (constructor)
        self.name = name                # ویژگی آبجکت (attribute)
        self.grade = grade

    def show(self):                     # متد (method)
        return f'{self.name}: {self.grade}'

s = Student('sara', 19)
s.show()                                # 'sara: 19'
# self = خود آبجکتی که متد روش صدا زده شده


# ---------- متدهای Dunder (سربارگذاری / overloading) ----------
# پایتون خودش صداشون می‌زنه؛ ما فقط می‌گیم چیکار کنن
class Box:
    def __init__(self, items):
        self.items = items

    def __str__(self):                  # print(b)
        return f'Box({self.items})'

    def __repr__(self):                 # نمایش برای برنامه‌نویس
        return f'Box({self.items!r})'

    def __len__(self):                  # len(b)
        return len(self.items)

    def __eq__(self, other):            # b1 == b2
        return self.items == other.items

    def __lt__(self, other):            # b1 < b2  (برای sort)
        return len(self.items) < len(other.items)

    def __add__(self, other):           # b1 + b2
        return Box(self.items + other.items)

    def __contains__(self, x):          # x in b
        return x in self.items

    def __getitem__(self, i):           # b[0]
        return self.items[i]

    def __iter__(self):                 # for x in b
        return iter(self.items)


# ---------- ارث‌بری (inheritance) ----------
class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f'hi, I am {self.name}'

class Teacher(Person):                  # Teacher از Person ارث می‌بره
    def __init__(self, name, course):
        super().__init__(name)          # صدا زدن سازنده‌ی پدر
        self.course = course

    def hello(self):                    # override: بازنویسی متد پدر
        return super().hello() + f' and I teach {self.course}'

t = Teacher('ali', 'math')
isinstance(t, Person)                   # True


# ---------- چند شکلی (polymorphism) ----------
# یه متد با یه اسم، رفتار متفاوت تو کلاس‌های مختلف
class Cat:
    def speak(self):
        return 'meow'

class Dog:
    def speak(self):
        return 'woof'

for animal in [Cat(), Dog()]:
    print(animal.speak())               # هر کدوم به روش خودش


# ---------- classmethod ----------
# اولین ورودی cls (خود کلاس). معمولاً برای ساخت آبجکت از راه دیگه
class Task:
    def __init__(self, title, is_done=False):
        self.title = title
        self.is_done = is_done

    @classmethod
    def from_string(cls, text):
        title, is_done = text.split(',')
        return cls(title.strip(), is_done.strip() == 'True')
# Task.from_string('sleep, False')


# ---------- staticmethod ----------
# نه self می‌گیره نه cls؛ فقط یه تابع معمولیه که تو کلاس نشسته
class Checker:
    @staticmethod
    def is_valid(title):
        return title.strip() != ''
# Checker.is_valid('abc')


# ---------- کلاس انتزاعی (abstract class) ----------
# پدر می‌گه «این متد باید باشه»، بچه‌ها حتماً باید بنویسنش
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
# Shape()  → ارور (نمی‌شه از کلاس انتزاعی آبجکت ساخت)


# ---------- property + getter/setter ----------
# _radius = مقدار واقعی (داخل کلاس)   radius = دروازه‌ی بیرونی
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):                   # getter
        return self._radius

    @radius.setter
    def radius(self, value):            # setter (با چک کردن)
        if value <= 0:
            raise ValueError('radius must be positive')
        self._radius = value

    @property
    def area(self):                     # فقط‌خواندنی
        return 3.14 * self._radius ** 2


# ##########################################################
#                         Git
# ##########################################################
# git status                  وضعیت فایل‌ها
# git diff                    چی عوض شده
# git add file.py             آماده‌ی commit
# git commit -m "message"     ثبت تغییرات
# git push                    فرستادن به GitHub


# ##########################################################
#          بعداً اضافه می‌شه (هنوز یاد نگرفتیم)
# ##########################################################
# private / public (دسترسی از بیرون کلاس)
# decorators (دکوریتورها، همون @ها)
# مثال‌های تکمیلی OOP