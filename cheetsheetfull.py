# ==========================================================================
#  چیت‌شیت کاملِ پایتون سارا 🌿  (نسخه‌ی کامل‌تر)
#  این فایل «مرجع»ه، اجراش نکن؛ فقط بخون و مثال‌ها رو خودت تایپ کن
#  علامت 🔜 یعنی «هنوز با هم کار نکردیم»
# ==========================================================================
#
#  فهرست
#  ---- بخش ۱: پایتون مقدماتی ----
#   1.  انواع داده‌ها          2.  عملگرها             3.  دستورات شرطی
#   4.  حلقه‌ها               5.  رشته (str)           6.  لیست (list)
#   7.  تاپل (tuple)          8.  دیکشنری (dict)       9.  مجموعه (set)
#   10. تابع - بخش اول        11. تابع - بخش دوم       12. تابع بازگشتی
#   13. عبارت لامبدا          14. مدیریت استثناء‌ها     15. فایل
#   16. عبارت‌های منظم (regex) 17. الگوریتم‌های مرتب‌سازی و جستجو
#  ---- بخش ۲: شی‌گرایی (OOP) ----
#   18. مفاهیم اولیه          19. متدهای Dunder        20. ارث‌بری
#   21. چند شکلی              22. classmethod و staticmethod
#   23. کلاس انتزاعی (abstract) 24. property و getter/setter
#   25. private/public 🔜     26. decorator 🔜          27. مثال‌های تکمیلی
#  ---- 28. Git ----
# ==========================================================================


# ##########################################################################
#                      بخش ۱: پایتون مقدماتی
# ##########################################################################


# ==========================================================================
# 1. انواع داده‌ها (data types)
# ==========================================================================
a = 5               # int      عدد صحیح
b = 3.14            # float    اعشاری
c = 2 + 3j          # complex  مختلط (کم استفاده)
d = True            # bool     True / False  (با حرف بزرگ!)
e = None            # NoneType «هیچی»
s = 'hello'         # str      رشته
L = [1, 2]          # list     لیست      (تغییرپذیر)
T = (1, 2)          # tuple    تاپل      (تغییرناپذیر)
D = {'a': 1}        # dict     دیکشنری
S = {1, 2}          # set      مجموعه

print(type(a))                 # <class 'int'>
print(isinstance(a, int))      # True  (چک کردن نوع)
print(isinstance(a, (int, float)))   # چند نوع با هم

# --- تبدیل نوع (type conversion) ---
int('7')            # 7
int(3.9)            # 3   (قطع می‌کنه، رند نمی‌کنه)
float('2.5')        # 2.5
str(100)            # '100'
bool(0)             # False
bool('')            # False
bool('False')       # True  ⚠️ هر متن غیرخالی True است!
list('abc')         # ['a', 'b', 'c']
tuple([1, 2])       # (1, 2)
set([1, 1, 2])      # {1, 2}
dict([('a', 1)])    # {'a': 1}
# int('abc') → ValueError

# --- مقادیر False (falsy): بقیه‌ی چیزها True هستن ---
# 0   0.0   ''   []   ()   {}   set()   None   False

# --- تغییرپذیر (mutable) و تغییرناپذیر (immutable) ---
# immutable: int float str tuple bool None frozenset
# mutable:   list dict set
x = [1, 2]
y = x               # ⚠️ هر دو به یک لیست اشاره می‌کنن!
y.append(3)
print(x)            # [1, 2, 3]
z = x.copy()        # کپی مستقل
x is y              # True  (همون آبجکت)
x is z              # False

# --- ورودی و خروجی ---
# name = input('name? ')         # همیشه str برمی‌گردونه!
# age = int(input('age? '))      # برای عدد باید تبدیل کنی
print('a', 'b', sep='-')         # a-b
print('hello', end='')           # بدون رفتن به خط بعد
print('x =', 5)

# --- توابع آماده‌ی عددی ---
abs(-5)             # 5
round(3.14159, 2)   # 3.14
round(2.5)          # 2  ⚠️ (رند بانکی: به زوج نزدیک‌تر)
min(3, 1, 2)        # 1
max([3, 1, 2])      # 3
sum([1, 2, 3])      # 6
pow(2, 3)           # 8
divmod(7, 2)        # (3, 1)  یعنی (خارج‌قسمت, باقی‌مانده)
len('abc')          # 3

# --- خطای اعشاری ---
0.1 + 0.2 == 0.3                 # False !
# import math
# math.isclose(0.1 + 0.2, 0.3)   # True

# --- اعداد با مبناهای دیگه ---
0b101   # 5 (دودویی)     0o17  # 15 (هشت‌هشتی)     0xff  # 255 (شانزدهی)
bin(5)  # '0b101'        hex(255)  # '0xff'
1_000_000                        # خوانایی بیشتر عدد بزرگ


# ==========================================================================
# 2. عملگرها (operators)
# ==========================================================================
# --- ریاضی ---
7 + 2       # 9
7 - 2       # 5
7 * 2       # 14
7 / 2       # 3.5   (همیشه float)
7 // 2      # 3     (تقسیم صحیح)
7 % 2       # 1     (باقی‌مانده)
2 ** 3      # 8     (توان)
-7 // 2     # -4    ⚠️ به سمت منفی بی‌نهایت گرد می‌شه
-7 % 2      # 1
'ab' * 3    # 'ababab'      [0] * 3  # [0, 0, 0]
'a' + 'b'   # 'ab'          [1] + [2]  # [1, 2]

# --- انتساب (assignment) ---
x = 5
x += 1      # x = x + 1       (همچنین -=  *=  /=  //=  %=  **=)
a, b = 1, 2          # انتساب هم‌زمان
a, b = b, a          # جابه‌جایی (swap)
a = b = 0            # هر دو صفر

# --- مقایسه (comparison) ---
5 == 5      # True      5 != 3   # True
5 > 3       # True      5 >= 5   # True
1 < x < 10  # مقایسه‌ی زنجیره‌ای (chained)
'a' < 'b'   # True (مقایسه‌ی حروف الفبایی/یونیکد)

# --- منطقی (logical) ---
True and False      # False
True or False       # True
not True            # False
# short-circuit: اگه جواب از سمت چپ معلوم شد، راست اجرا نمی‌شه
name = '' or 'default'      # 'default'   (or اولین Truthy رو برمی‌گردونه)
val = 5 and 10              # 10          (and آخرین رو برمی‌گردونه اگه همه Truthy)

# --- هویت (identity) و عضویت (membership) ---
a is b              # آیا هر دو دقیقاً یه آبجکتن؟   (برای None: x is None)
a is not b
'a' in 'cat'        # True
3 in [1, 2, 3]      # True
'k' in {'k': 1}     # True (روی کلیدها)
3 not in [1, 2]     # True

# --- بیتی (bitwise) — کم استفاده ---
5 & 3    # 1 (and)      5 | 3   # 7 (or)      5 ^ 3   # 6 (xor)
~5       # -6           1 << 3  # 8            16 >> 2 # 4

# --- اولویت (precedence) از زیاد به کم ---
# **  ←  (-x)  ←  * / // %  ←  + -  ←  مقایسه‌ها  ←  not  ←  and  ←  or
# اگه شک داشتی، پرانتز بذار!


# ==========================================================================
# 3. دستورات شرطی (conditionals)
# ==========================================================================
age = 20
if age < 13:
    print('child')
elif age < 18:
    print('teen')
elif age < 60:
    print('adult')
else:
    print('senior')

# شرط‌های ترکیبی
if age >= 18 and age < 60:   pass
if age < 18 or age > 60:     pass
if not (age > 18):           pass

# شرط تو در تو (nested)
if age > 18:
    if age < 30:
        print('young adult')

# چک کردن خالی بودن (روش پایتونی)
items = []
if not items:               # به جای len(items) == 0
    print('empty')
if items:                   # یعنی لیست پر است
    print('not empty')

# if یک‌خطی (ternary)
status = 'adult' if age >= 18 else 'child'

# pass = «هیچ کاری نکن» (جای خالی)
if age > 100:
    pass

# match-case (پایتون ۳.۱۰ به بعد، مثل switch)
cmd = 'start'
match cmd:
    case 'start':
        print('starting')
    case 'stop' | 'quit':
        print('stopping')
    case _:                 # بقیه حالت‌ها (default)
        print('unknown')

# چک کردن None
x = None
if x is None:
    print('no value')


# ==========================================================================
# 4. حلقه‌ها (loops)
# ==========================================================================
# --- for و range ---
for i in range(5):              # 0 1 2 3 4
    print(i)
for i in range(2, 5):           # 2 3 4
    pass
for i in range(0, 10, 2):       # 0 2 4 6 8  (گام ۲)
    pass
for i in range(5, 0, -1):       # 5 4 3 2 1  (معکوس)
    pass

# --- حلقه روی انواع داده ---
for ch in 'abc':                # حروف رشته
    pass
for item in [10, 20]:           # عضوهای لیست
    pass
for k in {'a': 1}:              # کلیدهای دیکشنری
    pass
for k, v in {'a': 1}.items():   # کلید و مقدار
    pass

# --- enumerate: شماره + مقدار ---
for i, name in enumerate(['ali', 'sara']):
    print(i, name)              # 0 ali / 1 sara
for i, name in enumerate(['ali', 'sara'], start=1):    # شروع از ۱
    pass

# --- zip: چند لیست هم‌زمان ---
for n, a in zip(['ali', 'sara'], [30, 20]):
    print(n, a)

# --- reversed و sorted ---
for x in reversed([1, 2, 3]):   # 3 2 1
    pass
for x in sorted([3, 1, 2]):     # 1 2 3
    pass

# --- while ---
n = 3
while n > 0:
    print(n)
    n -= 1

while True:                     # حلقه‌ی بی‌نهایت با خروج دستی
    ans = 'q'                   # (مثلاً input)
    if ans == 'q':
        break

# --- break / continue / else ---
for i in range(10):
    if i == 3:
        continue                # برو دور بعد
    if i == 6:
        break                   # از حلقه بیرون بیا
    print(i)
else:
    print('بدون break تموم شد')  # else فقط وقتی اجرا می‌شه که break نخورده باشه

# --- حلقه تو در تو (nested) ---
for i in range(3):
    for j in range(3):
        print(i, j)
# الگوی ستاره‌ای:
for i in range(1, 4):
    print('*' * i)

# --- comprehension ---
[x * 2 for x in range(5)]                    # [0, 2, 4, 6, 8]
[x for x in range(10) if x % 2 == 0]         # فقط زوج‌ها
[x if x > 0 else 0 for x in [-1, 2]]         # [0, 2]
{x: x**2 for x in range(3)}                  # دیکشنری
{x % 3 for x in range(10)}                   # مجموعه
[(i, j) for i in range(2) for j in range(2)] # دو حلقه

# ⚠️ تغییر دادن لیست وقتی روش حلقه می‌زنی کار درستی نیست؛ روی کپی حلقه بزن
for x in L[:]:
    pass


# ==========================================================================
# 5. رشته (string)
# ==========================================================================
s = 'Hello World'
# --- ایندکس و برش (slicing) ---
s[0]            # 'H'
s[-1]           # 'd'  (از آخر)
s[0:5]          # 'Hello'   (انتها شامل نمی‌شه)
s[:5]           # 'Hello'
s[6:]           # 'World'
s[::2]          # 'HloWrd' (گام ۲)
s[::-1]         # 'dlroW olleH'  (معکوس)
len(s)          # 11
# s[0] = 'h'    # ارور! رشته immutable است

# --- ساخت رشته ---
'single'  "double"  '''چند
خطی'''
'it\'s'  "it's"                  # علامت نقل‌قول داخل رشته
'a\nb'   # خط جدید       'a\tb'  # تب
r'C:\new\table'                  # raw: بک‌اسلش معنی خاص نداره
'ab' + 'cd'   'ab' * 3           # جمع و ضرب

# --- متدهای حروف ---
s.lower()           # 'hello world'
s.upper()           # 'HELLO WORLD'
s.capitalize()      # 'Hello world'
s.title()           # 'Hello World'
s.swapcase()        # 'hELLO wORLD'

# --- پاکسازی ---
'  hi  '.strip()    # 'hi'
'  hi  '.lstrip()   # 'hi  '
'  hi  '.rstrip()   # '  hi'
'xxhixx'.strip('x') # 'hi'

# --- جستجو ---
s.find('o')         # 4   (اولین جا؛ نبود → -1)
s.rfind('o')        # 7   (از آخر)
s.index('o')        # 4   (نبود → ValueError)
s.count('o')        # 2
s.startswith('He')  # True
s.endswith('d')     # True
'lo' in s           # True

# --- تغییر ---
s.replace('World', 'Sara')        # 'Hello Sara'
s.replace('l', 'L', 1)            # فقط اولی
'a,b,c'.split(',')                # ['a', 'b', 'c']
'a b  c'.split()                  # ['a', 'b', 'c'] (روی هر فاصله)
'a,b,c'.split(',', 1)             # ['a', 'b,c']
'a\nb'.splitlines()               # ['a', 'b']
'-'.join(['a', 'b', 'c'])         # 'a-b-c'
''.join(['a', 'b'])               # 'ab'
'5'.zfill(3)                      # '005'
'hi'.center(10, '*')              # '****hi****'
'hi'.ljust(5) + '|'               # 'hi   |'
'hi'.rjust(5)                     # '   hi'

# --- چک کردن نوع محتوا ---
'123'.isdigit()     # True
'abc'.isalpha()     # True
'abc1'.isalnum()    # True
'  '.isspace()      # True
'abc'.islower()     # True
'ABC'.isupper()     # True

# --- قالب‌بندی (formatting) ---
name, age = 'sara', 20
f'name: {name}, age: {age}'         # f-string (بهترین)
f'{3.14159:.2f}'                    # '3.14'
f'{5:03d}'                          # '005'
f'{1234567:,}'                      # '1,234,567'
f'{name!r}'                         # 'sara' با کوتیشن
f'{age + 1}'                        # حتی عبارت داخلش می‌شه
'{} is {}'.format(name, age)        # روش قدیمی‌تر
'%s is %d' % (name, age)            # روش خیلی قدیمی

# --- کد کاراکتر ---
ord('a')        # 97
chr(97)         # 'a'

# --- حلقه روی رشته و شمارش ---
for ch in 'abc': pass
vowels = sum(1 for ch in 'hello' if ch in 'aeiou')   # 2
# چک پالیندروم:
w = 'level'
w == w[::-1]    # True


# ==========================================================================
# 6. لیست (list)
# ==========================================================================
L = [10, 20, 30, 40]
# --- دسترسی ---
L[0]            # 10
L[-1]           # 40
L[1:3]          # [20, 30]
L[::-1]         # معکوس (کپی جدید)
L[0] = 99       # تغییر

# --- اضافه کردن ---
L.append(5)             # آخر
L.insert(1, 15)         # جای مشخص
L.extend([6, 7])        # چند عضو به آخر
L + [8, 9]              # لیست جدید
[0] * 3                 # [0, 0, 0]

# --- حذف ---
L.remove(15)            # اولین مقدار 15 (نبود → ValueError)
L.pop()                 # آخری رو حذف و برمی‌گردونه
L.pop(0)                # عضو شماره‌ی 0
del L[0]                # حذف با ایندکس
del L[1:3]              # حذف بازه
L.clear()               # خالی کردن

L = [3, 1, 2, 3]
# --- جستجو و آمار ---
L.index(3)              # 0   (اولین جا؛ نبود → ValueError)
L.count(3)              # 2
3 in L                  # True
len(L); min(L); max(L); sum(L)

# --- مرتب‌سازی ---
L.sort()                        # خود لیست عوض می‌شه، None برمی‌گردونه
L.sort(reverse=True)            # نزولی
sorted(L)                       # لیست جدید (اصلی دست‌نخورده)
L.sort(key=len)                 # بر اساس طول (برای لیست رشته‌ها)
L.reverse()                     # معکوس خود لیست
words = ['bb', 'a', 'ccc']
sorted(words, key=lambda w: len(w))             # ['a', 'bb', 'ccc']
people = [{'n': 'ali', 'a': 30}, {'n': 'sara', 'a': 20}]
sorted(people, key=lambda p: p['a'])            # بر اساس سن

# --- کپی ---
A = [1, 2, [3, 4]]
B = A                   # ⚠️ همون لیست
C = A.copy()            # کپی سطحی (shallow)  یا A[:]  یا list(A)
# import copy
# D = copy.deepcopy(A)  # کپی کامل (برای لیست تو در تو)

# --- لیست تو در تو / ماتریس ---
M = [[1, 2, 3], [4, 5, 6]]
M[1][2]                 # 6
for row in M:
    for x in row:
        pass
grid = [[0] * 3 for _ in range(2)]      # ✅ درست
bad = [[0] * 3] * 2                     # ❌ هر دو ردیف یکی هستن!

# --- باز کردن (unpacking) ---
a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4]             # first=1, rest=[2,3,4]
first, *mid, last = [1, 2, 3, 4]        # mid=[2,3]

# --- ابزارهای کمکی ---
list(range(5))                          # [0, 1, 2, 3, 4]
list(zip([1, 2], ['a', 'b']))           # [(1,'a'), (2,'b')]
any([0, 0, 1])                          # True  (حداقل یکی True)
all([1, 1, 0])                          # False (همه باید True)
list(set([1, 1, 2]))                    # حذف تکراری
# لیست به عنوان stack (آخرین ورودی، اولین خروجی): append + pop
# لیست به عنوان queue (صف): append + pop(0)  (یا collections.deque)


# ==========================================================================
# 7. تاپل (tuple)
# ==========================================================================
T = (1, 2, 3)
T = 1, 2, 3             # پرانتز اختیاریه
one = (5,)              # ⚠️ تاپل تک‌عضوی: ویرگول لازمه!  (5) فقط عدده
empty = ()
T[0]                    # 1
T[-1]                   # 3
T[0:2]                  # (1, 2)
len(T); min(T); max(T); sum(T)
T.count(2)              # 1
T.index(3)              # 2
2 in T                  # True
T + (4,)                # (1, 2, 3, 4)  (تاپل جدید)
# T[0] = 9              # ارور! تغییرناپذیره

# --- unpacking ---
a, b, c = T
a, *rest = T
a, b = b, a             # swap (در واقع تاپل‌سازی و باز کردنه)

# --- کاربردها ---
# 1) برگردوندن چند مقدار از تابع:  return a, b
# 2) کلید دیکشنری (چون hashable است):  d = {(1, 2): 'point'}
# 3) داده‌ی ثابتی که نباید عوض بشه
# اگه عضوش mutable باشه (مثلاً لیست)، خود اون عضو قابل تغییره:
t = ([1, 2], 3)
t[0].append(9)          # کار می‌کنه
# import collections
# Point = collections.namedtuple('Point', 'x y');  p = Point(1, 2);  p.x


# ==========================================================================
# 8. دیکشنری (dict)
# ==========================================================================
D = {'name': 'sara', 'age': 20}
empty = {}                              # ⚠️ این دیکشنری خالیه (نه set)
D = dict(name='sara', age=20)           # روش دیگه

# --- خوندن ---
D['name']                   # 'sara'   (نبود → KeyError)
D.get('city')               # None     (نبود → None، بدون ارور)
D.get('city', 'unknown')    # مقدار پیش‌فرض
'name' in D                 # True (چک کلید)
len(D)

# --- اضافه / تغییر ---
D['city'] = 'tehran'        # اضافه یا تغییر
D.update({'age': 21, 'job': 'student'})     # چند تا با هم
D.setdefault('x', 0)        # اگه نبود بساز و برگردون
D = D | {'z': 1}            # ادغام (پایتون ۳.۹+)

# --- حذف ---
D.pop('city')               # حذف و برگردوندن مقدار
D.pop('nokey', None)        # بدون ارور
del D['job']
D.popitem()                 # آخرین جفت
D.clear()

D = {'a': 1, 'b': 2, 'c': 3}
# --- پیمایش ---
D.keys()                    # کلیدها
D.values()                  # مقادیر
D.items()                   # جفت‌های (کلید, مقدار)
for k in D: pass
for k, v in D.items(): pass
list(D.keys())              # تبدیل به لیست

# --- ساخت و تبدیل ---
dict.fromkeys(['a', 'b'], 0)            # {'a': 0, 'b': 0}
dict(zip(['a', 'b'], [1, 2]))           # {'a': 1, 'b': 2}
{k: v * 2 for k, v in D.items()}        # comprehension
{k: v for k, v in D.items() if v > 1}   # با شرط
{v: k for k, v in D.items()}            # جابه‌جا کردن کلید و مقدار
D.copy()                                # کپی سطحی

# --- دیکشنری تو در تو ---
students = {
    'ali':  {'age': 30, 'grades': [18, 20]},
    'sara': {'age': 20, 'grades': [19, 17]},
}
students['sara']['grades'][0]           # 19

# --- مرتب‌سازی ---
sorted(D)                               # کلیدهای مرتب
sorted(D.items(), key=lambda kv: kv[1]) # بر اساس مقدار
sorted(D.items(), key=lambda kv: kv[1], reverse=True)
max(D, key=D.get)                       # کلیدی که بزرگ‌ترین مقدار رو داره

# --- شمارش (الگوی خیلی پرکاربرد) ---
counts = {}
for ch in 'banana':
    counts[ch] = counts.get(ch, 0) + 1  # {'b':1, 'a':3, 'n':2}
# کلید باید hashable باشه: str, int, tuple اوکی — list و dict نه


# ==========================================================================
# 9. مجموعه (set)
# ==========================================================================
S = {1, 2, 3}
empty = set()               # ⚠️ {} دیکشنریه! برای set خالی باید set() بنویسی
set([1, 1, 2])              # {1, 2}   (تکراری‌ها حذف می‌شن)
# بدون ترتیب است و ایندکس نداره (S[0] ارور)

# --- اضافه / حذف ---
S.add(4)
S.update([5, 6])            # چند تا
S.remove(1)                 # نبود → KeyError
S.discard(99)               # نبود → بدون ارور
S.pop()                     # یکی تصادفی رو حذف می‌کنه
S.clear()

A, B = {1, 2, 3}, {2, 3, 4}
# --- عملیات مجموعه‌ای ---
A | B                       # اجتماع        {1,2,3,4}   (A.union(B))
A & B                       # اشتراک        {2,3}       (A.intersection(B))
A - B                       # تفاضل         {1}         (A.difference(B))
A ^ B                       # تفاضل متقارن  {1,4}       (A.symmetric_difference(B))
# --- مقایسه ---
{1} <= A                    # زیرمجموعه     (A.issubset)
A >= {1}                    # فرامجموعه     (A.issuperset)
A.isdisjoint({9})           # هیچ اشتراکی ندارن؟
2 in A                      # چک عضویت (خیلی سریع)

# --- کاربردها ---
list(set([3, 1, 3, 2]))     # حذف تکراری (ترتیب حفظ نمی‌شه)
len(set('hello'))           # تعداد حروف متفاوت = 4
{x for x in range(10) if x % 2 == 0}    # comprehension
frozenset([1, 2])           # set تغییرناپذیر (می‌تونه کلید دیکشنری بشه)
# عضوهای set باید hashable باشن (لیست نمی‌تونه عضو set بشه)


# ==========================================================================
# 10. تابع - بخش اول (functions)
# ==========================================================================
def add(a, b):
    """جمع دو عدد (docstring: توضیح تابع)"""
    return a + b

add(2, 3)                       # 5
# بدون return، تابع None برمی‌گردونه

# --- آرگومان‌ها ---
def greet(name, greeting='hi'):     # greeting مقدار پیش‌فرض داره
    return f'{greeting} {name}'

greet('sara')                       # 'hi sara'
greet('sara', 'hello')              # موقعیتی (positional)
greet(greeting='yo', name='sara')   # نام‌دار (keyword) — ترتیب مهم نیست
# قانون: پارامترهای بدون پیش‌فرض اول، با پیش‌فرض بعدش

# --- برگردوندن چند مقدار (در واقع یه تاپل) ---
def min_max(L):
    return min(L), max(L)
lo, hi = min_max([3, 1, 2])

# --- return زودهنگام ---
def is_even(n):
    if n % 2 == 0:
        return True
    return False                    # (ساده‌تر: return n % 2 == 0)

# --- ⚠️ دام پیش‌فرض تغییرپذیر ---
def bad(x, L=[]):                   # ❌ لیست بین فراخوانی‌ها مشترک می‌مونه
    L.append(x)
    return L
def good(x, L=None):                # ✅
    if L is None:
        L = []
    L.append(x)
    return L

# --- محدوده‌ی متغیر (scope): Local → Enclosing → Global → Built-in ---
x = 10                              # سراسری (global)
def f():
    x = 5                           # محلی؛ x بیرونی دست‌نخورده می‌مونه
    return x

# --- type hint (راهنمای نوع، اجباری نیست) ---
def area(w: float, h: float) -> float:
    return w * h

# --- تغییر آرگومان‌های mutable ---
def add_item(L):
    L.append(1)                     # لیست اصلی عوض می‌شه!
# اعداد/رشته/تاپل (immutable) از بیرون عوض نمی‌شن

# --- تابع بدون ورودی/خروجی ---
def hello():
    print('hello')                  # فقط چاپ می‌کنه (return نداره)


# ==========================================================================
# 11. تابع - بخش دوم
# ==========================================================================
# --- *args: هر تعداد آرگومان موقعیتی (تاپل) ---
def total(*args):
    return sum(args)
total(1, 2, 3)                      # 6

# --- **kwargs: هر تعداد آرگومان نام‌دار (دیکشنری) ---
def info(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
info(name='sara', age=20)

# --- ترکیب همه (ترتیب مهمه) ---
def f(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)
f(1, 2, 3, 4, x=5)                  # 1 2 (3, 4) {'x': 5}

# --- باز کردن موقع صدا زدن ---
nums = [1, 2, 3]
total(*nums)                        # مثل total(1, 2, 3)
data = {'name': 'sara', 'age': 20}
info(**data)                        # مثل info(name=..., age=...)

# --- keyword-only: بعد از * فقط نام‌دار ---
def g(a, *, b):
    return a + b
g(1, b=2)                           # g(1, 2) ارور می‌ده

# --- global و nonlocal ---
counter = 0
def inc():
    global counter                  # تغییر متغیر سراسری از داخل تابع
    counter += 1                    # بدون global → UnboundLocalError

def outer():
    n = 0
    def inner():
        nonlocal n                  # تغییر متغیر تابع بیرونی
        n += 1
        return n
    return inner
c = outer()
c(); c()                            # 1, 2   (closure: داخلی n رو یادش می‌مونه)

# --- تابع داخل تابع ---
def power(n):
    def calc(x):
        return x ** n
    return calc
square = power(2)
square(5)                           # 25

# --- تابع هم یه آبجکته: می‌شه ذخیره کرد، پاس داد ---
def apply(func, x):
    return func(x)
apply(len, 'abc')                   # 3
ops = {'add': lambda a, b: a + b, 'mul': lambda a, b: a * b}
ops['add'](2, 3)                    # 5

# --- توابع آماده‌ی مفید با تابع ---
list(map(str, [1, 2, 3]))                       # ['1', '2', '3']
list(map(lambda x: x * 2, [1, 2, 3]))           # [2, 4, 6]
list(filter(lambda x: x > 1, [1, 2, 3]))        # [2, 3]
# import functools; functools.reduce(lambda a, b: a + b, [1, 2, 3])   # 6
sorted([3, 1, 2], key=lambda x: -x)             # [3, 2, 1]


# ==========================================================================
# 12. تابع بازگشتی (recursion)
# ==========================================================================
# قانون طلایی: ۱) شرط توقف (base case)  ۲) نزدیک شدن به شرط توقف
def factorial(n):
    if n <= 1:                      # شرط توقف
        return 1
    return n * factorial(n - 1)     # قدم بازگشتی
factorial(5)                        # 120

def fib(n):                         # فیبوناچی
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)  # کند! (محاسبه‌ی تکراری)

memo = {}
def fib_fast(n):                    # با حافظه (memoization)
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib_fast(n - 1) + fib_fast(n - 2)
    return memo[n]

def sum_list(L):                    # جمع لیست
    if not L:
        return 0
    return L[0] + sum_list(L[1:])

def reverse(s):                     # معکوس رشته
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]

def power(a, n):                    # توان
    if n == 0:
        return 1
    return a * power(a, n - 1)

def countdown(n):                   # چاپ ۳ ۲ ۱
    if n == 0:
        return
    print(n)
    countdown(n - 1)

def flatten(L):                     # لیست تو در تو → تخت
    res = []
    for x in L:
        if isinstance(x, list):
            res += flatten(x)
        else:
            res.append(x)
    return res
flatten([1, [2, [3, 4]], 5])        # [1, 2, 3, 4, 5]

def binary_search(L, x, lo, hi):    # جستجوی دودویی (L مرتب)
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if L[mid] == x:
        return mid
    if L[mid] < x:
        return binary_search(L, x, mid + 1, hi)
    return binary_search(L, x, lo, mid - 1)

# import sys; sys.getrecursionlimit()   # حدود 1000 — بی‌نهایت → RecursionError
# هر بازگشتی رو می‌شه با حلقه هم نوشت؛ حلقه معمولاً سریع‌تره


# ==========================================================================
# 13. عبارت لامبدا (lambda)
# ==========================================================================
# lambda ورودی‌ها: عبارت       (فقط یه عبارت؛ return خودکار است)
square = lambda x: x ** 2
add = lambda a, b: a + b
greet = lambda name='friend': f'hi {name}'      # پیش‌فرض هم داره
sign = lambda x: 'pos' if x > 0 else 'neg'      # با شرط
(lambda x: x + 1)(5)                            # صدا زدن مستقیم → 6

# کاربرد اصلی ۱: key در sorted / sort / min / max
people = [('ali', 30), ('sara', 20), ('reza', 25)]
sorted(people, key=lambda p: p[1])              # بر اساس سن
sorted(people, key=lambda p: p[1], reverse=True)
max(people, key=lambda p: p[1])                 # بزرگ‌ترین بر اساس سن
sorted(['bb', 'a', 'ccc'], key=lambda s: len(s))
sorted(people, key=lambda p: (p[1], p[0]))      # چند معیار (اول سن بعد اسم)

# کاربرد ۲: map / filter / reduce
list(map(lambda x: x * 2, [1, 2, 3]))           # [2, 4, 6]
list(filter(lambda x: x % 2 == 0, range(6)))    # [0, 2, 4]
# from functools import reduce
# reduce(lambda a, b: a * b, [1, 2, 3, 4])      # 24

# کاربرد ۳: ذخیره توی لیست/دیکشنری
ops = {'+': lambda a, b: a + b, '-': lambda a, b: a - b}
ops['+'](2, 3)                                  # 5

# محدودیت‌ها: فقط یک عبارت؛ نه چند خطی، نه انتساب. کار پیچیده‌تر → def بنویس
# comprehension معمولاً از map/filter خواناتره: [x * 2 for x in L]


# ==========================================================================
# 14. مدیریت استثناء‌ها (exceptions)
# ==========================================================================
# --- ساختار کامل ---
try:
    x = int(input('number: '))
    y = 10 / x
except ValueError:                  # متن به عدد تبدیل نشد
    print('not a number')
except ZeroDivisionError:           # تقسیم بر صفر
    print('zero!')
except (TypeError, KeyError) as e:  # چند نوع با هم + گرفتن پیام
    print('error:', e)
except Exception as e:              # هر ارور دیگه (آخر از همه!)
    print('unexpected:', e)
else:                               # فقط اگه ارور نیومد
    print('result', y)
finally:                            # همیشه (بستن فایل و ...)
    print('done')
# ⚠️ except: خالی (بدون نوع) همه‌چیز رو قورت می‌ده؛ استفاده نکن
# ترتیب except مهمه: اختصاصی اول، عمومی (Exception) آخر

# --- ارورهای رایج و علتشون ---
# ValueError         مقدار نامناسب            int('abc')
# TypeError          نوع نامناسب              '2' + 2
# KeyError           کلید نبود                {}['a']
# IndexError         ایندکس خارج از لیست      [1][5]
# ZeroDivisionError  تقسیم بر صفر             1 / 0
# FileNotFoundError  فایل پیدا نشد            open('nofile.txt')
# AttributeError     ویژگی/متد نیست           'a'.foo()
# NameError          متغیر تعریف نشده         print(zzz)
# ImportError        ماژول پیدا نشد           import nomodule
# IndentationError   تو رفتگی اشتباه
# RecursionError     بازگشتی بی‌نهایت

# --- raise: ارور درست کردن ---
def set_age(age):
    if age < 0:
        raise ValueError('age must be positive')
    return age

try:
    set_age(-1)
except ValueError as e:
    print(e)                        # age must be positive

# raise خالی داخل except: همون ارور رو دوباره پرتاب می‌کنه
try:
    try:
        1 / 0
    except ZeroDivisionError:
        print('logging...')
        raise
except ZeroDivisionError:
    print('caught again')

# --- ارور اختصاصی (custom exception) ---
class InsufficientFunds(Exception):
    pass

class NegativeAmount(Exception):
    def __init__(self, amount):
        super().__init__(f'bad amount: {amount}')
        self.amount = amount

# raise InsufficientFunds('not enough money')

# --- assert: چک کردن فرض‌ها (برای اشکال‌یابی) ---
assert 2 + 2 == 4
assert isinstance(5, int), 'must be int'    # False بشه → AssertionError با این پیام

# --- حلقه‌ی «تا وقتی ورودی درست بده» ---
while True:
    try:
        n = int(input('number: '))
        break
    except ValueError:
        print('try again')

# --- try تو در تو و with هم برای مدیریت منابع است (بخش فایل) ---


# ==========================================================================
# 15. فایل (files)
# ==========================================================================
# حالت‌های باز کردن (mode):
#   'r'  خوندن (پیش‌فرض؛ فایل نباشه → FileNotFoundError)
#   'w'  نوشتن (فایل رو از اول پاک می‌کنه! نباشه می‌سازه)
#   'a'  اضافه به آخر (append)
#   'x'  ساختن (فایل باشه → ارور)
#   'r+' خوندن و نوشتن
#   'b'  باینری ('rb', 'wb') برای عکس و غیره
# ⚠️ برای فارسی حتماً encoding='utf-8'

# --- نوشتن ---
with open('a.txt', 'w', encoding='utf-8') as f:
    f.write('سلام\n')               # \n خودت باید بذاری
    f.writelines(['x\n', 'y\n'])    # لیستی از رشته‌ها

with open('a.txt', 'a', encoding='utf-8') as f:
    f.write('more\n')

# --- خوندن ---
with open('a.txt', 'r', encoding='utf-8') as f:
    text = f.read()                 # همه‌ی متن یک‌جا
with open('a.txt', encoding='utf-8') as f:
    first = f.readline()            # یک خط
with open('a.txt', encoding='utf-8') as f:
    lines = f.readlines()           # لیست خط‌ها (با \n)
with open('a.txt', encoding='utf-8') as f:
    for line in f:                  # خط‌به‌خط (بهترین برای فایل بزرگ)
        print(line.strip())         # strip: حذف \n آخر هر خط
    # f.read(5) پنج کاراکتر؛  f.seek(0) برگشت به اول؛  f.tell() موقعیت فعلی

# --- چرا with؟ خودش فایل رو می‌بنده، حتی اگه ارور بیاد ---
# روش قدیمی: f = open(...); ...; f.close()

# --- چک کردن وجود فایل / پوشه ---
import os
os.path.exists('a.txt')             # True/False
os.path.isfile('a.txt')
os.remove('a.txt')                  # حذف فایل
os.listdir('.')                     # لیست فایل‌های پوشه
# from pathlib import Path;  Path('a.txt').exists();  Path('a.txt').read_text(encoding='utf-8')

# --- مدیریت ارور فایل ---
try:
    with open('nofile.txt') as f:
        data = f.read()
except FileNotFoundError:
    print('file not found')
except PermissionError:
    print('no permission')

# --- JSON: ذخیره‌ی لیست/دیکشنری ---
import json
data = [{'title': 'read', 'is_done': False}]
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)    # ensure_ascii=False برای فارسی
with open('data.json', encoding='utf-8') as f:
    data = json.load(f)
s = json.dumps(data)                # به رشته
data = json.loads(s)                # از رشته

# --- CSV ---
import csv
with open('a.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['name', 'age'])
    w.writerow(['sara', 20])
with open('a.csv', encoding='utf-8') as f:
    for row in csv.reader(f):       # هر ردیف یه لیسته
        print(row)
with open('a.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):   # هر ردیف یه دیکشنری
        print(row['name'])

# --- الگوی پرکاربرد: ذخیره/بارگذاری Todo ---
# ذخیره:  [{'title': t.title, 'is_done': t.is_done} for t in todo.tasks] → json.dump
# بارگذاری: json.load → برای هر دیکشنری Task(d['title'], d['is_done']) بساز


# ==========================================================================
# 16. عبارت‌های منظم (regex)
# ==========================================================================
import re

# --- توابع اصلی ---
re.search(r'\d+', 'abc 123 x')      # اولین تطابق «هرجای» متن → آبجکت match یا None
re.match(r'\d+', '123abc')          # فقط از «اول» متن
re.fullmatch(r'\d{4}', '2026')      # «کل» متن باید تطابق داشته باشه
re.findall(r'\d+', 'a1 b22 c333')   # ['1', '22', '333']
re.finditer(r'\d+', 'a1 b22')       # تکرارکننده‌ی match ها
re.sub(r'\s+', ' ', 'a   b  c')     # جایگزینی → 'a b c'
re.split(r'[,;]', 'a,b;c')          # ['a', 'b', 'c']
re.escape('a.b')                    # 'a\\.b' (کاراکتر خاص رو عادی می‌کنه)

m = re.search(r'(\d+)-(\d+)', 'tel 021-1234')
if m:                               # همیشه چک کن None نباشه
    m.group()                       # '021-1234' (کل تطابق)
    m.group(1)                      # '021'
    m.groups()                      # ('021', '1234')
    m.start(); m.end(); m.span()    # موقعیت تطابق

# --- الگوها ---
#  .      هر کاراکتر (به جز \n)         \.   خود نقطه
#  \d     رقم          \D  غیر رقم
#  \w     حرف/رقم/_    \W  غیر آن
#  \s     فاصله/تب/خط  \S  غیر آن
#  ^      شروع          $   پایان          \b  مرز کلمه
#  [abc]  یکی از a,b,c   [a-z]  بازه       [^abc]  هر چیز جز این‌ها
#  a|b    a یا b          (...)  گروه
# --- تکرار ---
#  *      صفر یا بیشتر       +   یک یا بیشتر      ?   صفر یا یک
#  {3}    دقیقاً ۳ بار       {2,4}  بین ۲ و ۴      {2,}  حداقل ۲
#  *? +?  حالت غیرحریص (non-greedy: کوتاه‌ترین تطابق)

# --- گروه نام‌دار ---
m = re.search(r'(?P<year>\d{4})-(?P<month>\d{2})', '2026-11')
m.group('year')                     # '2026'
m.groupdict()                       # {'year': '2026', 'month': '11'}

# --- حریص و غیرحریص ---
re.findall(r'<.+>', '<a><b>')       # ['<a><b>']   (حریص: بلندترین)
re.findall(r'<.+?>', '<a><b>')      # ['<a>', '<b>']  (غیرحریص)

# --- flags ---
re.search('hello', 'HELLO', re.IGNORECASE)      # بدون حساسیت به بزرگی/کوچکی (re.I)
# re.MULTILINE (re.M): ^ و $ برای هر خط   re.DOTALL (re.S): . شامل \n هم بشه

# --- compile: الگو رو یک‌بار بساز، چندبار استفاده کن ---
pat = re.compile(r'\d+')
pat.findall('a1 b22')

# --- الگوهای آماده ---
EMAIL   = r'[\w.+-]+@[\w-]+\.[\w.]+'
PHONE   = r'09\d{9}'                # موبایل ایران
DIGITS  = r'\d+'
DATE    = r'\d{4}/\d{2}/\d{2}'
re.fullmatch(EMAIL, 'sara@mail.com')            # تطابق دارد
re.sub(r'\d', '#', 'tel 123')                   # 'tel ###'
# همیشه الگو رو raw string بنویس: r'...'  (تا \d معنی خاص نشه)


# ==========================================================================
# 17. الگوریتم‌های مرتب‌سازی و جستجو
# ==========================================================================
# --- Bubble sort: همسایه‌ها رو مقایسه و جابه‌جا می‌کنه — O(n²) ---
def bubble_sort(L):
    n = len(L)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                swapped = True
        if not swapped:             # اگه جابه‌جایی نشد، مرتبه
            break
    return L

# --- Selection sort: هر بار کوچک‌ترین رو می‌ذاره سر جاش — O(n²) ---
def selection_sort(L):
    for i in range(len(L)):
        m = i
        for j in range(i + 1, len(L)):
            if L[j] < L[m]:
                m = j
        L[i], L[m] = L[m], L[i]
    return L

# --- Insertion sort: مثل مرتب کردن ورق بازی — O(n²) ---
def insertion_sort(L):
    for i in range(1, len(L)):
        key = L[i]
        j = i - 1
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key
    return L

# --- Merge sort: تقسیم، مرتب، ادغام — O(n log n) ---
def merge_sort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left, right = merge_sort(L[:mid]), merge_sort(L[mid:])
    res, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    return res + left[i:] + right[j:]

# --- Quick sort: یه pivot انتخاب، کوچیک‌ترا چپ، بزرگ‌ترا راست — میانگین O(n log n) ---
def quick_sort(L):
    if len(L) <= 1:
        return L
    pivot = L[0]
    less = [x for x in L[1:] if x < pivot]
    more = [x for x in L[1:] if x >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(more)

# --- جستجوی خطی و دودویی ---
def linear_search(L, x):            # O(n)
    for i, v in enumerate(L):
        if v == x:
            return i
    return -1

def binary_search_iter(L, x):       # O(log n) — لیست باید «مرتب» باشه
    lo, hi = 0, len(L) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if L[mid] == x:
            return mid
        if L[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# تو کار واقعی از sorted() / .sort() استفاده کن (Timsort، پایدار و سریع)
# پایدار (stable) یعنی عضوهای مساوی ترتیبشون عوض نمی‌شه


# ##########################################################################
#                      بخش ۲: شی‌گرایی (OOP)
# ##########################################################################


# ==========================================================================
# 18. مفاهیم اولیه شی‌گرایی
# ==========================================================================
# class = نقشه        object (instance) = چیزی که از نقشه ساخته می‌شه
class Student:
    school = 'MyUni'                    # ویژگی کلاس: بین همه‌ی آبجکت‌ها مشترک
    count = 0

    def __init__(self, name, grade=0):  # سازنده (constructor): موقع ساختن آبجکت
        self.name = name                # ویژگی آبجکت: مخصوص همین آبجکت
        self.grade = grade
        Student.count += 1              # شمردن آبجکت‌ها با ویژگی کلاس

    def show(self):                     # متد (method): تابع داخل کلاس
        return f'{self.name}: {self.grade}'

    def improve(self, amount):
        self.grade += amount            # تغییر ویژگی آبجکت

s1 = Student('sara', 19)
s2 = Student('ali')
s1.show()                               # 'sara: 19'
s1.grade = 20                           # تغییر مستقیم ویژگی
s1.school                               # 'MyUni' (از کلاس)
Student.count                           # 2
# self = خود آبجکتی که متد روش صدا زده شده (لازم نیست موقع صدا زدن بدی)
# s1.show() یعنی Student.show(s1)

# --- ابزارهای مفید ---
type(s1)                                # <class 'Student'>
isinstance(s1, Student)                 # True
hasattr(s1, 'name')                     # True
getattr(s1, 'name')                     # 'sara'
setattr(s1, 'age', 20)                  # ساخت/تغییر ویژگی
s1.__dict__                             # دیکشنری ویژگی‌های آبجکت
# del s1.grade                          # حذف ویژگی

# --- ⚠️ دام: ویژگی کلاس mutable مشترکه ---
class Bad:
    items = []                          # ❌ بین همه‌ی آبجکت‌ها مشترک است
class Good:
    def __init__(self):
        self.items = []                 # ✅ مخصوص هر آبجکت

# --- آبجکت‌ها داخل هم (composition: «دارد») ---
class Task:
    def __init__(self, title, is_done=False):
        self.title = title
        self.is_done = is_done

class TodoList:
    def __init__(self):
        self.tasks = []                 # TodoList «چند Task داره»
    def add(self, title):
        self.tasks.append(Task(title))


# ==========================================================================
# 19. متدهای Dunder (سربارگذاری / overloading)
# ==========================================================================
# dunder = double underscore. پایتون خودش صداشون می‌زنه؛ ما فقط تعریفشون می‌کنیم
class Box:
    def __init__(self, items):
        self.items = list(items)

    # --- نمایش ---
    def __str__(self):                  # print(b) و str(b)   (برای کاربر)
        return f'Box({self.items})'
    def __repr__(self):                 # نمایش دقیق (برای برنامه‌نویس/دیباگ)
        return f'Box({self.items!r})'

    # --- اندازه و عضویت ---
    def __len__(self):                  # len(b)  (باید int برگردونه)
        return len(self.items)
    def __contains__(self, x):          # x in b
        return x in self.items
    def __bool__(self):                 # if b:   (اگه نباشه، از __len__ استفاده می‌شه)
        return len(self.items) > 0

    # --- شاخص‌گذاری ---
    def __getitem__(self, i):           # b[0]   b[1:3]
        return self.items[i]
    def __setitem__(self, i, v):        # b[0] = 5
        self.items[i] = v
    def __delitem__(self, i):           # del b[0]
        del self.items[i]

    # --- پیمایش ---
    def __iter__(self):                 # for x in b
        return iter(self.items)

    # --- مقایسه ---
    def __eq__(self, other):            # b1 == b2
        return self.items == other.items
    def __ne__(self, other):            # b1 != b2  (معمولاً لازم نیست؛ خودکار از __eq__)
        return not self == other
    def __lt__(self, other):            # b1 < b2
        return len(self) < len(other)
    def __le__(self, other):            # b1 <= b2
        return len(self) <= len(other)
    def __gt__(self, other):            # b1 > b2
        return len(self) > len(other)
    def __ge__(self, other):            # b1 >= b2
        return len(self) >= len(other)

    # --- ریاضی ---
    def __add__(self, other):           # b1 + b2
        return Box(self.items + other.items)
    def __mul__(self, n):               # b * 3
        return Box(self.items * n)
    def __iadd__(self, other):          # b += x
        self.items += other.items
        return self                     # ⚠️ باید self برگردونه

    # --- صدا زدن آبجکت مثل تابع ---
    def __call__(self, x):              # b(5)
        return x in self.items

# دیگر ریاضی: __sub__ -  __truediv__ /  __floordiv__ //  __mod__ %  __pow__ **
# __neg__ (-b)  __abs__ (abs(b))  __radd__ (3 + b: وقتی سمت چپ آبجکت ما نیست)

# --- همیشه اگه __eq__ تعریف کردی و می‌خوای آبجکت داخل set یا کلید dict بره ---
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return isinstance(other, Point) and (self.x, self.y) == (other.x, other.y)
    def __hash__(self):                 # بدون این، آبجکت hashable نیست
        return hash((self.x, self.y))
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

# --- مقایسه‌ی همه‌ی عملگرها با یه میان‌بر ---
# from functools import total_ordering
# @total_ordering  → فقط __eq__ و یکی از __lt__/... رو بنویس، بقیه خودکار

# --- مدیریت منابع با with (context manager) ---
class Timer:
    def __enter__(self):                # شروع with
        print('start')
        return self
    def __exit__(self, exc_type, exc, tb):   # پایان with (حتی با ارور)
        print('end')
        return False                    # False: ارور رو قورت نده
# with Timer() as t: ...

# --- مثال: __next__ و iterator ---
class Counter:
    def __init__(self, n):
        self.n, self.i = n, 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration         # پایان پیمایش
        self.i += 1
        return self.i
# for x in Counter(3): print(x)         # 1 2 3

# __del__ (موقع حذف آبجکت)  __new__ (قبل از __init__، ساخت واقعی)  — کم استفاده


# ==========================================================================
# 20. ارث‌بری (inheritance)
# ==========================================================================
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        return f'hi, I am {self.name}'

    def __str__(self):
        return f'Person({self.name})'

class Teacher(Person):                  # Teacher از Person ارث می‌بره
    def __init__(self, name, age, course):
        super().__init__(name, age)     # سازنده‌ی پدر رو صدا بزن (خیلی مهم!)
        self.course = course

    def hello(self):                    # override: بازنویسی متد پدر
        return super().hello() + f' and I teach {self.course}'

class Student2(Person):                 # بدون __init__ جدید: همون سازنده‌ی پدر
    pass

t = Teacher('ali', 40, 'math')
t.name                                  # از پدر
t.hello()                               # نسخه‌ی بازنویسی‌شده
isinstance(t, Teacher)                  # True
isinstance(t, Person)                   # True  (بچه، یه جور پدره هم هست)
issubclass(Teacher, Person)             # True
type(t) == Person                       # False (type دقیقاً نوع خودش)

# --- ارث‌بری چندگانه (multiple inheritance) ---
class A:
    def who(self): return 'A'
class B:
    def who(self): return 'B'
class C(A, B):                          # اول A، بعد B
    pass
C().who()                               # 'A'
C.mro()                                 # ترتیب جستجوی متدها (MRO): C → A → B → object

# --- ارث‌بری چندسطحی ---
class Animal: pass
class Dog(Animal): pass
class Puppy(Dog): pass                  # Puppy → Dog → Animal → object

# --- قانون: «است یک» (is-a) = ارث‌بری ، «دارد» (has-a) = composition ---
# Dog «است یک» Animal  ✔      Car «دارد» Engine  ✔ (Engine رو ارث نمی‌بره)

# --- نکته: متدهای پدر رو از بچه مستقیم هم می‌شه صدا زد ---
# Person.hello(t)   یا   super().hello()


# ==========================================================================
# 21. چند شکلی (polymorphism)
# ==========================================================================
# یه اسم، رفتارهای متفاوت. سه شکل داره:

# ۱) override در ارث‌بری
class Animal:
    def speak(self):
        return '...'
class Cat(Animal):
    def speak(self):
        return 'meow'
class Dog(Animal):
    def speak(self):
        return 'woof'
for a in [Cat(), Dog(), Animal()]:
    print(a.speak())                    # هرکدوم به روش خودش

# ۲) duck typing: «اگه مثل اردک راه می‌ره و کواک می‌کنه، اردکه»
class Robot:
    def speak(self):
        return 'beep'                   # ارث نمی‌بره ولی speak داره → کار می‌کنه
for x in [Cat(), Robot()]:
    print(x.speak())

# ۳) operator overloading (dunder ها): + برای عدد جمع، برای رشته چسبوندن
1 + 2           # 3
'a' + 'b'       # 'ab'
# Point(1,2) + Point(3,4) با __add__
# len() روی رشته، لیست، دیکشنری و آبجکت خودمون با __len__

# --- مثال کامل با abstract ---
# Shape → Circle, Rectangle با area() متفاوت؛ یه حلقه روی همه: s.area()


# ==========================================================================
# 22. classmethod و staticmethod
# ==========================================================================
class Task:
    count = 0

    def __init__(self, title, is_done=False):
        self.title = title
        self.is_done = is_done
        Task.count += 1

    # --- متد معمولی (instance): ورودی اولش self ---
    def mark_done(self):
        self.is_done = True

    # --- classmethod: ورودی اولش cls (خود کلاس) ---
    @classmethod
    def from_string(cls, text):         # سازنده‌ی جایگزین (alternative constructor)
        title, is_done = text.split(',')
        return cls(title.strip(), is_done.strip() == 'True')
    # چرا cls و نه Task؟ چون اگه یه بچه‌کلاس ازش استفاده کنه، آبجکتِ خودِ بچه ساخته می‌شه

    @classmethod
    def total(cls):                     # کار با ویژگی کلاس
        return cls.count

    # --- staticmethod: نه self نه cls؛ تابع معمولی داخل کلاس ---
    @staticmethod
    def is_valid(title):
        return title.strip() != ''

t = Task.from_string('sleep, False')    # بدون ساختن آبجکت اولیه صدا زده می‌شه
Task.is_valid('abc')                    # True
Task.total()                            # تعداد آبجکت‌ها
t.is_valid('x')                         # از روی آبجکت هم می‌شه

# --- فرق سه‌تا ---
#                 اولین ورودی   به ویژگی آبجکت   به ویژگی کلاس   کاربرد
#  instance         self            ✔                ✔           کار با داده‌ی همین آبجکت
#  classmethod      cls             ✘                ✔           ساخت جایگزین، کار با داده‌ی کلاس
#  staticmethod     —               ✘                ✘           تابع کمکی مرتبط با کلاس
# قانون ساده: به self یا cls نیاز نداری؟ staticmethod


# ==========================================================================
# 23. کلاس انتزاعی (abstract class)
# ==========================================================================
# کلاسی که فقط «قالبه»: از خودش آبجکت ساخته نمی‌شه، بچه‌ها باید متدهاش رو بنویسن
from abc import ABC, abstractmethod
import math

class Shape(ABC):                       # ABC = Abstract Base Class
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):                     # بچه‌ها «حتماً» باید بنویسنش
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):                 # متد معمولی: بچه‌ها همینو ارث می‌برن
        return f'{self.name}: area={self.area():.2f}'

class Circle(Shape):
    def __init__(self, r):
        super().__init__('circle')
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
    def perimeter(self):
        return 2 * math.pi * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        super().__init__('rectangle')
        self.w, self.h = w, h
    def area(self):
        return self.w * self.h
    def perimeter(self):
        return 2 * (self.w + self.h)

# Shape('x')                            # TypeError: نمی‌شه آبجکت ساخت
# کلاسی که فقط یکی از متدهای abstract رو بنویسه، هنوز abstract است و آبجکت نمی‌شه ساخت
shapes = [Circle(2), Rectangle(3, 4)]
for s in shapes:
    print(s.describe())                 # چند شکلی + abstract

# --- abstract property ---
class Account(ABC):
    @property
    @abstractmethod
    def rate(self):
        pass
# کلاس‌هایی که از ABC ارث نمی‌برن مجبور به نوشتن متدهای abstract نیستن


# ==========================================================================
# 24. property و getter/setter
# ==========================================================================
# _name با آندرلاین = «مقدار واقعی، به‌صورت قرارداد خصوصی»
# name بدون آندرلاین (property) = دروازه‌ی بیرونی
class Circle2:
    def __init__(self, radius):
        self.radius = radius            # ⚠️ از setter رد می‌شه (بدون آندرلاین!)

    @property
    def radius(self):                   # getter: c.radius
        return self._radius

    @radius.setter
    def radius(self, value):            # setter: c.radius = 5
        if value <= 0:
            raise ValueError('radius must be positive')
        self._radius = value            # ⚠️ با self._radius ذخیره کن، نه self.radius (بازگشتی بی‌نهایت!)

    @radius.deleter                     # del c.radius (کم استفاده)
    def radius(self):
        del self._radius

    @property
    def area(self):                     # فقط‌خواندنی (read-only): setter نداره
        return 3.14 * self._radius ** 2

c = Circle2(2)
c.radius                                # 2     (getter)
c.radius = 5                            # setter
# c.radius = -1                         # ValueError
c.area                                  # بدون پرانتز! مثل ویژگی خونده می‌شه
# c.area = 3                            # AttributeError (read-only)

# --- مثال: حساب بانکی با موجودی فقط‌خواندنی ---
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance         # مقدار واقعی
        self.transactions = []

    @property
    def balance(self):                  # بیرون فقط می‌خونه
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('amount must be positive')
        self._balance += amount         # فقط داخل کلاس عوض می‌شه
        self.transactions.append(('deposit', amount))

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError('not enough money')
        self._balance -= amount
        self.transactions.append(('withdraw', amount))

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

    def __str__(self):
        return f'{self.owner}: {self._balance}'


# ==========================================================================
# 25. private / public 🔜 (هنوز با هم کار نکردیم)
# ==========================================================================
# پایتون «واقعاً» private نداره؛ قراردادهای نام‌گذاریه:
class Demo:
    def __init__(self):
        self.public = 1                 # عمومی: از بیرون آزاد
        self._protected = 2             # یه آندرلاین: «لطفاً از بیرون دست نزن» (قرارداد)
        self.__private = 3              # دو آندرلاین: name mangling (اسمش عوض می‌شه)

    def get_private(self):              # راه تمیز: از داخل کلاس
        return self.__private

d = Demo()
d.public                                # 1
d._protected                            # 2 (کار می‌کنه ولی قرارداده که نباید)
# d.__private                           # AttributeError
d.get_private()                         # 3  ← دسترسی درست از بیرون (با متد/property)
d._Demo__private                        # 3  ← دسترسی اجباری (کار تمیزی نیست)
# راه استاندارد برای دسترسی کنترل‌شده: property (بخش ۲۴)
# متد هم می‌تونه _ یا __ داشته باشه:  def _helper(self)  /  def __secret(self)


# ==========================================================================
# 26. decorator 🔜 (هنوز با هم کار نکردیم)
# ==========================================================================
# decorator = تابعی که یه تابع دیگه رو می‌گیره و «چیزی بهش اضافه» می‌کنه
def log(func):
    def wrapper(*args, **kwargs):
        print('calling', func.__name__)
        result = func(*args, **kwargs)
        print('done')
        return result
    return wrapper

@log                                    # یعنی: hello = log(hello)
def hello(name):
    return f'hi {name}'
# hello('sara')  → اول 'calling hello' چاپ می‌شه، بعد نتیجه

# دکوریتورهایی که تا الان دیدی: @classmethod  @staticmethod  @property  @abstractmethod
# import functools → @functools.wraps(func) برای حفظ اسم و docstring تابع اصلی


# ==========================================================================
# 27. مثال‌های تکمیلی (الگوهای پرتکرار)
# ==========================================================================
# --- Stack (پشته) ---
class Stack:
    def __init__(self):
        self._items = []
    def push(self, x):
        self._items.append(x)
    def pop(self):
        if self.is_empty():
            raise IndexError('stack is empty')
        return self._items.pop()
    def peek(self):
        return self._items[-1]
    def is_empty(self):
        return len(self._items) == 0
    def __len__(self):
        return len(self._items)

# --- Library: Book + Library (composition) ---
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
    def __str__(self):
        return f'{self.title} by {self.author}'

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def find(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        return None
    def borrow(self, title):
        book = self.find(title)
        if book is None:
            raise ValueError('book not found')
        if not book.available:
            raise ValueError('book is already borrowed')
        book.available = False
    def __len__(self):
        return len(self.books)

# --- ارث‌بری: Employee → Manager ---
class Employee:
    def __init__(self, name, salary):
        self.name, self.salary = name, salary
    def pay(self):
        return self.salary
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    def pay(self):                      # override + super
        return super().pay() + self.bonus
staff = [Employee('ali', 100), Manager('sara', 200, 50)]
total_pay = sum(e.pay() for e in staff)     # چند شکلی

# --- مرتب‌سازی آبجکت‌ها ---
# sorted(staff, key=lambda e: e.salary)
# یا __lt__ تعریف کن و مستقیم sorted(staff) بزن

# --- ذخیره‌ی آبجکت‌ها توی فایل با JSON ---
# to_dict:   return {'title': self.title, 'is_done': self.is_done}
# from_dict (classmethod):  return cls(d['title'], d['is_done'])


# ##########################################################################
#                              28. Git
# ##########################################################################
# --- شروع ---
# git init                         ساخت repo جدید تو پوشه
# git clone <url>                  دانلود repo از GitHub
# git config --global user.name "Sara"
# git config --global user.email "me@mail.com"
#
# --- چرخه‌ی روزمره ---
# git status                       وضعیت فایل‌ها (قرمز = جدید/تغییرکرده، سبز = آماده‌ی commit)
# git diff                         چی تغییر کرده (هنوز add نشده)
# git add file.py                  فایل مشخص رو آماده‌ی commit کن
# git add .                        همه‌ی فایل‌ها (با احتیاط)
# git commit -m "message"          ثبت تغییرات با یه پیام واضح
# git push                         فرستادن به GitHub
# git pull                         گرفتن آخرین تغییرات از GitHub
#
# --- تاریخچه ---
# git log                          تاریخچه‌ی commit ها
# git log --oneline                خلاصه، یه خط برای هر commit
#
# --- .gitignore: فایل‌هایی که نباید وارد git بشن ---
# __pycache__/
# *.pyc
# .venv/
# data.json   (اگه خصوصیه)
#
# --- branch (شاخه) ---
# git branch                       لیست شاخه‌ها
# git branch new-feature           ساخت شاخه
# git checkout new-feature         رفتن به شاخه  (یا: git switch new-feature)
# git checkout -b new-feature      ساخت + رفتن
# git merge new-feature            ادغام شاخه تو شاخه‌ی فعلی
#
# --- برگشت (با دقت!) ---
# git restore file.py              پس گرفتن تغییرات add نشده
# git restore --staged file.py     برگردوندن از حالت add شده
# git commit --amend               ویرایش آخرین commit (قبل از push)